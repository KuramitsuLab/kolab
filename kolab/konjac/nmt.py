import math
import torchtext
import torch
import torch.nn as nn
from torchtext.data.utils import get_tokenizer
from collections import Counter
from torchtext.data.metrics import bleu_score
from torchtext.vocab import Vocab
from torchtext.utils import download_from_url, extract_archive
from torch.nn import (TransformerEncoder, TransformerDecoder,
                      TransformerEncoderLayer, TransformerDecoderLayer)
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader
from torch import Tensor
from torchtext.data.metrics import bleu_score
import pandas as pd
from sklearn.model_selection import train_test_split
import sentencepiece as spm
import csv
import io
import time

SEED = 1234

torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.use_deterministic_algorithms(True)

specials = ['<unk>', '<pad>', '<sos>', '<eos>', '<blk>', '</blk>', '<sep>', '<A>', '<B>', '<C>', '<D>', '<E>', '<F>', '<G>', '<H>', '<I>', '<J>', '<K>', '<L>', '<M>', '<N>', '<O>', '<P>', '<Q>', '<R>', '<S>', '<T>', '<U>', '<V>', '<W>', '<X>', '<Y>', '<Z>', '<a>', '<b>', '<c>', '<d>', '<e>', '<f>', '<g>', '<h>', '<i>', '<j>', '<k>', '<l>', '<m>', '<n>', '<o>', '<p>', '<q>', '<r>', '<s>', '<t>', '<u>', '<v>', '<w>', '<x>', '<y>', '<z>']

def from_tsv(in_path, outdir_path, drop=True):
    df = pd.read_table(in_path, header=None)
    df = df.dropna()

    if drop:
      print('BEFORE_shape', df.shape)
      df.drop_duplicates(inplace=True)
      print('AFTER_shape', df.shape)
    else:
      print('shape', df.shape)

    df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)
    df_valid, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

    df_train.to_csv(outdir_path + '/train.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
    df_train.to_csv(outdir_path + '/train.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
    df_valid.to_csv(outdir_path + '/valid.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
    df_valid.to_csv(outdir_path + '/valid.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
    df_test.to_csv(outdir_path + '/test.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
    df_test.to_csv(outdir_path + '/test.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')

def build_vocab(filepath, tokenizer):
  counter = Counter()
  with io.open(filepath, encoding="utf8") as f:
    for string_ in f:
      counter.update(tokenizer(string_))
  return Vocab(counter, specials=specials)

def data_process(filepaths, src_vocab, tgt_vocab, src_tokenizer, tgt_tokenizer):
  raw_src_iter = iter(io.open(filepaths[0], encoding="utf8"))
  raw_tgt_iter = iter(io.open(filepaths[1], encoding="utf8"))
  data = []
  for (raw_src, raw_tgt) in zip(raw_src_iter, raw_tgt_iter):
    src_tensor_ = torch.tensor([src_vocab[token] for token in src_tokenizer(raw_src.rstrip("\n"))],
                            dtype=torch.long)
    tgt_tensor_ = torch.tensor([tgt_vocab[token] for token in tgt_tokenizer(raw_tgt.rstrip("\n"))],
                            dtype=torch.long)
    data.append((src_tensor_, tgt_tensor_))
  return data

def data_process_sentence(filepaths):
  raw_src_iter = iter(io.open(filepaths[0], encoding="utf8"))
  raw_tgt_iter = iter(io.open(filepaths[1], encoding="utf8"))
  data = []
  for (raw_src, raw_tgt) in zip(raw_src_iter, raw_tgt_iter):
    src_ = "".join([token for token in raw_src.rstrip("\n")])
    tgt_ = "".join([token for token in raw_tgt.rstrip("\n")])
    data.append((src_, tgt_))
  return data



# def generate_batch(data_batch):
#   src_batch, tgt_batch = [], []
#   for (src_item, tgt_item) in data_batch:
#     src_batch.append(torch.cat([torch.tensor([SOS_IDX]), src_item, torch.tensor([EOS_IDX])], dim=0))
#     tgt_batch.append(torch.cat([torch.tensor([SOS_IDX]), tgt_item, torch.tensor([EOS_IDX])], dim=0))
#   src_batch = pad_sequence(src_batch, padding_value=PAD_IDX)
#   tgt_batch = pad_sequence(tgt_batch, padding_value=PAD_IDX)
#   return src_batch, tgt_batch




class Seq2SeqTransformer(nn.Module):
    def __init__(self, num_encoder_layers: int, num_decoder_layers: int,
                 emb_size: int, src_vocab_size: int, tgt_vocab_size: int,
                 dim_feedforward:int = 512, dropout:float = 0.1):
        super(Seq2SeqTransformer, self).__init__()
        encoder_layer = TransformerEncoderLayer(d_model=emb_size, nhead=NHEAD,
                                                dim_feedforward=dim_feedforward)
        self.transformer_encoder = TransformerEncoder(encoder_layer, num_layers=num_encoder_layers)
        decoder_layer = TransformerDecoderLayer(d_model=emb_size, nhead=NHEAD,
                                                dim_feedforward=dim_feedforward)
        self.transformer_decoder = TransformerDecoder(decoder_layer, num_layers=num_decoder_layers)
                
        self.generator = nn.Linear(emb_size, tgt_vocab_size)
        self.src_tok_emb = TokenEmbedding(src_vocab_size, emb_size)
        self.tgt_tok_emb = TokenEmbedding(tgt_vocab_size, emb_size)
        self.positional_encoding = PositionalEncoding(emb_size, dropout=dropout)

    def forward(self, src: Tensor, tgt: Tensor, src_mask: Tensor,
                tgt_mask: Tensor, src_padding_mask: Tensor,
                tgt_padding_mask: Tensor, memory_key_padding_mask: Tensor):
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
    def __init__(self, emb_size: int, dropout, maxlen: int = 5000):
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

# def generate_square_subsequent_mask(sz):
#     mask = (torch.triu(torch.ones((sz, sz), device=DEVICE)) == 1).transpose(0, 1)
#     mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
#     return mask

# def create_mask(src, tgt):
#   src_seq_len = src.shape[0]
#   tgt_seq_len = tgt.shape[0]

#   tgt_mask = generate_square_subsequent_mask(tgt_seq_len)
#   src_mask = torch.zeros((src_seq_len, src_seq_len), device=DEVICE).type(torch.bool)

#   src_padding_mask = (src == PAD_IDX).transpose(0, 1)
#   tgt_padding_mask = (tgt == PAD_IDX).transpose(0, 1)
#   return src_mask, tgt_mask, src_padding_mask, tgt_padding_mask

# def train_epoch(model, train_iter, optimizer):
#   model.train()
#   losses = 0
#   for idx, (src, tgt) in enumerate(train_iter):
#       src = src.to(device)
#       tgt = tgt.to(device)
            
#       tgt_input = tgt[:-1, :]

#       src_mask, tgt_mask, src_padding_mask, tgt_padding_mask = create_mask(src, tgt_input)

#       logits = model(src, tgt_input, src_mask, tgt_mask,
#                                 src_padding_mask, tgt_padding_mask, src_padding_mask)
      
#       optimizer.zero_grad()
      
#       tgt_out = tgt[1:,:]
#       loss = loss_fn(logits.reshape(-1, logits.shape[-1]), tgt_out.reshape(-1))
#       loss.backward()

#       optimizer.step()
#       losses += loss.item()
#   return losses / len(train_iter)


# def evaluate(model, val_iter):
#   model.eval()
#   losses = 0
#   for idx, (src, tgt) in (enumerate(valid_iter)):
#     src = src.to(device)
#     tgt = tgt.to(device)

#     tgt_input = tgt[:-1, :]

#     src_mask, tgt_mask, src_padding_mask, tgt_padding_mask = create_mask(src, tgt_input)

#     logits = model(src, tgt_input, src_mask, tgt_mask,
#                               src_padding_mask, tgt_padding_mask, src_padding_mask)
#     tgt_out = tgt[1:,:]
#     loss = loss_fn(logits.reshape(-1, logits.shape[-1]), tgt_out.reshape(-1))
#     losses += loss.item()
#   return losses / len(val_iter)

# def greedy_decode(model, src, src_mask, max_len, start_symbol):
#     src = src.to(device)
#     src_mask = src_mask.to(device)

#     memory = model.encode(src, src_mask)
#     ys = torch.ones(1, 1).fill_(start_symbol).type(torch.long).to(device)
#     for i in range(max_len-1):
#         memory = memory.to(device)
#         memory_mask = torch.zeros(ys.shape[0], memory.shape[0]).to(device).type(torch.bool)
#         tgt_mask = (generate_square_subsequent_mask(ys.size(0))
#                                     .type(torch.bool)).to(device)
#         out = model.decode(ys, memory, tgt_mask)
#         out = out.transpose(0, 1)
#         prob = model.generator(out[:, -1])
#         _, next_word = torch.max(prob, dim = 1)
#         next_word = next_word.item()

#         ys = torch.cat([ys,
#                         torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=0)
#         if next_word == EOS_IDX:
#           break
#     return ys

# def translate(model, src, src_vocab, tgt_vocab, src_tokenizer):
#   model.eval()
#   tokens = [SOS_IDX] + [src_vocab.stoi[tok] for tok in src_tokenizer(src)]+ [EOS_IDX]
#   num_tokens = len(tokens)
#   src = (torch.LongTensor(tokens).reshape(num_tokens, 1) )
#   src_mask = (torch.zeros(num_tokens, num_tokens)).type(torch.bool)
#   tgt_tokens = greedy_decode(model,  src, src_mask, max_len=num_tokens + 5, start_symbol=SOS_IDX).flatten()

#   trans_list = [tgt_vocab.itos[tok] for tok in tgt_tokens]
#   if '<sos>' in trans_list:
#     trans_list.remove('<sos>')
#   if '<eos>' in trans_list:
#     trans_list.remove('<eos>')

#   trans_str = " ".join(trans_list)

#   return trans_str, trans_list

# def calc_bleu(data, model, src_vocab, tgt_vocab, src_tokenizer, tgt_tokenizer):
#     tgts = []
#     pred_tgts = []
    
#     for idx in data:
#         src = idx[0]
#         tgt = tgt_tokenizer(idx[1])

#         _, pred_tgt = translate(model, src, src_vocab, tgt_vocab, src_tokenizer)
        
#         pred_tgts.append(pred_tgt)
#         tgts.append([tgt])

#     return bleu_score(pred_tgts, tgts)