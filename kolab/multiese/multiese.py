import sys
import argparse
from parser import multiese_parser


def read_multiese_file(filename: str, pairs: list = None):
    if pairs is None:
        pairs = []  # [('日本語', 'コード') .. ] こういう順番で入ります
    with open(filename) as f:
        code = None  # コード
        sentences = []  # 自然言語文
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue  # #で始まる行はスキップ
            if line == '':
                if code is not None:  # もしコード が nullなら
                    for sentence in sentences:
                        pairs.append((sentence, code))
                code = None
                sentences = []  # 自然言語文
                continue
            line = line.split('#')[0]  # #以降はコメントとして捨てる
            # if code is None and ord(line[0])>127 and '=' in line:
            #     key, value = [s.strip() for s in line.split('=')]
            #     tokibi.update_synonyms(synonyms, key, value)
            #     continue
            if code is None:
                code = line
            else:
                sentences.append(line)
        if code is not None:
            for sentence in sentences:
                pairs.append((sentence, code))
    return pairs


def write_multiese_tsv(pairs, file=sys.stdout):
    for sentence, code in pairs:
        ss = multiese_parser(sentence)
        sentence = ss
        # sentence = ss.emit()
        if args.pyfirst:
            print(code, sentence, sep='\t', file=file)
        else:
            print(sentence, code, sep='\t', file=file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Multiese')
    parser.add_argument('files', nargs='+', help='files')
    parser.add_argument('--pyfirst', action='store_true')
    #parser.add_argument('--files', nargs='*')
    args = parser.parse_args()
    options = vars(args)
    print(options)
    for filename in args.files:
        pairs = []
        read_multiese_file(filename, pairs)
    write_multiese_tsv(pairs)


'''
import tokibi
from expression import *

OPTIONS = ('bool')

def read_terakoya(filename, synonyms, dataset=None):
    if dataset is None:
        dataset = []
    with open(filename) as f:
        code = None
        options = OPTIONS
        desc = []
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            if line == '':
                if code is not None:
                    dataset.append((code, tuple(desc), options))
                code = None
                options = OPTIONS
                desc = []
                continue
            line = line.split('#')[0]
            if code is None and ord(line[0])>127 and '=' in line:
                key, value = [s.strip() for s in line.split('=')]
                tokibi.update_synonyms(synonyms, key, value)
                continue
            if code is None:
                lines = line.split('@')
                code = lines[0]
                options = tuple(s.strip() for s in lines[1:])
            else:
                desc.append(line)
        if code is not None:
            dataset.append((code, tuple(desc), options))
    return dataset

def emit_tsv(doc, code, file):
    if tokibi.OPTION['--pyfirst']:
        print(f'{code}\t{doc}', file=file)
    else:
        print(f'{doc}\t{code}', file=file)

条件 = tokibi.parse('[もし|]X[ならば]|X[とき|場合]|')
条件2 = tokibi.parse('[もし|]X[ならば]|Xの[とき|場合]|')

def emit(code, docs, buffers, options):
    for doc in docs:
        if doc.endswith('かどうか'):
            tokibi.randomize()
            cond = doc[:-4]
            buffers.append((cond+tokibi.alt('かどうか|か否か|か|か'), code))
            if cond.endswith('る') or cond.endswith('い') or cond.endswith('た'):
                doc = tokibi.choice(条件.apply({'X': doc[:-4]}).generate())
            else:
                doc = tokibi.choice(条件2.apply({'X': doc[:-4]}).generate())
            buffers.append((doc, f'if {code}:'))
        else:
            buffers.append((doc, code))
    
def dispatch_emit(code, docs, buffers, options):
    if 'option' not in options:
        # @option は出力しない
        emit(code, docs, buffers, options)
    if len(options) > 0:
        symbols = globals()
        for option in options:
            local_options = option.split(':')
            option = local_options[0]
            fname = f'emit_{option}'
            if fname in symbols:
                app = symbols[fname]
                local_buffers = []
                is_extendable = app(code, docs, local_buffers, tuple(local_options[1:]) + options)
                buffers.extend(local_buffers)
                if is_extendable:
                    docs.extend([f'{x[1]}#{x[0]}' for x in local_buffers])
            else:
                print(f'undefined {option}')

def write_tsv(datasetset, synonyms, file=sys.stdout):
    for code, desc, options in datasetset:
        buffers = []
        for d in desc:
            try:
                exp, mcode, _ = tokibi.parse2(d, code, synonyms=synonyms)
                docs = exp.generate()
                dispatch_emit(mcode, docs, buffers, options)
            except RuntimeError:
                pass
        if tokibi.OPTION['--pyfirst']:
            for doc,code in buffers:
                print(f'{code}\t{doc}', file=file)
        else:
            for doc,code in buffers:
                print(f'{doc}\t{code}', file=file)
  

def parse_value(s):
    if s.isdecimal():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            return s == 'True'
'''
