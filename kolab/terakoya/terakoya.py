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
                key, value = [s.strip() for s in line.split('=')]
                tokibi.update_synonyms(synonyms, key, value)
                continue
            if code is None:
                code = line
            else:
                desc.append(line)
        if code is not None:
            dataset.append((code, tuple(desc)))
    return dataset

条件 = tokibi.parse('[もし|]X[ならば]|X[とき|場合]|')
条件2 = tokibi.parse('[もし|]X[ならば]|Xの[とき|場合]|')

def emit(doc, code, file):
    if doc.endswith('かどうか'):
        print(f'{doc}\t{code}', file=file)
        tokibi.randomize()
        cond = doc[:-4]
        if cond.endswith('る') or cond.endswith('い') or cond.endswith('た'):
            doc = tokibi.choice(条件.apply({'X': doc[:-4]}).generate())
        else:
            doc = tokibi.choice(条件2.apply({'X': doc[:-4]}).generate())
        print(f'{doc}\tif {code}:', file=file)        
    else:
        print(f'{doc}\t{code}', file=file)

def write_tsv(datasetset, synonyms, file=sys.stdout):
    for code, desc in datasetset:
        for d in desc:
            try:
                docs = tokibi.parse(d, synonyms=synonyms).generate()
                for doc in docs:
                    emit(doc, code, file)
            except RuntimeError:
                pass

if __name__ == '__main__':
    if len(sys.argv) > 1:
        dataset=[]
        synonyms = {}
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                if '=' not in filename:
                    filename += '=True'
                key, value = filename.split('=')
                tokibi.OPTION[key] = int(value) if value.isdigit() else value == 'True'
                continue
            read_terakoya(filename, synonyms, dataset)
        write_tsv(dataset, synonyms)
        print(tokibi.OPTION)

