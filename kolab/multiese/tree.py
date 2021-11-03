from janome.tokenizer import Tokenizer
import sys

janome = Tokenizer()

OPTION = {
    #     '--random': True,
    #     '--single': False, # ひとつしか選ばない (DAはオフ)
    '--order': False,  # 順序も入れ替える
    #     '--short': False, # 短い類義語を選ぶ
    #     '--pyfirst': False, #Pythonを先に出力する (yk使用)
    #     '--change-subject': 0.0, # 助詞の「が」をランダムに「は」に変える
    #     '--drop': 0.0, # パラメータをドロップする
    #     '--partial': False, #不完全なコードでも出力する
}


class ノード(object):  # 抽象的なトップクラス

    def emit(self, out):
        pass

    def stringfy(self):
        out = []
        self.emit(out)
        return ''.join(out)

    def flatten(self, ns=None):
        if ns is None:
            ns = []
        ns.append(self)
        return ns

    def simplify(self):
        """シンプルにしてノードを返す
        """
        return self


class 字句(ノード):  # 抽象的な字句
    w: str

    def __init__(self, w):
        self.w = w

    def emit(self, out):
        # 類義語に置き換える処理を書けばよい
        out.append(self.w)

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {repr(self.w)}]"


class 系列(ノード):  # 系列
    ws: list  # 系列のリスト

    def __init__(self, *ws):
        self.ws = ws

    def emit(self, out):
        for w in self.ws:
            w.emit(out)

    def flatten(self, ns=None):
        if ns is None:
            ns = []
        for w in self.ws:
            w.flatten(ns)
        return ns

    def simplify(self):
        if len(self.ws) == 1:
            return self.ws[0]
        return self

    def __repr__(self):
        s = ' '.join(map(repr, self.ws))
        return f"[{self.__class__.__name__} {s}]"


class グループ(ノード):  # 外からみると、字句として扱えるが、中には系列が入っている
    node: str

    def __init__(self, node):
        self.node = node

    def emit(self, out):
        self.node.emit(out)

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {repr(self.node)}]"


class Choice(ノード):  # 系列が入っている字句として扱えるが、中には系列が入っている
    nodes: list

    def __init__(self, nodes):
        self.nodes = nodes

    def emit(self, out):
        pass  # がんばれ
        # nodes のどれかを選べばよい

    def __repr__(self):  # repr
        s = ' '.join(map(repr, self.nodes))
        return f"[{self.__class__.__name__} {s}]"


# アノテーション


class Annotation(ノード):  # 本来ならアノテーションごとに作った方がよい
    name: str
    nodes: list

    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

    def emit(self, out):
        pass  # がんばれ

    def __repr__(self):  # repr
        s = ' '.join(map(repr, self.nodes))
        return f"[{self.__class__.__name__} {self.name} {s}]"


class 型情報(ノード):  # 本来ならアノテーションごとに作った方がよい
    name: str  # 変数名
    desc: str  # 型情報

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def emit(self, out):
        pass  # がんばれ

    def __repr__(self):  # repr
        return f"[{self.__class__.__name__} {self.name} {self.desc}]"


def annotation(name: str, nodes):
    if name == 'type':
        if len(nodes) == 1:
            return 型情報(nodes[0].stringfy(), '')
        return 型情報(nodes[0].stringfy(), nodes[1].stringfy())
    return Annotation(name, nodes)


class 文(系列):
    def emit(self, out):
        # 変更するところだけ定義する
        for w in self.ws:
            w.emit(out)


class 文節(系列):
    pass


# 末端(字句)

class 名詞(字句):
    pass


class 助詞(字句):
    pass


class 助動詞(字句):
    pass


class 形容詞(字句):
    pass


class 連体詞(字句):
    pass


class 副詞(字句):
    pass


class 接続詞(字句):
    pass


class 動詞(字句):
    pass


class コード(字句):
    pass


class 記号(字句):
    pass


class 未定義(ノード):
    def emit(self, out):
        out.append(f'@{self.w}')


def parse(s: str) -> ノード:
    '''
    janome で解析した結果から、文オブジェクトを返す
    https://note.nkmk.me/python-janome-tutorial/
    '''
    buf_pos = []
    buf_phrase = []

    wakati = [token.surface for token in janome.tokenize(s)]   # 分かち書きのリスト
    # wakati = [token.base_form for token in janome.tokenize(s)]   # 基本形 (標準形) のリスト

    pos = [token.part_of_speech.split(',')[0]
           for token in janome.tokenize(s)]   # 品詞のリスト
    pos2 = [token.part_of_speech.split(',')[1] for token in janome.tokenize(s)]
    # pos3 = [token.part_of_speech.split(',')[2] for token in janome.tokenize(s)]

    # print('@@wakati', wakati)
    # print('@@pos   ', pos)
    # print('@@pos2  ', pos2)
    # print('@@pos3  ', pos3)

    for idx in range(len(wakati)):
        if pos[idx] == '名詞' or pos[idx] == '接頭詞':
            x = 名詞(wakati[idx])
            buf_pos.append(x)
            if OPTION['--order']:
                print('@@option_test')

        elif pos[idx] == '動詞':
            x = 動詞(wakati[idx])
            buf_pos.append(x)
            try:
                if pos[idx+1] == '名詞':
                    x = 文節(*buf_pos)
                    buf_phrase.append(x)
                    buf_pos = []
            except:
                pass

        elif pos[idx] == '助動詞':
            x = 助動詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '助詞':   # TODO: おそらく動詞+助詞をちゃんと処理しないと
            x = 助詞(wakati[idx])
            buf_pos.append(x)
            x = 文節(*buf_pos)
            buf_phrase.append(x)
            buf_pos = []

        elif pos[idx] == '副詞':   # 動詞を修飾
            x = 副詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '連体詞':   # 名詞を修飾 (TODO: 「その」「あの」など...「大きな」などとの区別)
            x = 連体詞(wakati[idx])
            buf_pos.append(x)
        elif pos[idx] == '形容詞':   # 副詞と連体詞は活用なし、形容詞は活用あり
            x = 形容詞(wakati[idx])
            buf_pos.append(x)

        elif pos[idx] == '接続詞':
            x = 接続詞(wakati[idx])
            buf_pos.append(x)
            x = 文節(*buf_pos)
            buf_phrase.append(x)
            buf_pos = []

        elif pos[idx] == '記号':
            if pos2[idx] == '空白' or pos2[idx] == '句点':
                pass
            elif pos2[idx] == '一般':   # 名詞で扱った方が良いかも？
                x = 記号(wakati[idx])
                buf_pos.append(x)
            elif pos2[idx] == '読点':
                if len(buf_pos) == 0:
                    pass
                else:
                    x = 記号(wakati[idx])
                    buf_pos.append(x)
                    x = 文節(*buf_pos)
                    buf_phrase.append(x)
                    buf_pos = []
            else:
                x = 未定義(wakati[idx])
                buf_pos.append(x)
                print('@@', wakati[idx], pos[idx], pos2[idx])
        else:
            x = 未定義(wakati[idx])
            buf_pos.append(x)
            print('@@', wakati[idx], pos[idx], pos2[idx])

    if buf_pos != []:
        x = 文節(*buf_pos)
        buf_phrase.append(x)

    s = 文(*buf_phrase)

    return s


def read_txt(input_filename):
    '''
    テキストファイルを1行ずつ読み込んで
    parse した結果をプリント
    '''
    with open(input_filename) as f:
        for line in f.readlines():
            s = parse(line.strip())
            print(s.stringfy())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            if filename.startswith('-'):
                if '=' not in filename:
                    filename += '=True'
                key, value = filename.split('=')
                OPTION[key] = int(
                    value) if value.isdigit() else value == 'True'
                continue

            try:
                read_txt(filename)
            except:
                pass
    else:
        # s = parse('データフレームdfを逆順にソートする')
        # s2 = parse('データフレームdfを逆順にソートして、df2とする')

        s = parse('隣の客はよく柿食う客だ')
        print(repr(s), s.stringfy())

        s = parse('その写真は美しい')
        s2 = parse('美しい写真を眺める').simplify()

        s = parse('大きな犬').simplify()

        print(repr(s), s.stringfy())
        print(repr(s2), s2.stringfy())
