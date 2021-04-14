import torch
import torch.nn as nn
import torch.optim as optim

import torchtext
from torchtext.datasets import TranslationDataset
from torchtext.data import Field, BucketIterator

# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import japanize_matplotlib #日本語化 matplotlib
# import seaborn as sns
# sns.set(font="IPAexGothic") #日本語フォント設定

import numpy as np

import random
import math
import time

# import sentencepiece as spm

import pandas as pd
import csv
from sklearn.model_selection import train_test_split


import collections
from torchtext.data.utils import ngrams_iterator

# sentencepiece
# MAX_LEN=80
# def sp_model(text):
#     sp = spm.SentencePieceProcessor(model_file= text )
#     return sp

# def tokenize_jpn(text):
#   ss = [tok.replace('▁', '') for tok in sp.encode(text, out_type=str)][:MAX_LEN]
#   return [s for s in ss if len(s) != 0]

# Python はあらかじめ空白区切りに
# MAX_LEN=80
# def tokenize_py(text):
#     return [tok for tok in text.split()][:MAX_LEN]

# SRC = Field(tokenize = tokenize_jpn, 
#             init_token = '<sos>', 
#             eos_token = '<eos>', 
#             # lower = True, 
#             batch_first = True)

# TRG = Field(tokenize = tokenize_py, 
#             init_token = '<sos>', 
#             eos_token = '<eos>', 
#             # lower = True, 
#             batch_first = True)



# def from_tsv(f_path):
#   df = pd.read_table(f_path, header=None)
#   df = df.dropna()

#   print('BEFORE', df.shape)
#   df.drop_duplicates(inplace=True)
#   print('AFTER_drop', df.shape)

#   df_train, df_test = train_test_split(df, test_size=0.3, random_state=42)
#   df_valid, df_test = train_test_split(df_test, test_size=0.5, random_state=42)

#   df_train.to_csv('data/train.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
#   df_train.to_csv('data/train.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
#   df_valid.to_csv('data/valid.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
#   df_valid.to_csv('data/valid.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
#   df_test.to_csv('data/test.py', columns=[0], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')
#   df_test.to_csv('data/test.jpn', columns=[1], header=False, index=False, sep='\t', quoting=csv.QUOTE_NONE, doublequote=False, escapechar='\\')


# # from_tsv('corpus_Python-JPN/Corpus-AOJ/line-by-line/AOJ_orig.tsv')


# # ja => py
# train_data = TranslationDataset(path='data/train', exts=('.jpn', '.py'), fields=(SRC, TRG))
# valid_data = TranslationDataset(path='data/valid', exts=('.jpn', '.py'), fields=(SRC, TRG))
# test_data = TranslationDataset(path='data/test', exts=('.jpn', '.py'), fields=(SRC, TRG))

# # print(len(train_data), len(valid_data), len(test_data))


# # example_idx = 8

# # src = vars(train_data.examples[example_idx])['src']
# # trg = vars(train_data.examples[example_idx])['trg']

# # print(f'src = {src}')
# # print(f'trg = {trg}')

# SRC.build_vocab(train_data, min_freq = 2, specials=specials)
# TRG.build_vocab(train_data, min_freq = 2, specials=specials)

# BATCH_SIZE = 128

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# train_iterator, valid_iterator, test_iterator = BucketIterator.splits(
#     (train_data, valid_data, test_data), 
#      batch_size = BATCH_SIZE,
#      device = device)


class Encoder(nn.Module):
    def __init__(self, 
                 input_dim, 
                 hid_dim, 
                 n_layers, 
                 n_heads, 
                 pf_dim,
                 dropout, 
                 device,
                 max_length = 100):
        super().__init__()

        self.device = device
        
        self.tok_embedding = nn.Embedding(input_dim, hid_dim)
        self.pos_embedding = nn.Embedding(max_length, hid_dim)
        
        self.layers = nn.ModuleList([EncoderLayer(hid_dim, 
                                                  n_heads, 
                                                  pf_dim,
                                                  dropout, 
                                                  device) 
                                     for _ in range(n_layers)])
        
        self.dropout = nn.Dropout(dropout)
        
        self.scale = torch.sqrt(torch.FloatTensor([hid_dim])).to(device)
        
    def forward(self, src, src_mask):
        
        #src = [batch size, src len]
        #src_mask = [batch size, 1, 1, src len]
        
        batch_size = src.shape[0]
        src_len = src.shape[1]
        
        pos = torch.arange(0, src_len).unsqueeze(0).repeat(batch_size, 1).to(self.device)
        
        #pos = [batch size, src len]
        
        src = self.dropout((self.tok_embedding(src) * self.scale) + self.pos_embedding(pos))
        
        #src = [batch size, src len, hid dim]
        
        for layer in self.layers:
            src = layer(src, src_mask)
            
        #src = [batch size, src len, hid dim]
            
        return src

class EncoderLayer(nn.Module):
    def __init__(self, 
                 hid_dim, 
                 n_heads, 
                 pf_dim,  
                 dropout, 
                 device):
        super().__init__()
        
        self.self_attn_layer_norm = nn.LayerNorm(hid_dim)
        self.ff_layer_norm = nn.LayerNorm(hid_dim)
        self.self_attention = MultiHeadAttentionLayer(hid_dim, n_heads, dropout, device)
        self.positionwise_feedforward = PositionwiseFeedforwardLayer(hid_dim, 
                                                                     pf_dim, 
                                                                     dropout)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, src, src_mask):
        
        #src = [batch size, src len, hid dim]
        #src_mask = [batch size, 1, 1, src len] 
                
        #self attention
        _src, _ = self.self_attention(src, src, src, src_mask)
        
        #dropout, residual connection and layer norm
        src = self.self_attn_layer_norm(src + self.dropout(_src))
        
        #src = [batch size, src len, hid dim]
        
        #positionwise feedforward
        _src = self.positionwise_feedforward(src)
        
        #dropout, residual and layer norm
        src = self.ff_layer_norm(src + self.dropout(_src))
        
        #src = [batch size, src len, hid dim]
        
        return src

class MultiHeadAttentionLayer(nn.Module):
    def __init__(self, hid_dim, n_heads, dropout, device):
        super().__init__()
        
        assert hid_dim % n_heads == 0
        
        self.hid_dim = hid_dim
        self.n_heads = n_heads
        self.head_dim = hid_dim // n_heads
        
        self.fc_q = nn.Linear(hid_dim, hid_dim)
        self.fc_k = nn.Linear(hid_dim, hid_dim)
        self.fc_v = nn.Linear(hid_dim, hid_dim)
        
        self.fc_o = nn.Linear(hid_dim, hid_dim)
        
        self.dropout = nn.Dropout(dropout)
        
        self.scale = torch.sqrt(torch.FloatTensor([self.head_dim])).to(device)
        
    def forward(self, query, key, value, mask = None):
        
        batch_size = query.shape[0]
        
        #query = [batch size, query len, hid dim]
        #key = [batch size, key len, hid dim]
        #value = [batch size, value len, hid dim]
                
        Q = self.fc_q(query)
        K = self.fc_k(key)
        V = self.fc_v(value)
        
        #Q = [batch size, query len, hid dim]
        #K = [batch size, key len, hid dim]
        #V = [batch size, value len, hid dim]
                
        Q = Q.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        K = K.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        V = V.view(batch_size, -1, self.n_heads, self.head_dim).permute(0, 2, 1, 3)
        
        #Q = [batch size, n heads, query len, head dim]
        #K = [batch size, n heads, key len, head dim]
        #V = [batch size, n heads, value len, head dim]
                
        energy = torch.matmul(Q, K.permute(0, 1, 3, 2)) / self.scale
        
        #energy = [batch size, n heads, query len, key len]
        
        if mask is not None:
            energy = energy.masked_fill(mask == 0, -1e10)
        
        attention = torch.softmax(energy, dim = -1)
                
        #attention = [batch size, n heads, query len, key len]
                
        x = torch.matmul(self.dropout(attention), V)
        
        #x = [batch size, n heads, query len, head dim]
        
        x = x.permute(0, 2, 1, 3).contiguous()
        
        #x = [batch size, query len, n heads, head dim]
        
        x = x.view(batch_size, -1, self.hid_dim)
        
        #x = [batch size, query len, hid dim]
        
        x = self.fc_o(x)
        
        #x = [batch size, query len, hid dim]
        
        return x, attention

class PositionwiseFeedforwardLayer(nn.Module):
    def __init__(self, hid_dim, pf_dim, dropout):
        super().__init__()
        
        self.fc_1 = nn.Linear(hid_dim, pf_dim)
        self.fc_2 = nn.Linear(pf_dim, hid_dim)
        
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x):
        
        #x = [batch size, seq len, hid dim]
        
        x = self.dropout(torch.relu(self.fc_1(x)))
        
        #x = [batch size, seq len, pf dim]
        
        x = self.fc_2(x)
        
        #x = [batch size, seq len, hid dim]
        
        return x

class Decoder(nn.Module):
    def __init__(self, 
                 output_dim, 
                 hid_dim, 
                 n_layers, 
                 n_heads, 
                 pf_dim, 
                 dropout, 
                 device,
                 max_length = 100):
        super().__init__()
        
        self.device = device
        
        self.tok_embedding = nn.Embedding(output_dim, hid_dim)
        self.pos_embedding = nn.Embedding(max_length, hid_dim)
        
        self.layers = nn.ModuleList([DecoderLayer(hid_dim, 
                                                  n_heads, 
                                                  pf_dim, 
                                                  dropout, 
                                                  device)
                                     for _ in range(n_layers)])
        
        self.fc_out = nn.Linear(hid_dim, output_dim)
        
        self.dropout = nn.Dropout(dropout)
        
        self.scale = torch.sqrt(torch.FloatTensor([hid_dim])).to(device)
        
    def forward(self, trg, enc_src, trg_mask, src_mask):
        
        #trg = [batch size, trg len]
        #enc_src = [batch size, src len, hid dim]
        #trg_mask = [batch size, 1, trg len, trg len]
        #src_mask = [batch size, 1, 1, src len]
                
        batch_size = trg.shape[0]
        trg_len = trg.shape[1]
        
        pos = torch.arange(0, trg_len).unsqueeze(0).repeat(batch_size, 1).to(self.device)
                            
        #pos = [batch size, trg len]
            
        trg = self.dropout((self.tok_embedding(trg) * self.scale) + self.pos_embedding(pos))
                
        #trg = [batch size, trg len, hid dim]
        
        for layer in self.layers:
            trg, attention = layer(trg, enc_src, trg_mask, src_mask)
        
        #trg = [batch size, trg len, hid dim]
        #attention = [batch size, n heads, trg len, src len]
        
        output = self.fc_out(trg)
        
        #output = [batch size, trg len, output dim]
            
        return output, attention

class DecoderLayer(nn.Module):
    def __init__(self, 
                 hid_dim, 
                 n_heads, 
                 pf_dim, 
                 dropout, 
                 device):
        super().__init__()
        
        self.self_attn_layer_norm = nn.LayerNorm(hid_dim)
        self.enc_attn_layer_norm = nn.LayerNorm(hid_dim)
        self.ff_layer_norm = nn.LayerNorm(hid_dim)
        self.self_attention = MultiHeadAttentionLayer(hid_dim, n_heads, dropout, device)
        self.encoder_attention = MultiHeadAttentionLayer(hid_dim, n_heads, dropout, device)
        self.positionwise_feedforward = PositionwiseFeedforwardLayer(hid_dim, 
                                                                     pf_dim, 
                                                                     dropout)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, trg, enc_src, trg_mask, src_mask):
        
        #trg = [batch size, trg len, hid dim]
        #enc_src = [batch size, src len, hid dim]
        #trg_mask = [batch size, 1, trg len, trg len]
        #src_mask = [batch size, 1, 1, src len]
        
        #self attention
        _trg, _ = self.self_attention(trg, trg, trg, trg_mask)
        
        #dropout, residual connection and layer norm
        trg = self.self_attn_layer_norm(trg + self.dropout(_trg))
            
        #trg = [batch size, trg len, hid dim]
            
        #encoder attention
        _trg, attention = self.encoder_attention(trg, enc_src, enc_src, src_mask)
        
        #dropout, residual connection and layer norm
        trg = self.enc_attn_layer_norm(trg + self.dropout(_trg))
                    
        #trg = [batch size, trg len, hid dim]
        
        #positionwise feedforward
        _trg = self.positionwise_feedforward(trg)
        
        #dropout, residual and layer norm
        trg = self.ff_layer_norm(trg + self.dropout(_trg))
        
        #trg = [batch size, trg len, hid dim]
        #attention = [batch size, n heads, trg len, src len]
        
        return trg, attention

class Seq2Seq(nn.Module):
    def __init__(self, 
                 encoder, 
                 decoder, 
                 src_pad_idx, 
                 trg_pad_idx, 
                 device):
        super().__init__()
        
        self.encoder = encoder
        self.decoder = decoder
        self.src_pad_idx = src_pad_idx
        self.trg_pad_idx = trg_pad_idx
        self.device = device
        
    def make_src_mask(self, src):
        
        #src = [batch size, src len]
        
        src_mask = (src != self.src_pad_idx).unsqueeze(1).unsqueeze(2)

        #src_mask = [batch size, 1, 1, src len]

        return src_mask
    
    def make_trg_mask(self, trg):
        
        #trg = [batch size, trg len]
        
        trg_pad_mask = (trg != self.trg_pad_idx).unsqueeze(1).unsqueeze(2)
        
        #trg_pad_mask = [batch size, 1, 1, trg len]
        
        trg_len = trg.shape[1]
        
        trg_sub_mask = torch.tril(torch.ones((trg_len, trg_len), device = self.device)).bool()
        
        #trg_sub_mask = [trg len, trg len]
            
        trg_mask = trg_pad_mask & trg_sub_mask
        
        #trg_mask = [batch size, 1, trg len, trg len]
        
        return trg_mask

    def forward(self, src, trg):
        
        #src = [batch size, src len]
        #trg = [batch size, trg len]
                
        src_mask = self.make_src_mask(src)
        trg_mask = self.make_trg_mask(trg)
        
        #src_mask = [batch size, 1, 1, src len]
        #trg_mask = [batch size, 1, trg len, trg len]
        
        enc_src = self.encoder(src, src_mask)
        
        #enc_src = [batch size, src len, hid dim]
                
        output, attention = self.decoder(trg, enc_src, trg_mask, src_mask)
        
        #output = [batch size, trg len, output dim]
        #attention = [batch size, n heads, trg len, src len]
        
        return output, attention

# INPUT_DIM = len(SRC.vocab)
# OUTPUT_DIM = len(TRG.vocab)
# HID_DIM = 256
# ENC_LAYERS = 3
# DEC_LAYERS = 3
# ENC_HEADS = 8
# DEC_HEADS = 8
# ENC_PF_DIM = 512
# DEC_PF_DIM = 512
# ENC_DROPOUT = 0.1
# DEC_DROPOUT = 0.1

# enc = Encoder(INPUT_DIM, 
#               HID_DIM, 
#               ENC_LAYERS, 
#               ENC_HEADS, 
#               ENC_PF_DIM, 
#               ENC_DROPOUT, 
#               device)

# dec = Decoder(OUTPUT_DIM, 
#               HID_DIM, 
#               DEC_LAYERS, 
#               DEC_HEADS, 
#               DEC_PF_DIM, 
#               DEC_DROPOUT, 
#               device)

# SRC_PAD_IDX = SRC.vocab.stoi[SRC.pad_token]
# TRG_PAD_IDX = TRG.vocab.stoi[TRG.pad_token]

# model = Seq2Seq(enc, dec, SRC_PAD_IDX, TRG_PAD_IDX, device).to(device)



def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

# print(f'The model has {count_parameters(model):,} trainable parameters')


def initialize_weights(m):
    if hasattr(m, 'weight') and m.weight.dim() > 1:
        nn.init.xavier_uniform_(m.weight.data)

model.apply(initialize_weights)


LEARNING_RATE = 0.0005

optimizer = torch.optim.Adam(model.parameters(), lr = LEARNING_RATE)

criterion = nn.CrossEntropyLoss(ignore_index = TRG_PAD_IDX)


# def train(model, iterator, optimizer, criterion, clip):
    
    # model.train()
    
    # epoch_loss = 0
    
    # for i, batch in enumerate(iterator):
        
    #     src = batch.src
    #     trg = batch.trg
        
    #     optimizer.zero_grad()
        
    #     output, _ = model(src, trg[:,:-1])
                
    #     #output = [batch size, trg len - 1, output dim]
    #     #trg = [batch size, trg len]
            
    #     output_dim = output.shape[-1]
            
    #     output = output.contiguous().view(-1, output_dim)
    #     trg = trg[:,1:].contiguous().view(-1)
                
    #     #output = [batch size * trg len - 1, output dim]
    #     #trg = [batch size * trg len - 1]
            
    #     loss = criterion(output, trg)
        
    #     loss.backward()
        
    #     torch.nn.utils.clip_grad_norm_(model.parameters(), clip)
        
    #     optimizer.step()
        
    #     epoch_loss += loss.item()
        
    # return epoch_loss / len(iterator)

# def evaluate(model, iterator, criterion):
    
#     model.eval()
    
#     epoch_loss = 0
    
#     with torch.no_grad():
    
#         for i, batch in enumerate(iterator):

#             src = batch.src
#             trg = batch.trg

#             output, _ = model(src, trg[:,:-1])
            
#             #output = [batch size, trg len - 1, output dim]
#             #trg = [batch size, trg len]
            
#             output_dim = output.shape[-1]
            
#             output = output.contiguous().view(-1, output_dim)
#             trg = trg[:,1:].contiguous().view(-1)
            
#             #output = [batch size * trg len - 1, output dim]
#             #trg = [batch size * trg len - 1]
            
#             loss = criterion(output, trg)

#             epoch_loss += loss.item()
        
#     return epoch_loss / len(iterator)

# def epoch_time(start_time, end_time):
#     elapsed_time = end_time - start_time
#     elapsed_mins = int(elapsed_time / 60)
#     elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
#     return elapsed_mins, elapsed_secs


# N_EPOCHS = 20  # 10から増やしてある
# CLIP = 1

# best_valid_loss = float('inf')

# for epoch in range(N_EPOCHS):
    
#     start_time = time.time()
    
#     train_loss = train(model, train_iterator, optimizer, criterion, CLIP)
#     valid_loss = evaluate(model, valid_iterator, criterion)
    
#     end_time = time.time()
    
#     epoch_mins, epoch_secs = epoch_time(start_time, end_time)
    
#     if valid_loss < best_valid_loss:
#         best_valid_loss = valid_loss
#         torch.save(model.state_dict(), 'tut6-model.pt')
    
#     print(f'Epoch: {epoch+1:02} | Time: {epoch_mins}m {epoch_secs}s')
#     print(f'\tTrain Loss: {train_loss:.3f} | Train PPL: {math.exp(train_loss):7.3f}')
#     print(f'\t Val. Loss: {valid_loss:.3f} |  Val. PPL: {math.exp(valid_loss):7.3f}')

# model.load_state_dict(torch.load('tut6-model.pt'))

# test_loss = evaluate(model, test_iterator, criterion)

# print(f'| Test Loss: {test_loss:.3f} | Test PPL: {math.exp(test_loss):7.3f} |')


def translate_sentence(sentence, src_field, trg_field, model, device, max_len = 50):
    
    model.eval()
        
    if isinstance(sentence, str):
        tokens = tokenize(sentence)
    else:
        # tokens = [token.lower() for token in sentence]
        tokens = [token for token in sentence]

    tokens = [src_field.init_token] + tokens + [src_field.eos_token]
        
    src_indexes = [src_field.vocab.stoi[token] for token in tokens]

    src_tensor = torch.LongTensor(src_indexes).unsqueeze(0).to(device)
    
    src_mask = model.make_src_mask(src_tensor)
    
    with torch.no_grad():
        enc_src = model.encoder(src_tensor, src_mask)

    trg_indexes = [trg_field.vocab.stoi[trg_field.init_token]]

    for i in range(max_len):

        trg_tensor = torch.LongTensor(trg_indexes).unsqueeze(0).to(device)

        trg_mask = model.make_trg_mask(trg_tensor)
        
        with torch.no_grad():
            output, attention = model.decoder(trg_tensor, enc_src, trg_mask, src_mask)
        
        pred_token = output.argmax(2)[:,-1].item()
        
        trg_indexes.append(pred_token)

        if pred_token == trg_field.vocab.stoi[trg_field.eos_token]:
            break
    
    trg_tokens = [trg_field.vocab.itos[i] for i in trg_indexes]
    
    return trg_tokens[1:], attention

# def display_attention(sentence, translation, attention, n_heads = 8, n_rows = 4, n_cols = 2):
    
#     assert n_rows * n_cols == n_heads
    
#     fig = plt.figure(figsize=(15,25))
    
#     for i in range(n_heads):
        
#         ax = fig.add_subplot(n_rows, n_cols, i+1)
        
#         _attention = attention.squeeze(0)[i].cpu().detach().numpy()

#         cax = ax.matshow(_attention, cmap='bone')

#         ax.tick_params(labelsize=12)
#         ax.set_xticklabels(['']+['<sos>']+[t.lower() for t in sentence]+['<eos>'], 
#                            rotation=45)
#         ax.set_yticklabels(['']+translation)

#         ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
#         ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

#     plt.show()
#     plt.close()



# example_idx = 8

# src = vars(train_data.examples[example_idx])['src']
# trg = vars(train_data.examples[example_idx])['trg']

# print(f'src = {src}')
# print(f'trg = {trg}')


# translation, attention = translate_sentence(src, SRC, TRG, model, device)

# print(f'predicted trg = {translation}')

# display_attention(src, translation, attention)




def _compute_ngram_counter(tokens, max_n):
    assert max_n > 0
    ngrams_counter = collections.Counter(tuple(x.split(' '))
                                         for x in ngrams_iterator(tokens, max_n))

    return ngrams_counter


def bleu_score(candidate_corpus, references_corpus, max_n=4, weights=[0.25] * 4):
    assert max_n == len(weights), 'Length of the "weights" list has be equal to max_n'
    assert len(candidate_corpus) == len(references_corpus),\
        'The length of candidate and reference corpus should be the same'

    clipped_counts = torch.zeros(max_n)
    total_counts = torch.zeros(max_n)
    weights = torch.tensor(weights)

    candidate_len = 0.0
    refs_len = 0.0

    for (candidate, refs) in zip(candidate_corpus, references_corpus):
        candidate_len += len(candidate)

        # Get the length of the reference that's closest in length to the candidate
        refs_len_list = [float(len(ref)) for ref in refs]
        refs_len += min(refs_len_list, key=lambda x: abs(len(candidate) - x))

        reference_counters = _compute_ngram_counter(refs[0], max_n)
        for ref in refs[1:]:
            reference_counters = reference_counters | _compute_ngram_counter(ref, max_n)

        candidate_counter = _compute_ngram_counter(candidate, max_n)

        clipped_counter = candidate_counter & reference_counters

        for ngram in clipped_counter:
            clipped_counts[len(ngram) - 1] += clipped_counter[ngram]

        for ngram in candidate_counter:  # TODO: no need to loop through the whole counter
            total_counts[len(ngram) - 1] += candidate_counter[ngram]

    if min(clipped_counts) == 0:
        return 0.0
    else:
        pn = clipped_counts / total_counts
        log_pn = weights * torch.log(pn)
        score = torch.exp(sum(log_pn))

        bp = math.exp(min(1 - refs_len / candidate_len, 0))

        return bp * score.item()

def calculate_bleu(data, src_field, trg_field, model, device, max_len = 50):
    
    trgs = []
    pred_trgs = []
    
    for datum in data:
        
        src = vars(datum)['src']
        trg = vars(datum)['trg']
        
        pred_trg, _ = translate_sentence(src, src_field, trg_field, model, device, max_len)
        
        #cut off <eos> token
        pred_trg = pred_trg[:-1]
        
        pred_trgs.append(pred_trg)
        trgs.append([trg])
        
    return bleu_score(pred_trgs, trgs)

# bleu_score = calculate_bleu(test_data, SRC, TRG, model, device)

# print(f'BLEU score = {bleu_score*100:.2f}')
