import sys
import tokibi

def read_terakoya(filename, synonyms, dataset=None):
    if dataset is None:
        dataset = []
    with open(filename) as f:
        code = None
        desc = []
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#'):
                continue
            if line == '':
                if code is not None:
                    dataset.append((code, tuple(desc)))
                code = None
                desc = []
                continue
            if code is None and ord(line[0])>127 and '=' in line:
                key, value = [s.strip() for s in line.split('#')[0].split('=')]
                tokibi.update_synonyms(synonyms, key, value)
                continue
            if code is None:
                code = line
            else:
                desc.append(line)
        if code is not None:
            dataset.append((code, tuple(desc)))
    return dataset

def emit_tsv(doc, code, file):
    if tokibi.OPTION['--pyfirst']:
        print(f'{code}\t{doc}', file=file)
    else:
        print(f'{doc}\t{code}', file=file)

条件 = tokibi.parse('[もし|]X[ならば]|X[とき|場合]|')
条件2 = tokibi.parse('[もし|]X[ならば]|Xの[とき|場合]|')

def emit(doc, code, file):
    if doc.endswith('かどうか'):
        tokibi.randomize()
        cond = doc[:-4]
        emit_tsv(cond+tokibi.alt('かどうか|か否か|か|か'), code, file)
        if cond.endswith('る') or cond.endswith('い') or cond.endswith('た'):
            doc = tokibi.choice(条件.apply({'X': doc[:-4]}).generate())
        else:
            doc = tokibi.choice(条件2.apply({'X': doc[:-4]}).generate())
        emit_tsv(doc, f'if {code}:', file)
    else:
        emit_tsv(doc, code, file)
    
def write_tsv(datasetset, synonyms, file=sys.stdout):
    for code, desc in datasetset:
        for d in desc:
            try:
                docs = tokibi.parse(d, synonyms=synonyms).generate()
                for doc in docs:
                    emit(doc, code, file)
            except RuntimeError:
                pass

def parse_value(s):
    if s.isdecimal():
        return int(s)
    else:
        try:
            return float(s)
        except ValueError:
            return s == 'True'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dataset=[]
        synonyms = {}
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                if '=' not in filename:
                    filename += '=True'
                key, value = filename.split('=')
                tokibi.OPTION[key] = parse_value(value)
                continue
            read_terakoya(filename, synonyms, dataset)
        write_tsv(dataset, synonyms)

