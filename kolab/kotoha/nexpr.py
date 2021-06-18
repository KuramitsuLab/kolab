import random
from . import verb

EMPTY = tuple()

# オプション

OPTION = {
    'Simple': False,  # シンプルな表現を優先する
    'Block': False,  # Expressionに <e> </e> ブロックをつける
    'ReversePolish': True,  # 膠着語の場合はTrue
    'EnglishFirst': False,  # 英訳の精度を優先する
    'ShuffleSynonym': True,  # 同音異議語をシャッフルする
    'MultipleSentence': True,  # 複数行モード
    'ShuffleOrder': True,  # もし可能なら順序も入れ替える
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


def shuffle(x, y):
    if OPTION['ShuffleSynonym']:
        return x if random.random() < 0.6 else y
    return x

# NExpr

class NExpr(object):
    def apply(self, mapped):
        return self

def apply(w, mapped):
    if isinstance(w, NExpr):
        return w.apply(mapped)
    return w

def emit(w, mode = verb._U, suffix='', buffer=None):
    if isinstance(w, NExpr):
        return w.emit(mode, suffix, buffer)
    return str(w)

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

    def emit(self, mode, prefix, buffer=None):
        if prefix in ['結果', '値']:
            return self.value
        return f'{prefix} {self.value}'


class NPred(NExpr):
    prefix: tuple
    verb: str
    ret: str

    def __init__(self, verb, ret, prefix=EMPTY):
        self.verb = verb
        self.ret = ret
        self.prefix = prefix

    def __str__(self):
        if self.ret == '':
            return str(self.verb)
        return f'({self.verb} : {self.ret})'

    def emit(self, mode, suffix, buffer=None):
        ss = []
        for e in self.prefix:
            ss.append(emit(verb._U, '', buffer))
        tok = alt(self.verb)
        if suffix == '':
            suffix = alt(self.ret)
        if suffix != '':
            mode |= verb.NOUN
        ss.append(emit(tok, mode, suffix, buffer))
        return ''.join(ss)

class NChunk(NExpr):
    pieces: tuple

    def __init__(self, *pieces):
        self.pieces = tuple(pieces)

    def apply(self, mapped):
        pieces = [e.apply(mapped) for e in self.pieces]
        return NChunk(self.suffix, *pieces)

    def __str__(self):
        ss = []
        for p in self.pieces:
            ss.append(str(p))
        ss.append(self.suffix)
        return '{{ ' + ''.join(ss) + ' }}'

    def emit(self, typefix, buffer=None):
        ss = []
        for p in self.pieces:
            ss.append(p.emit(typefix, buffer))
        return ''.join(ss)

class NContext(NExpr):
    inner: NExpr
    mode: int
    suffix: str

    def __init__(self, inner, mode, suffix):
        self.suffix = inner
        self.mode = mode
        self.suffix = suffix

    def __str__(self):
        if self.ret == '':
            return str(self.verb)
        return f'({self.verb} : {self.ret})'

    def emit(self, mode=0, suffix='', buffer=None):
        return emit(self.inner, self.mode|mode, suffix, buffer)

class NParam(NExpr):
    # symbol: str
    index: int
    typefix: str
    bound: NExpr

    def __init__(self, index, typefix=''):
        self.index = index
        self.typefix = typefix
        self.bound = bound

    def apply(self, mapped):
        if self.index in mapped:
            bound = mapped[self.index]
            return NContext(bound, self.mode, self.suffix)
        return self

    def __str__(self):
        return ALPHA[self.index]


class NTuple(NExpr):
    elements: tuple

    def __init__(self, *elements):
        self.elements = tuple(toNExpr(e) for e in elements)

    def asType(self, typefix):
        return NTuple(*[c.asType(typefix) for c in self.elements])

    def apply(self, mapped):
        return NTuple(*[c.apply(mapped) for c in self.elements])

    def __str__(self):
        return '(' + ','.join(map(str, self.elements)) + ')'

    def emit(self, typefix, buffer=None):
        return '(' + ','.join(map(lambda e: e.emit(typefix, buffer), self.elements)) + ')'


class NPhrase(NExpr):
    pieces: tuple
    options: tuple
    ret: str  # 返り値の種類

    def __init__(self, *pieces):
        self.pieces = [toNExpr(p) for p in pieces]
        self.options = EMPTY
        self.ret = None

    def asType(self, ret):
        self.ret = ret
        return self

    def apply(self, mapped):
        pred = NPhrase(*[e.apply(mapped) for e in self.pieces])
        pred.options = mapped.get('options', EMPTY)
        pred.ret = self.ret
        return pred

    def __str__(self):
        ss = []
        for p in self.pieces:
            ss.append(str(p))
        return ' '.join(ss)

    def emit(self, typefix, buffer=None):
        ss = []
        if OPTION['Block']:
            ss.append('<e>')
        if len(self.options) > 2 and OPTION['ShuffleOrder']:
            os = list(self.options)
            random.shuffle(os)
            self.options = tuple(os)

        for p in self.options:
            if buffer is None:
                ss.append(p.emit(shuffle('T、', 'A、')))
            else:
                buffer.append(p.emit(EOS))

        for p in self.pieces:
            ss.append(p.emit(typefix, buffer))

        if OPTION['Block']:
            if buffer is not None:
                ss.extend(buffer)
                buffer.clear()
            ss.append('</e>')
        return ' '.join(ss)
