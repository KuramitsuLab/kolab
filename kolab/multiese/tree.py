

class ノード(object):  # 抽象的なクラス
    pass

    def emit(self, out):
        pass

    def stringfy(self):
        out = []
        self.emit(out)
        return ''.join(out)


class 文(ノード):
    ws: list  # 文節のリスト

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            w.emit(out)


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
        # 類義語に置き換える処理を書けばよい
        out.append(self.w)


class 助詞(ノード):
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        out.append(self.w)


def parse(s: str):
    # Janome で解析し、文オブジェクトを返す
    # 偶数の
    # s = 文(文節(名詞('偶数'), 助詞('の')))
    return s


s = parse('偶数の')
print(s.stringfy())

# 吾輩を猫とする
