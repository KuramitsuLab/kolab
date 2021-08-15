import torch
import torchtext
import torch.nn as nn
from torch.nn import (TransformerEncoder, TransformerDecoder,
                      TransformerEncoderLayer, TransformerDecoderLayer)
from torchtext.vocab import Vocab, build_vocab_from_iterator
from torchtext.utils import unicode_csv_reader
from torchtext.data.datasets_utils import _RawTextIterableDataset
from torch import Tensor
from typing import Iterable, List
import sentencepiece as spm
import io
import math
import pandas as pd
import csv
from sklearn.model_selection import train_test_split

UNK_IDX, PAD_IDX, SOS_IDX, EOS_IDX = 0, 1, 2, 3

# tsv ファイルから train/valid/test それぞれのファイルを作成する関数
def from_tsv(f_path):
  df = pd.read_table(f_path, header=None)
  # 欠損値の削除
  df = df.dropna()
  print('BEFORE', df.shape)

  # 重複データの削除
  df.drop_duplicates(inplace=True)
  df = df.reset_index(drop=True)
  print('AFTER_drop', df.shape)

  # データ数の調整
  # df = df.iloc[range(2674), :]
  # print('AFTER_iloc', df.shape)

  df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)
  df_valid, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

  df_train.to_csv('data/train.tsv', header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
  df_valid.to_csv('data/valid.tsv', header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
  df_test.to_csv('data/test.tsv', header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')

  NUM_LINES = {
      'train': len(df_train),
      'valid': len(df_valid),
      'test': len(df_test),
  }

  return NUM_LINES

class Seq2SeqTransformer(nn.Module):
    def __init__(self, 
                 num_encoder_layers: int, 
                 num_decoder_layers: int,
                 emb_size: int, 
                 nhead: int, 
                 src_vocab_size: int, 
                 tgt_vocab_size: int,
                 dim_feedforward: int = 512, 
                 dropout: float = 0.1):
        super(Seq2SeqTransformer, self).__init__()
        encoder_layer = TransformerEncoderLayer(d_model=emb_size, nhead=nhead,
                                                dim_feedforward=dim_feedforward)
        self.transformer_encoder = TransformerEncoder(encoder_layer, num_layers=num_encoder_layers)
        decoder_layer = TransformerDecoderLayer(d_model=emb_size, nhead=nhead,
                                                dim_feedforward=dim_feedforward)
        self.transformer_decoder = TransformerDecoder(decoder_layer, num_layers=num_decoder_layers)
        
        self.generator = nn.Linear(emb_size, tgt_vocab_size)
        self.src_tok_emb = TokenEmbedding(src_vocab_size, emb_size)
        self.tgt_tok_emb = TokenEmbedding(tgt_vocab_size, emb_size)
        self.positional_encoding = PositionalEncoding(emb_size, dropout=dropout)

    def forward(self, 
                src: Tensor, 
                tgt: Tensor, 
                src_mask: Tensor,
                tgt_mask: Tensor, 
                src_padding_mask: Tensor,
                tgt_padding_mask: Tensor, 
                memory_key_padding_mask: Tensor):
        src_emb = self.positional_encoding(self.src_tok_emb(src))
        tgt_emb = self.positional_encoding(self.tgt_tok_emb(tgt))
        memory = self.transformer_encoder(src_emb, src_mask, src_padding_mask)
        outs = self.transformer_decoder(tgt_emb, memory, tgt_mask, None,
                                        tgt_padding_mask, memory_key_padding_mask)
        return self.generator(outs)

    def encode(self, src: Tensor, src_mask: Tensor):
        return self.transformer_encoder(self.positional_encoding(
                            self.src_tok_emb(src)), src_mask)

    def decode(self, tgt: Tensor, memory: Tensor, tgt_mask: Tensor):
        return self.transformer_decoder(self.positional_encoding(
                          self.tgt_tok_emb(tgt)), memory,
                          tgt_mask)

class PositionalEncoding(nn.Module):
    def __init__(self, 
                 emb_size: int, 
                 dropout: float, 
                 maxlen: int = 5000):
        super(PositionalEncoding, self).__init__()
        den = torch.exp(- torch.arange(0, emb_size, 2) * math.log(10000) / emb_size)
        pos = torch.arange(0, maxlen).reshape(maxlen, 1)
        pos_embedding = torch.zeros((maxlen, emb_size))
        pos_embedding[:, 0::2] = torch.sin(pos * den)
        pos_embedding[:, 1::2] = torch.cos(pos * den)
        pos_embedding = pos_embedding.unsqueeze(-2)

        self.dropout = nn.Dropout(dropout)
        self.register_buffer('pos_embedding', pos_embedding)

    def forward(self, token_embedding: Tensor):
        return self.dropout(token_embedding + 
                            self.pos_embedding[:token_embedding.size(0),:])

class TokenEmbedding(nn.Module):
    def __init__(self, vocab_size: int, emb_size):
        super(TokenEmbedding, self).__init__()
        self.embedding = nn.Embedding(vocab_size, emb_size)
        self.emb_size = emb_size
    def forward(self, tokens: Tensor):
        return self.embedding(tokens.long()) * math.sqrt(self.emb_size)

def generate_square_subsequent_mask(sz):
    mask = (torch.triu(torch.ones((sz, sz))) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask

def sequential_transforms(*transforms):
    def func(txt_input):
        for transform in transforms:
            txt_input = transform(txt_input)
        return txt_input
    return func

def tensor_transform(token_ids: List[int]):
    return torch.cat((torch.tensor([SOS_IDX]), 
                      torch.tensor(token_ids), 
                      torch.tensor([EOS_IDX])))

# greedy search を使って翻訳結果 (シーケンス) を生成 
def greedy_decode(model, src, src_mask, max_len, beamsize, start_symbol):
    memory = model.encode(src, src_mask)   # encode の出力 (コンテキストベクトル)

    ys = torch.ones(1, 1).fill_(start_symbol).type(torch.long)

    for i in range(max_len-1):
        tgt_mask = (generate_square_subsequent_mask(ys.size(0)).type(torch.bool))
        out = model.decode(ys, memory, tgt_mask)
        out = out.transpose(0, 1)
        prob = model.generator(out[:, -1])
        next_prob, next_word = prob.topk(k=beamsize, dim=1)

        next_word = next_word[:, 0]
        next_word = next_word.item()

        ys = torch.cat([ys,
                        torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=0)
        if next_word == EOS_IDX:
            break
    return ys

#greedy_decodeのトークン候補確率を出力するバージョン
def greedy_decode_output(model, src, src_mask, max_len, beamsize, start_symbol):
    memory = model.encode(src, src_mask)   # encode の出力 (コンテキストベクトル)

    ys = torch.ones(1, 1).fill_(start_symbol).type(torch.long)

    for i in range(max_len-1):
        tgt_mask = (generate_square_subsequent_mask(ys.size(0)).type(torch.bool))
        out = model.decode(ys, memory, tgt_mask)
        out = out.transpose(0, 1)
        prob = model.generator(out[:, -1])
        next_prob, next_word = prob.topk(k=beamsize, dim=1)
        print(f'次に来るトークン候補 : {next_word}')
        print(f'その確率 : {next_prob}')

        next_word = next_word[:, 0]
        next_word = next_word.item()

        ys = torch.cat([ys,
                        torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=0)
        if next_word == EOS_IDX:
            break
    return ys
