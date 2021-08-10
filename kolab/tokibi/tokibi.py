import sys
import pegtree as pg
from pegtree.visitor import ParseTreeVisitor
import random
# from . import verb
import verb

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
    else:
        RandomIndex = 0


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
        if RandomIndex % 2 != 0:
            mode = (mode & ~verb.CASE) | verb.NOUN
            suffix = alt('とき、|場合、|際、')
        else:
            suffix = '、'
    if mode & verb.THEN == verb.THEN:
        if RandomIndex % 2 != 0:
            mode = (mode & ~verb.THEN) | verb._I
        suffix = '、'
    return verb.conjugate(w, mode, vpos) + suffix

# NExpr

def identity(e):
    return e

class NExpr(object):
    subs: tuple
    def __init__(self, subs=EMPTY):
        self.subs = tuple(NWord(s) if isinstance(s, str) else s for s in subs)

    def apply(self, dict_or_func=identity):
        if len(self.subs) > 0:
            (e.apply(dict_or_func) for e in self.subs)
        return self
    
    def generate(self):
        ss = []
        c = 0
        while c < 3:
            randomize()
            buffers = []
            self.emit(buffers)
            s = ''.join(buffers)
            if s not in ss:
                ss.append(s)
            else:
                c += 1
        return ss

class NWord(NExpr):
    w: str

    def __init__(self, w):
        NExpr.__init__(self)
        self.w = str(w)

    def __repr__(self):
        if '|' in self.w:
            return '[' + self.w + ']'
        return self.w
    
    def apply(self, dict_or_func=identity):
        if not isinstance(dict_or_func, dict):
            return dict_or_func(self)
        return self

    def emit(self, buffers):
        buffers.append(alt(self.w))


class NVerb(NExpr):
    w: str
    vpos: str
    mode: int

    def __init__(self, w, vpos, mode=0):
        NExpr.__init__(self)
        self.w = str(w)
        self.vpos = vpos
        self.mode = mode

    def __repr__(self):
        return verb.conjugate(self.w, self.mode, self.vpos)
    
    def apply(self, dict_or_func=identity):
        if not isinstance(dict_or_func, dict):
            return dict_or_func(self)
        return self

    def emit(self, buffers):
        buffers.append(verb.conjugate(self.w, self.mode, self.vpos))


class NChoice(NExpr):
    def __init__(self, *subs):
        NExpr.__init__(self, subs)

    def __repr__(self):
        ss = []
        for p in self.subs:
            ss.append(repr(p))
        return ' | '.join(ss)

    def apply(self, dict_or_func=identity):
        return NChoice(*(e.apply(dict_or_func) for e in self.subs))

    def emit(self, buffers):
        choice(self.subs).emit(buffers)


class NPhrase(NExpr):
    def __init__(self, *subs):
        NExpr.__init__(self, subs)

    def __repr__(self):
        ss = []
        for p in self.subs:
            ss.append(grouping(p))
        return ' '.join(ss)

    def apply(self, dict_or_func=identity):
        return NPhrase(*(e.apply(dict_or_func) for e in self.subs))

    def emit(self, buffers):
        for p in self.subs:
            p.emit(buffers)

def grouping(e):
    if isinstance(e, NPhrase):
        return '{' + repr(e) + '}'
    return repr(e)

class NOrdered(NExpr):
    def __init__(self, *subs):
        NExpr.__init__(self, subs)

    def __repr__(self):
        ss = []
        for p in self.subs:
            ss.append(grouping(p))
        return '/'.join(ss)

    def apply(self, dict_or_func=identity):
        return NOrdered(*(e.apply(dict_or_func) for e in self.subs))

    def emit(self, buffers):
        subs = list(self.subs)
        if OPTION['ShuffleOrder']:
            random.shuffle(subs)
        for p in subs:
            p.emit(buffers)


class NClause(NExpr):

    def __init__(self, verb, noun):
        NExpr.__init__(self, (verb,noun))

    def __repr__(self):
        return grouping(self.subs[0]) + grouping(self.subs[1])

    def apply(self, dict_or_func=identity):
        return NClause(*(e.apply(dict_or_func) for e in self.subs))

    def emit(self, buffers):
        verb = self.subs[0]
        noun = self.subs[1]
        if isinstance(verb, NClause):
            verb.subs[0].emit(buffers)
        else:
            verb.emit(buffers)
        noun.emit(buffers)

class NSuffix(NExpr):
    suffix: str

    def __init__(self, e, suffix):
        NExpr.__init__(self, (e,))
        self.suffix = suffix

    def __repr__(self):
        return grouping(self.subs[0]) + self.suffix

    def apply(self, dict_or_func=identity):
        return NSuffix(self.subs[0].apply(dict_or_func), self.suffix)

    def emit(self, buffers):
        self.subs[0].emit(buffers)
        buffers.append(self.suffix)

class NLiteral(NExpr):
    w: str

    def __init__(self, w):
        NExpr.__init__(self)
        self.w = str(w)

    def __repr__(self):
        return self.w

    def apply(self, dict_or_func=identity):
        if not isinstance(dict_or_func):
            return dict_or_func(self)

    def emit(self, buffers):
        buffers.append(self.w)


class NSymbol(NExpr):
    index: int
    w: str

    def __init__(self, index, w):
        NExpr.__init__(self)
        self.index = index
        self.w = str(w)

    def __repr__(self):
        return self.w
    
    def apply(self, dict_or_func=identity):
        if isinstance(dict_or_func, dict):
            if self.index in dict_or_func:
                return dict_or_func[self.index]
            if self.w in dict_or_func:
                return dict_or_func[self.w]
            return self
        else:
            return dict_or_func(self)

    def emit(self, buffers):
        buffers.append(self.w)


##
peg = pg.grammar('tokibi.pegtree')
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
        return nexpr #, self.indexes

# [#NPhrase [#NOrdered [#NSuffix [#NSymbol 'str'][# 'が']][#NSuffix [#NSymbol 'prefix'][# 'で']]][#NWord '始まるかどうか']]

    def acceptNChoice(self, tree):
        ne = NChoice(*(self.visit(t) for t in tree))
        return ne

    def acceptNPhrase(self, tree):
        ne = NPhrase(*(self.visit(t) for t in tree))
        if len(ne.subs) == 1:
            return ne.subs[0]
        return ne

    def acceptNClause(self, tree):
        ne = NClause(self.visit(tree[0]), self.visit(tree[1]))
        return ne

    def acceptNOrdered(self, tree):
        ne = NOrdered(*(self.visit(t) for t in tree))
        return ne

    def acceptNSuffix(self, tree):
        t = self.visit(tree[0])
        suffix = str(tree[1])
        return NSuffix(t, suffix)

    def acceptNSymbol(self, tree):
        s = str(tree)
        if s not in self.indexes:
            self.indexes[s] = len(self.indexes)
        return NSymbol(self.indexes[s], s)

    def acceptNLiteral(self, tree):
        s = str(tree)
        return NLiteral(s)

    def acceptNWord(self, tree):
        s = str(tree)
        w, vpos, mode = verb.parse(s.split('|')[0])
        if vpos.startswith('V') or vpos == 'ADJ':
            return NVerb(w, vpos, mode)
        return NWord(s)

    def acceptNPiece(self, tree):
        s = str(tree)
        return NWord(s)


tokibi_reader = TokibiReader()

def parse(s, synonyms=None):
    if synonyms is not None:
        tokibi_reader.synonyms = synonyms
    if s.endswith('かどうか'):
        s = s[:-4]
        e = tokibi_reader.parse(s)
        e = NClause(e, NWord('かどうか'))
    else:
        e = tokibi_reader.parse(s)
    #print(grouping(e[0]))
    return e

def read_tsv(filename):
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue
            if '#' in line:
                line = line.split('#')[1].strip()
                e = parse(line)
                print(e, e.generate())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_tsv(sys.argv[1])
    else:
        e = parse('望遠鏡で/{[子犬|Puppy]が泳ぐ}[様子|の]を見る')
        print(e, e.generate())
        e2 = parse('[猫|ねこ]が/[虎|トラ]と等しくないかどうか')
        #e2, _ = parse('{Aと/B(子犬)を/順に/[ひとつずつ]表示した}結果')
        e = parse('Aを調べる')
        e = e.apply({0: e2})
        print(e, e.generate())
        e = parse('A(事実)を調べる')
        e = e.apply({0: e2})
        print(e, e.generate())
