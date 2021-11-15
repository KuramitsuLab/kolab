from os import read
import random
import sys
import pegtree as pg
import argparse
import csv

from pegtree.optimizer import optimize

peg = pg.grammar('yk.tpeg')
parse = pg.generate(peg)

parser = argparse.ArgumentParser(description='yk for Parameter Handling')

parser.add_argument('--notConv', action='store_true')   # Python　のトークナイズのみ
parser.add_argument('--diff', action='store_true')      # 変数名 (name) とリテラル (val) に異なるものを付与
parser.add_argument('--shuffle', action='store_true')   # 特殊トークンをランダムに付与 (順序を考慮しない)
parser.add_argument('--files', nargs='*')               # 入力ファイルを与える

args = parser.parse_args()

token_idx = list(range(1, 10))

def replace_as_special_parameter(s, mapped, tag=None):   # mapped => {'df': '<A>'}
    if s in mapped:
        return mapped[s]

    if tag == 'Name':
        x = f'<name{token_idx[len(mapped)]}>'
    elif tag == 'Value':
        x = f'<val{token_idx[len(mapped)]}>'
    else:
        x = f'<var{token_idx[len(mapped)]}>'

    mapped[s] = x

    return x

def convert_nothing(tok, doc, mapped, diff):
    s = str(tok)
    if s == ';':  # ; だけはセミコロンに変える
        return '<sep>'
    return s

def convert_all(tok, doc, mapped, diff):
    tag = tok.getTag()
    s = str(tok)

    if diff:
        if tag == 'Name':
            
            if s in doc:
                in_idx = [i for i, x in enumerate(doc) if x == s]
                flag = 0
                for idx in in_idx:
                    try:
                        if '軸' in doc[idx+1] or '座標' in doc[idx+1]:
                            flag += 1
                    except:
                        pass
                if len(in_idx) == flag:
                    return s
                else:
                    return replace_as_special_parameter(s, mapped, tag='Name')
            else:
                if s.startswith('.'):
                    s = '. ' + s[1:]
                return s
        if tag == 'Value':
            if s in doc:
                return replace_as_special_parameter(s, mapped, tag='Value')
            s_q1 = f"'{s[1:-1]}'"
            if s_q1 in doc:
                return replace_as_special_parameter(s_q1, mapped, tag='Value')
            s_q2 = f'"{s[1:-1]}"'
            if s_q2 in doc:
                return replace_as_special_parameter(s_q2, mapped, tag='Value')
    else:
        if tag == 'Name':
            if s in doc:
                return replace_as_special_parameter(s, mapped)
            else:
                if s.startswith('.'):
                    s = '. ' + s[1:]
                return s
        if tag == 'Value':
            if s in doc:
                return replace_as_special_parameter(s, mapped)
            s_q1 = f"'{s[1:-1]}'"
            if s_q1 in doc:
                return replace_as_special_parameter(s_q1, mapped)
            s_q2 = f'"{s[1:-1]}"'
            if s_q2 in doc:
                return replace_as_special_parameter(s_q2, mapped)
    return convert_nothing(tok, doc, mapped, diff)

def make(code, doc0, convert=convert_all, diff=False):
    mapped = {}
    doc = []
    for tok in parse(doc0):
        s = str(tok)
        if tok.getTag() == 'Raw':
            q = f"'{s}'"
            q2 = f'"{s}"'
            if q in code:
                doc.append(q)
                continue
            if q2 in code:
                doc.append(q2)
                continue
        doc.append(s)

    ws = [convert(tok, doc, mapped, diff) for tok in parse(code)]
    code = ' '.join(ws)

    ws = []
    for idx, tok in enumerate(doc):
        if tok.strip() != '':
            if tok in mapped:
                try:
                    if '軸' in doc[idx+1] and '座標' in doc[idx+1]:
                        ws.append(tok)
                    else:
                        ws.append(mapped[tok])
                except:
                    ws.append(mapped[tok])
            else:
                ws.append(tok)
    doc = ' '.join(ws)

    return code, doc

def read_tsv(input_filename, output_filename=None):
    with open(input_filename) as f:
        reader = csv.reader(f, delimiter='\t')
        if output_filename != None:
            writer = csv.writer(output_filename, delimiter='\t')

        for row in reader:
            if args.shuffle:
                random.shuffle(token_idx)
            if args.notConv:
                code, doc = make(row[0], row[1], convert=convert_nothing , diff=args.diff)
            else:
                code, doc = make(row[0], row[1], convert=convert_all, diff=args.diff)
            
            if output_filename == None:
                print(code, doc)
            else:
                writer.writerow([code, doc])

if __name__ == '__main__':
    if args.files != None:
        for filename in args.files:
            try:
                read_tsv(filename, sys.stdout)
            except:
                read_tsv(filename)
    else:
        pass
