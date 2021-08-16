import sys

def count_utf8(line):
    """
    文字コードで解説とコードを見分けるいい加減な実装
    """
    a, u = 0, 0
    for c in line:
        if c == '#' and u == 0: #コメント
            break
        if ord(c) > 128:
            u+=1
        else:
            a+=1
    return u / (a+u)        

def read_file(filename):
    with open(filename) as f:
        docs = []
        codes = []
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0: continue
            uraito = count_utf8(line)
            if uraito < 0.05:
                codes.append(line)
            else:
                docs.append(line)
        docs = ''.join(docs).split('。')
        print(docs)  # 解説文(デバッグ用)
        print(codes) # コード（デバッグ用)
        return docs, codes

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            read_file(filename)
