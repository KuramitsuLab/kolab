

class ノード(object):
    pass

    def emit(self, out):
        pass

    def stringfy(self):
        out = []
        self.emit(out)
        return ''.join(out)


class 文節(ノード):
    ws: list

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            w.emit(out)


class 名詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)


class 助詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)


# 偶数の
chunk = 文節(名詞('偶数'), 助詞('の'))
print(chunk.stringfy())
