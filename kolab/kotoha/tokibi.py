import pegtree as pg
from pegtree.visitor import ParseTreeVisitor
import random
# from . import verb
import verb

# 犬と/猫が/等しい#not

EMPTY = tuple()

# オプション

OPTION = {
    'Simple': False,  # シンプルな表現を優先する
    'Block': False,  # Expressionに <e> </e> ブロックをつける
    'EnglishFirst': False,  # 英訳の精度を優先する
    'ShuffleSynonym': True,  # 同音異議語をシャッフルする
    'MultipleSentence': False,  # 複数行モード
    'ShuffleOrder': True,  # 順序も入れ替える
    'Verbose': True,  # デバッグ出力あり
}

# randomize

RandomIndex = 0


def randomize():
    global RandomIndex
    if OPTION['ShuffleSynonym']:
        RandomIndex = random.randint(1, 1789)


def random_index(arraysize: int, seed):
    if OPTION['ShuffleSynonym']:
        return (RandomIndex + seed) % arraysize
    return 0


def alt(s: str):
    if '|' in s:
        ss = s.split('|')
        if OPTION['EnglishFirst']:
            return ss[-1]  # 最後が英語
        return ss[random_index(len(ss), len(s))]
    return s


def choice(ss: list):
    return ss[random_index(len(ss), 17)]


def conjugate(w, mode=0, vpos=None):
    suffix = ''
    if mode & verb.CASE == verb.CASE:
        mode = (mode & ~verb.CASE) | verb.NOUN
        suffix = alt('とき、|場合、|際、')
    if mode & verb.THEN == verb.THEN:
        if RandomIndex % 2 != 0:
            mode = (mode & ~verb.THEN) | verb._I
        suffix = '、'
    return verb.conjugate(w, mode, vpos) + suffix

# NExpr


class NExpr(object):
    def apply(self, mapped):
        return self


def apply_nparam(w, mapped):
    if isinstance(w, NExpr):
        return w.apply(mapped)
    return w


def emit(w, mode=0, alias='', buffer=None):
    if isinstance(w, NExpr):
        return w.emit(mode, alias, buffer)
    return alt(str(w))


def longer(s, s2):
    return s if len(s) > len(s2) else s2


class NLiteral(NExpr):
    value: str
    ret: str

    def __init__(self, value: str, ret=None):
        self.value = value
        if ret is None:
            if value.startswith('"') or value.startswith("'"):
                ret = 'str'
            elif value.isdigit():
                ret = 'int'
        self.ret = ret

    def __str__(self):
        return self.value

    def emit(self, mode=0, alias='', buffer=None):
        if alias in ['', '結果', '値']:
            return self.value
        return f'{alias} {self.value}'


class NPred(NExpr):
    verb: str
    mode: int
    cat: str

    def __init__(self, verb, vpos=None, mode=0, cat=''):
        self.verb = verb
        self.vpos = vpos
        self.mode = mode
        self.cat = cat

    def asType(self, ret, cat):
        self.cat = cat
        return self

    def __repr__(self):
        if self.cat == '':
            return f'{{{str(self.verb)}}}'
        return f'({self.verb} -> {self.cat})'

    def emit(self, mode=0, alias='', buffer=None):
        ss = []
        tok = alt(self.verb)
        mode |= self.mode
        if mode & verb.NOUN == verb.NOUN:
            alias = longer(alias, alt(self.cat))
            if alias == '':
                alias = '結果'
        else:
            alias = ''
        #print(tok, mode, '@', suffix)
        ss.append(conjugate(tok, mode, self.vpos)+alias)
        return ''.join(ss)


class NChunk(NExpr):
    pieces: tuple

    def __init__(self, *pieces):
        self.pieces = tuple(pieces)

    def apply(self, mapped):
        pieces = [apply_nparam(e, mapped) for e in self.pieces]
        return NChunk(*pieces)

    def __repr__(self):
        ss = []
        for p in self.pieces:
            ss.append(str(p))
        return ''.join(ss)

    def emit(self, mode=0, suffix='', buffer=None):
        ss = []
        for p in self.pieces[:-1]:
            ss.append(emit(p))
        ss.append(emit(self.pieces[-1], mode, suffix, buffer))
        return ''.join(ss)


ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def retype(name: str):
    if name[-1].isdigit():
        return retype(name[:-1])
    return name


class NContext(NExpr):
    inner: NExpr
    mode: int
    alias: str

    def __init__(self, inner, mode=0, alias=''):
        self.inner = inner
        self.mode = mode
        self.alias = alias

    def __repr__(self):
        if self.alias == '':
            return str(self.inner)
        return f'{self.inner}({self.alias})'

    def emit(self, mode=0, alias='', buffer=None):
        return self.inner.emit(self.mode | mode, longer(alias, self.alias), buffer)


class NParam(NExpr):
    symbol: str
    index: int
    ret: str
    cat: str

    def __init__(self, index, ret):
        self.index = index
        self.symbol = ret
        self.ret = retype(ret)
        self.cat = ''

    def apply(self, mapped):
        if self.index in mapped:
            bound = mapped[self.index]
            return NContext(bound, verb.NOUN, self.cat)
        return self

    def __repr__(self):
        return ALPHA[self.index]

    def emit(self, mode=0, suffix='', buffer=None):
        return alt(longer(self.cat, self.ret))


class NTuple(NExpr):
    elements: tuple
    ret: str  # 返り値の種類
    cat: str

    def __init__(self, *elements):
        self.elements = tuple(elements)
        self.ret = 'tuple'

    def apply(self, mapped):
        return NTuple(*[apply_nparam(c, mapped) for c in self.elements])

    def __repr__(self):
        return '(' + ','.join(map(str, self.elements)) + ')'

    def emit(self, mode=0, alias='', buffer=None):
        return '(' + ','.join(map(lambda e: emit(e, 0, '', None), self.elements)) + ')'


class NChoice(NExpr):
    elements: tuple
    ret: str  # 返り値の種類
    cat: str

    def __init__(self, *elements):
        self.elements = tuple(elements)

    def asType(self, ret, cat):
        for e in self.elements:
            if isinstance(e, NExpr):
                e.asType(ret, cat)
        return self

    def apply(self, mapped):
        return NChoice(*[apply_nparam(c, mapped) for c in self.elements])

    def __repr__(self):
        return ' | '.join(map(str, self.elements))

    def emit(self, mode=0, suffix='', buffer=None):
        return choice(self.elements).emit(mode, suffix, buffer)


class NPhrase(NExpr):
    pieces: tuple
    options: tuple
    ret: str  # 返り値の種類
    cat: str

    def __init__(self, *pieces):
        self.pieces = tuple(NChunk(*c) if isinstance(c, tuple) else c for c in pieces) 
        self.options = EMPTY
        self.ret = ''
        self.cat = ''

    def asType(self, ret, cat):
        self.pieces[-1].asType(ret, cat)
        self.ret = ret
        self.cat = cat
        return self

    def apply(self, mapped):
        pred = NPhrase(*[apply_nparam(e, mapped) for e in self.pieces])
        pred.options = mapped.get('options', EMPTY)
        return pred.asType(self.ret, self.cat)

    def __repr__(self):
        ss = []
        for p in self.pieces:
            ss.append(str(p))
        return ' '.join(ss)

    def emit(self, mode=0, alias='', buffer=None):
        ss = []
        options = self.options
        params = self.pieces[:-1]
        if OPTION['ShuffleOrder']:
            if len(options) >= 2:
                options = list(options)
                random.shuffle(options)
            if len(params) >= 2:
                params = list(params)
                random.shuffle(params)

        for p in options:
            if buffer is None:
                ss.append(emit(p, verb.THEN))
            else:
                buffer.append(emit(p))

        alias = longer(alias, alt(self.cat))
        for p in params:
            ss.append(emit(p))
        #print(type(self.pieces[-1]), self.pieces)
        ss.append(emit(self.pieces[-1], mode, alias, buffer))

        return ' '.join(ss)


##
peg = pg.grammar('tokibi.tpeg')
tokibi_parser = pg.generate(peg)


class TokibiReader(ParseTreeVisitor):

    def __init__(self, synonyms=None):
        ParseTreeVisitor.__init__(self)
        self.indexes = {}
        self.synonyms = {} if synonyms is None else synonyms

    def parse(self, s):
        tree = tokibi_parser(s)
        self.indexes = {}
        nexpr = self.visit(tree)
        return nexpr, self.indexes

    def acceptNChoice(self, tree):
        ss = [self.visit(t) for t in tree]
        if len(ss) == 1:
            return ss[0]
        return NChoice(*ss)

    def acceptNPhrase(self, tree):
        ss = [self.visit(t) for t in tree]
        ret = ''
        cat = ''
        if isinstance(ss[-1], str):
            pred = ss[-1]
            if pred.endswith('かどうか'):
                pred = pred[:-4]
                ret = 'bool'
                cat = 'かどうか'
            w, vpos, mode = verb.parse(pred)
            #print(w, vpos, mode)
            if w in self.synonyms:
                w = self.synonyms[w]
                vpos = None
            if cat == '':
                cat = self.synonyms.get(ret, '')
            ss[-1] = pred = NPred(w, vpos, mode, cat)
        #print('@@@', ss)
        ne = NPhrase(*ss)
        ne.ret = ret
        return ne

    def acceptNType(self, tree):
        ne = self.visit(tree[0])
        ret = str(tree[1])
        cat = str(tree[2]) if len(tree) == 3 else self.synonyms.get(ret, '')
        if isinstance(ne, NPhrase):
            ne.ret = ret
            ne.cat = cat
        if isinstance(ne, NChoice):
            for e in ne.elements:
                e.ret = ret
                e.cat = cat
        return ne

    def acceptNChunk(self, tree):
        ss = [self.visit(t) for t in tree]
        if len(ss) == 1:
            return ss[0]
        return NChunk(*ss)

    def acceptNVar(self, tree):
        s = str(tree)
        if s not in self.indexes:
            self.indexes[s] = len(self.indexes)
        return NParam(self.indexes[s], s)

    def acceptNMode(self, tree):
        param = self.visit(tree[0])
        param.cat = self.visit(tree[1])
        return param

    def acceptNAlt(self, tree):
        ss = [str(t) for t in tree]
        if len(ss) == 1:
            if ss[0] in self.synonyms:
                return self.synonyms[ss[0]]
            return ss[0]+'|'
        return '|'.join(ss)

    def acceptNTuple(self, tree):
        ss = [str(t) for t in tree]
        return NTuple(*ss)

    def acceptNLiteral(self, tree):
        symbol = str(tree)
        return NLiteral(symbol)

    def acceptNPiece(self, tree):
        w = str(tree)
        if w in self.synonyms:
            w = self.synonyms[w]
        return w


tokibi_reader = TokibiReader()


def parse(s):
    randomize()
    nexpr = tokibi_reader.parse(s)
    #print(nexpr, nexpr.emit())
    return nexpr


if __name__ == '__main__':
    e = parse('Aを/調べる')
    e2 = parse('[猫|ねこ]が/[虎|トラ]と/等しくないかどうか')
    e = e.apply({0: e2})
    print(e.emit())

    #parse('Aと/B(子犬)を/順に/1つずつ/表示する | Aを/Bに/表示する ->x(結果)')
    #parse('{xの各要素に/functionを/適用して}フィルタする -> list')
    # parse('dictの/key(エントリ) -> x')
    # parse('{xのyから/始まる}順序数列')
    # parse('望遠鏡で/{泳ぐ}子犬を/見た')
    # parse('{望遠鏡で/{泳ぐ}子犬を/見たとき}、{少し/{新しい}ことを/考えた}')
    # parse('x, y, zの各要素のタプル列 -> int')
