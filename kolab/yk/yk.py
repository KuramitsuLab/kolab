from os import read
import sys
import pegtree as pg
import csv

from pegtree.optimizer import optimize

peg = pg.grammar('yk.tpeg')
parse = pg.generate(peg)

VAR_literal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
NAME_literal = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
VAL_literal = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

OPTION = {
    '--notConv': False,
    '--diff': False,
    '--reverse': False,
}

def replace_as_special_parameter(s, mapped, tag=None):   # mapped => {'df': '<A>'}
    if s in mapped:
        return mapped[s]

    if tag == 'Name':
        x = '<' + NAME_literal[len(mapped)] +'>' #辞書
    elif tag == 'Value':
        x = '<' + VAL_literal[len(mapped)] +'>' #辞書
    else:
        x = '<' + VAR_literal[len(mapped)] +'>' #辞書

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
    # print('@@', s, tag)
    if diff:
        if tag == 'Name':
            if s in doc:
                return replace_as_special_parameter(s, mapped, tag='Name')
            else:
                if s.startswith('.'):
                    s = '. ' + s[1:]
                return s
        if tag == 'Value':
            # print(f"@@val '{s[1:-1]}'")
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

def make(code, doc0, convert=convert_all, diff=False, reverse=False):
    # print('BEFORE', code, doc)
    mapped = {}
    doc = []
    flag = 0
    for tok in parse(doc0):
        s = str(tok)
        # TODO: この分岐の意味とflagの意味
        if tok.getTag() == 'Raw':
            q = f"'{s}'"
            q2 = f'"{s}"'
            if q in code:
                #print(f'`{s}` => {q}')
                doc.append(q)
                flag=1
                continue
            if q2 in code:
                #print(f'`{s}` => {q2}')
                doc.append(q2)
                flag=1
                continue
        doc.append(s)
    ws = [convert(tok, doc, mapped, diff) for tok in parse(code)]
    # print('@@ws', ws)
    code = ' '.join(ws)

    if reverse:
        reverse_stoken = {}
        if convert == convert_all:
            if diff:
                cnt = 1
                for k, v in mapped.items():
                    if v[1] in NAME_literal:
                        s_token = '<' + NAME_literal[len(mapped) - cnt] + '>'
                    else:
                        s_token = '<' + VAL_literal[len(mapped) - cnt] + '>'
                    mapped[k] = s_token
                    reverse_stoken[v] = s_token
                    cnt += 1
            else:
                cnt = 1
                for k, v in mapped.items():
                    s_token = '<' + VAR_literal[len(mapped) - cnt] + '>'
                    mapped[k] = s_token
                    reverse_stoken[v] = s_token
                    cnt += 1

        # print('@@rd', reverse_stoken)
        ws_rev = [reverse_stoken[tok] if tok in reverse_stoken else tok for tok in ws]
        code = ' '.join(ws_rev)

    # print('@@mp', mapped)
    ws = [mapped[tok] if tok in mapped else tok for tok in doc if tok.strip() != '']
    doc = ' '.join(ws)

    return code, doc

def read_tsv(input_filename, output_filename=None):
    with open(input_filename) as f:
        reader = csv.reader(f, delimiter='\t')
        if output_filename != None:
            writer = csv.writer(output_filename, delimiter='\t')

        for row in reader:
            code2 = None
            if OPTION['--notConv']:
                code, doc = make(row[0], row[1], convert=convert_nothing)
            elif OPTION['--diff'] and OPTION['--reverse']:
                code, doc = make(row[0], row[1], diff=True, reverse=False)
                code2, doc2 = make(row[0], row[1], diff=True, reverse=True)
            elif OPTION['--diff']:
                code, doc = make(row[0], row[1], diff=True, reverse=False)
            elif OPTION['--reverse']:
                code, doc = make(row[0], row[1], diff=False, reverse=False)
                code2, doc2 = make(row[0], row[1], diff=False, reverse=True)
            else:
                code, doc = make(row[0], row[1])
            
            if output_filename == None:
                print(code, doc)
                if code2 != None and code2 != code:
                    print(code2, doc2)
            else:
                writer.writerow([code, doc])
                if code2 != None and code2 != code:
                    writer.writerow([code2, doc2])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                if '=' not in filename:
                    filename += '=True'
                key, value = filename.split('=')
                OPTION[key] = int(value) if value.isdigit() else value == 'True'
                continue

            try:
                read_tsv(filename, sys.stdout)
            except:
                read_tsv(filename)

    else:
        pass
