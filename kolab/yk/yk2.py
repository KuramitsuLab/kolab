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
parser.add_argument('--both', action='store_true')      # shuffle ありとなしを両方追加
parser.add_argument('--files', nargs='*')               # 入力ファイルを与える

args = parser.parse_args()

token_idx = list(range(1, 7))

def replace_as_special_parameter(s, mapped, token_idx=token_idx, tag=None):   # mapped => {'df': '<A>'}
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

def convert_nothing(tok, doc, mapped, token_idx, diff):
    s = str(tok)
    if s == ';':  # ; だけはセミコロンに変える
        return '<sep>'
    return s

def convert_all(tok, doc, mapped, token_idx, diff):
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
                    return replace_as_special_parameter(s, mapped, token_idx, tag='Name')
            else:
                if s.startswith('.'):
                    s = '. ' + s[1:]
                return s
        if tag == 'Value':
            if s in doc:
                return replace_as_special_parameter(s, mapped, token_idx, tag='Value')
            s_q1 = f"'{s[1:-1]}'"
            if s_q1 in doc:
                return replace_as_special_parameter(s_q1, mapped, token_idx, tag='Value')
            s_q2 = f'"{s[1:-1]}"'
            if s_q2 in doc:
                return replace_as_special_parameter(s_q2, mapped, token_idx, tag='Value')
    else:
        if tag == 'Name':
            if s in doc:
                return replace_as_special_parameter(s, mapped, token_idx)
            else:
                if s.startswith('.'):
                    s = '. ' + s[1:]
                return s
        if tag == 'Value':
            if s in doc:
                return replace_as_special_parameter(s, mapped, token_idx)
            s_q1 = f"'{s[1:-1]}'"
            if s_q1 in doc:
                return replace_as_special_parameter(s_q1, mapped, token_idx)
            s_q2 = f'"{s[1:-1]}"'
            if s_q2 in doc:
                return replace_as_special_parameter(s_q2, mapped, token_idx)
    return convert_nothing(tok, doc, mapped, token_idx, diff)

def make(code, doc0, convert=convert_all, token_idx=token_idx, diff=False):
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

    ws = [convert(tok, doc, mapped, token_idx, diff) for tok in parse(code)]
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
            code0 = None
            if args.both:
                token_idx0 = list(range(1, 7))
                code0, doc0 = make(row[0], row[1], convert=convert_all , token_idx=token_idx0, diff=args.diff)

            if args.shuffle or args.both:
                random.shuffle(token_idx)

            if args.notConv:
                code, doc = make(row[0], row[1], convert=convert_nothing , token_idx=token_idx, diff=args.diff)
            else:
                code, doc = make(row[0], row[1], convert=convert_all, token_idx=token_idx, diff=args.diff)
            
            if output_filename == None:
                print(code, doc)
                if code0 != None and code0 != code:
                    print(code0, doc0)
            else:
                writer.writerow([code, doc])
                if code0 != None and code0 != code:
                    writer.writerow([code0, doc0])

if __name__ == '__main__':
    if args.files != None:
        for filename in args.files:
            try:
                read_tsv(filename, sys.stdout)
            except:
                read_tsv(filename)
    else:
        pass
