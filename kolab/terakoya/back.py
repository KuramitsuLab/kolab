import sys
from pegtree.visitor import ParseTreeVisitor
import pegtree as pg
import tokibi
import terakoya

from logging import getLogger
logger = getLogger(__name__)

EMPTY = tuple()

# コード表現

ALPHA = [chr(c) for c in range(ord('A'), ord('Z')+1)] + ['?']

STATIC_MODULE = {
    'math', 'pd', 'sys', 'os'
}

class NExpr(object):pass

def toCExpr(value):
    return value if isinstance(value, CExpr) else CValue(value)

# コードのクラス表現
# 全て CExpr から継承する

class CExpr(object):
    name: str
    params: tuple

    def __init__(self, name='', params=EMPTY):
        self.name = name
        self.params = params
        self.options = EMPTY

    def format(self):
        return f'undefined({self.__class__.__name__})'

    def __repr__(self):
        try:
            argv = self.params+self.options
            return self.format().format(*argv)
        except IndexError:
            print('FIXME', self.format(), argv, len(argv), argv[0], type(argv[0]))
            return self.format()

    def __lt__(self, a):
        return id(self) < id(a)

    def __len__(self):
        return len(self.params)

    def __getitem__(self, index):
        return self.params[index]

    def getoption(self, name):
        for option in self.options:
            if name == option.name:
                return option
        return None

    def unmatched(self, model) -> NExpr:
        logger.debug('undefined? ' + str(type(self)) + ' ' + str(self))
        # print('unmatched? ' + str(type(self)) + ' ' + str(self))
        return tokibi.NExpression(str(self))


class CMetaVar(CExpr):
    index: int
    original_name: str

    def __init__(self, index: int, original_name: str):
        CExpr.__init__(self)
        self.index = index
        self.original_name = original_name

    def format(self):
        return repr(self)

    def __repr__(self):
        return ALPHA[self.index]


class CValue(CExpr):
    value: object

    def __init__(self, value):
        CExpr.__init__(self)
        self.value = value

    def __repr__(self):
        if isinstance(self.value, str):
            return repr(self.value)  # FIXME
        return str(self.value)

    def format(self):
        return repr(self)

    def match(self, model) -> NExpr:
        return tokibi.NLiteral(str(self))


def stem_name(name: str):
    if name[-1].isdigit():
        return stem_name(name[:-1])
    return name


class CVar(CExpr):

    def __init__(self, name):
        CExpr.__init__(self, name)

    def format(self):
        return self.name

    def __repr__(self):
        return self.name

    def unmatched(self, model) -> NExpr:
        name = str(self.name)
        ret = stem_name(name)
        if ret in model.names:
            return tokibi.NLiteral(name, ret)
        return tokibi.NLiteral(name)


class CBinary(CExpr):

    def __init__(self, left, op, right):
        CExpr.__init__(self, op, (toCExpr(left), toCExpr(right)))

    def format(self):
        return f'{{}} {self.name} {{}}'

class CAssign(CExpr):

    def __init__(self, left, right):
        CExpr.__init__(self, '@assign', (toCExpr(left), toCExpr(right)))

    def format(self):
        return f'{{}} = {{}}'

    def match(self, model) -> NExpr: #x=1 x を 1とする a[0]
        left = self.params[0].match(model)
        right = self.params[1].match(model)
        if isinstance(self.params[0], CVar):
            if tokibi.RandomIndex % 2 == 1:
                return tokibi.NPhrase((right, 'を', left, 'と'), tokibi.NPred('する', verb.VS))
            return tokibi.NPhrase((left, 'を', right, 'と'), tokibi.NPred('する', verb.VS))
        else:
            if tokibi.RandomIndex % 2 == 1:
                return tokibi.NPhrase((left, 'を', right, 'に'), tokibi.NPred('する', verb.VS))
            return tokibi.NPhrase((right, 'を'), (left, 'に'), tokibi.NPred('代入する|セットする', verb.VS))


class CAnd(CExpr):

    def __init__(self, left, right):
        CExpr.__init__(self, 'and', (toCExpr(left), toCExpr(right)))

    def format(self):
        return f'{{}} and {{}}'

    def match(self, model) -> NExpr:
        left = self.params[0].match(model)
        right = self.params[1].match(model)
        return tokibi.NPhrase(tokibi.NChunk(tokibi.NContext(left, verb.THEN), 'かつ、'), right)


class COr(CExpr):

    def __init__(self, left, right):
        CExpr.__init__(self, 'or', (toCExpr(left), toCExpr(right)))

    def format(self):
        return f'{{}} or {{}}'

    def match(self, model) -> NExpr:
        left = self.params[0].match(model)
        right = self.params[1].match(model)
        return tokibi.NPhrase(tokibi.NChunk(tokibi.NContext(left, verb.THEN), 'または、|あるいは、'), right)


class CUnary(CExpr):

    def __init__(self, op, expr):
        CExpr.__init__(self, op, (toCExpr(expr),))

    def format(self):
        return f'{self.name} {{}}'


class CNot(CExpr):

    def __init__(self, expr):
        CExpr.__init__(self, 'not', (toCExpr(expr),))

    def format(self):
        return f'not {{}}'

    def match(self, model) -> NExpr:
        value = self.params[0].match(model)
        return value.modeNot()


class COption(CExpr):

    def __init__(self, name: str, value: CExpr):
        CExpr.__init__(self, name, (toCExpr(value),))

    def format(self):
        return f'{self.name} = {{}}'

    def unmatched(self, model) -> NExpr:
        name = tokibi.alt(model.names[self.name]) if self.name in model.names else self.name
        value = self.params[0].match(model)
        if tokibi.OPTION['MultipleSentence']:
            return tokibi.NPhrase((name, 'は'), (value, 'に'), tokibi.NPred('する', 'VS'))
        else:
            return tokibi.NPhrase((name, 'を'), (value, 'に'), tokibi.NPred('する', 'VS', mode=verb.THEN))


class CApp(CExpr):

    def __init__(self, name: str, *es):
        CExpr.__init__(self, name, tuple(toCExpr(e)
                                         for e in es if not isinstance(e, COption)))
        if len(es) != len(self.params):
            self.options = tuple(toCExpr(e)
                                 for e in es if isinstance(e, COption))

    def format(self):
        ss = []
        ss.append(self.name)
        ss.append('(')
        n = len(self.params)+len(self.options)
        if n > 0:
            ps = [',', '{}'] * (n)
            ss.extend(ps[1:])
        ss.append(')')
        return ' '.join(ss)

class CIf(CApp):

    def __init__(self, name: str, *es):
        CApp.__init__(self, name, *es)

    def format(self):
        return f'if {{}}:'

    def match(self, model) -> NExpr:
        value = self.params[0].match(model)
        if isinstance(value, tokibi.NLiteral) or isinstance(value, str):
            suffix = ' の'
            return tokibi.NChunk(value, f'{suffix} とき、|{suffix} 場合、')
        return value.modeCase()

class CWhile(CApp):

    def __init__(self, name: str, *es):
        CApp.__init__(self, name, *es)

    def format(self):
        return f'while {{}}:'

    def match(self, model) -> NExpr:
        value = self.params[0].match(model)
        suffix=' 間'
        if isinstance(value, tokibi.NLiteral) or isinstance(value, str):
            suffix = ' の' + suffix
        return tokibi.NChunk(value, f'{suffix}、|{suffix}、繰り返す')


class OOP(object):
    pass


class CMethod(CExpr, OOP):

    def __init__(self, name: str, *es):
        CExpr.__init__(self, name, tuple(toCExpr(e)
                                         for e in es if not isinstance(e, COption)))
        if len(es) != len(self.params):
            self.options = tuple(toCExpr(e)
                                 for e in es if isinstance(e, COption))

    def format(self):
        ss = ['{}', '.']
        ss.append(self.name)
        ss.append('(')
        n = len(self.params)+len(self.options)
        if n > 1:
            ps = [',', '{}'] * (n-1)
            ss.extend(ps[1:])
        ss.append(')')
        return ' '.join(ss)


class CField(CExpr, OOP):

    def __init__(self, recv: CExpr, name: str):
        CExpr.__init__(self, name, (toCExpr(recv),))

    def format(self):
        return f'{{}} . {self.name}'


class CTuple(CExpr):

    def __init__(self, *es):
        CExpr.__init__(self, "(,)", tuple(toCExpr(e) for e in es))

    def format(self):
        ss = []
        ss.append('(')
        n = len(self.params)
        if n == 1:
            ss.extend(['{}', ','])
        else:
            ps = [',', '{}'] * (n)
            ss.extend(ps[1:])
        ss.append(')')
        return ' '.join(ss)


class CList(CExpr):

    def __init__(self, *es):
        CExpr.__init__(self, "[,]", tuple(toCExpr(e) for e in es))

    def format(self):
        ss = []
        ss.append('[')
        n = len(self.params)
        if n > 0:
            ps = [',', '{}'] * (n)
            ss.extend(ps[1:])
        ss.append(']')
        return ' '.join(ss)


class CSeq(CExpr):

    def __init__(self, es):
        CExpr.__init__(self, "", es)

    def format(self):
        ss = []
        n = len(self.params)
        if n > 0:
            ps = [',', '{}'] * (n)
            ss.extend(ps[1:])
        return ' '.join(ss)

    def match(self, model):
        ss = []
        for e in self.params:
            ss.append('、')
            ss.append(e.match(model))
        return tokibi.NChunk(*ss[1:])


class CData(CExpr):

    def __init__(self, *es):
        CExpr.__init__(self, "{,}", tuple(toCExpr(e) for e in es))

    def format(self):
        ss = []
        ss.append('{')
        for i in range(0, len(self.params), 2):
            ss.extend(['{}', '=', '{}', ','])
        ss.append('}')
        return ' '.join(ss)


class CIndex(CExpr, OOP):

    def __init__(self, recv, index):
        CExpr.__init__(self, "@index", (toCExpr(recv), toCExpr(index)))

    def format(self):
        return f'{{}} [ {{}} ]'


class CEmpty(CExpr, OOP):

    def __init__(self):
        CExpr.__init__(self, "@empty")

    def format(self):
        return ''

CEMPTY = CEmpty()

class CSlice(CExpr):

    def __init__(self, recv, start=CEMPTY, stop=CEMPTY, step=CEMPTY):
        CExpr.__init__(self, "[]", (toCExpr(recv),
                                    toCExpr(start),  toCExpr(stop), toCExpr(step)))

    def format(self):
        return f'{{}} [ {{}} : {{}} : {{}}]'

##
peg = pg.grammar('kotoha.pegtree')
snipet_parser = pg.generate(peg, start='Snipet')

class CodeParser(ParseTreeVisitor):

    def __init__(self):
        ParseTreeVisitor.__init__(self)
        self.symbols = EMPTY
        self.modules = STATIC_MODULE
        # self.names = {}
        # self.synonyms = {}
        # self.newnames = set()

    def parse(self, source, symbols=EMPTY):
        self.symbols = symbols
        tree = snipet_parser(source)
        return self.visit(tree)

    def isRuleMode(self):
        return self.symbols is not EMPTY

    def acceptSource(self, tree):
        for t in tree:
            self.visit(t)

    def acceptAssignment(self, tree):
        left = self.visit(tree.left)  # xをyとする
        right = self.visit(tree.right)
        return CAssign(left, right)

    def acceptSelfAssignment(self, tree):
        name = str(tree.name)
        left = self.visit(tree.left)
        right = self.visit(tree.right)
        return CBinary(left, name, right)

    def acceptInfix(self, tree):
        name = str(tree.name)
        left = self.visit(tree.left)
        right = self.visit(tree.right)
        return CBinary(left, name, right)

    def acceptAnd(self, tree):
        left = self.visit(tree.get('left'))
        right = self.visit(tree.get('right'))
        return CAnd(left, right)

    def acceptOr(self, tree):
        left = self.visit(tree.get('left'))
        right = self.visit(tree.get('right'))
        return COr(left, right)

    def acceptUnary(self, tree):
        name = str(tree.name)
        expr = self.visit(tree.expr)
        return CUnary(name, expr)

    def acceptNot(self, tree):
        expr = self.visit(tree[0])
        return CNot(expr)

    def acceptApplyExpr(self, tree):
        name = str(tree.name)
        params = self.visit(tree.params)
        return CApp(name, *params)

    def acceptArguments(self, tree):
        return [self.visit(e) for e in tree]

    def acceptOption(self, tree):
        value = self.visit(tree[1])
        return COption(str(tree[0]), value)

    def acceptMethodExpr(self, tree):
        recv = self.visit(tree.recv)
        name = str(tree.name)
        params = self.visit(tree.params)
        if isinstance(recv, CVar):
            if self.isRuleMode() and recv.name.startswith('_'):
                return CApp(recv.name[1:] + '.' + name, *params)
            if recv.name in self.modules:
                return CApp(recv.name + '.' + name, *params)
        return CMethod(name, *([recv]+params))

    def acceptGetExpr(self, tree):
        recv = self.visit(tree.recv)
        name = str(tree.name)
        if isinstance(recv, CVar):
            if self.isRuleMode() and recv.name.startswith('_'):
                recv.name = recv.name[1:] + '.' + name
                return recv
            if recv.name in self.modules or '.' in recv.name:
                recv.name += '.' + name
                return recv
        return CField(recv, name)  # Fixme

    def acceptIndexExpr(self, tree):
        recv = self.visit(tree.recv)
        index = self.visit(tree.index)
        return CIndex(recv, index)

    def acceptName(self, tree):
        s = str(tree)
        if self.isRuleMode():
            if s in self.symbols:
                return CMetaVar(self.symbols[s], s)
        return CVar(s)

    def acceptString(self, tree):
        s = str(tree)
        if s.startswith("'") and s.endswith("'"):
            s = s[1:-1].encode('unicode-escape').decode('unicode-escape')
        if s.startswith('"') and s.endswith('"'):
            s = s[1:-1].encode('unicode-escape').decode('unicode-escape')
        return CValue(s)

    def acceptInt(self, tree):
        s = str(tree)
        if s.startswith('0b') or s.startswith('0B'):
            n = int(s[2:],2)
        elif s.startswith('0x') or s.startswith('0X'):
            n = int(s[2:],16)
        else:
            n = int(s)
        return CValue(n)

    def acceptDouble(self, tree):
        try:
            s = str(tree).replace(' ', '')
            return CValue(float(s))
        except ValueError:
            return CValue(0.0)

    def acceptTrue(self, tree):
        return CValue(True)

    def acceptFalse(self, tree):
        return CValue(False)

    def acceptNull(self, tree):
        return CValue(None)

    def acceptList(self, tree):
        es = [self.visit(t) for t in tree]
        return CList(*es)

    def acceptTuple(self, tree):
        es = [self.visit(t) for t in tree]
        return CTuple(*es)

    def acceptList(self, tree):
        es = [self.visit(t) for t in tree]
        return CList(*es)

    def acceptIf(self, tree):
        e = self.visit(tree[0])
        return CIf('if', e)

    def acceptWhile(self, tree):
        e = self.visit(tree[0])
        return CWhile('while', e)

    def acceptUndefined(self, tree):
        logger.warning(f'@undefined {repr(tree)}')
        s = str(tree)
        return CValue(s)

    def accepterr(self, tree):
        print(repr(tree))
        raise RuntimeError

# cmatch

def cmatch(cpat, code, mapped: dict):
        if cpat.__class__ is not code.__class__:
            return False
        if cpat.name != code.name or len(cpat.params) != len(code.params):
            return False
        for e, e2 in zip(cpat.params, code.params):
            # print(':: ', type(e), e, type(e2), e2)
            if isinstance(e, CMetaVar):
                if e.index in mapped:
                    if str(mapped[e.index]) != str(e2):
                        return False
                    else:
                        continue
                mapped[e.index] = e2
                continue
            if isinstance(e, CValue) and isinstance(e2, CValue):
                if e.value != e2.value:
                    return False
                continue
            if not cmatch(e, e2, mapped):
                return False
        for opat in cpat.options:
            option = code.getoption(opat.name)
            if option is None:
                return False
            if not cmatch(opat, option, mapped):
                return False
        if len(code.options) > 0:
            os = []
            for option in code.options:
                opat = cpat.getoption(option.name)
                if opat is None:
                    os.append(option)
            mapped['options'] = os
        return True


class BTModel(ParseTreeVisitor):
    rules: dict
    def __init__(self):
        ParseTreeVisitor.__init__(self)
        self.rules = {}
        self.reader = CodeParser()
        # self.symbols = EMPTY
        # self.names = {}
        # self.modules = STATIC_MODULE
        # self.synonyms = {}
        # self.newnames = set()

    def load(self, *filenames):
        dataset=[]
        synonyms = {}
        for filename in filenames:
            if filename.endswith('.txt'):
                terakoya.read_terakoya(filename, synonyms, dataset)
        #
        for code, desc in dataset:
            for doc in desc:
                try:
                    ndoc, symbols = tokibi.parse2(doc.strip(), synonyms)
                    cpat = self.reader.parse(code, symbols)
                    if cpat.name != '':
                        self.add_rule(cpat, len(symbols), ndoc)
                    else:
                        print(cpat.name, cpat, type(cpat), ndoc)
                except RuntimeError:
                    pass

    def add_rule(self, cpat: CExpr, size, pred: NExpr):
        name = cpat.name
        assert name != ''
        # if len(cpat.params) > 0 and isinstance(cpat.params[0], CMetaVar):
        #     ns = cpat.params[0].original_name
        #     if len(ns) > 1:
        #         lname = f'{ns}.{name}'
        #         if lname not in self.rules:
        #             self.rules[lname] = []
        #         # print('adding', lname, (size, cpat, pred))
        #         self.rules[lname].append((size, cpat, pred))
        #         if name not in self.rules or ns in self.newnames:
        #             self.newnames.add(ns)
        #         else:
        #             # print(f'{lname}のみ登録', cpat, pred)
        #             return
        if name not in self.rules:
            self.rules[name] = []
        #print('adding', name, (size, cpat, pred))
        self.rules[name].append((size, cpat, pred))

    def predict(self, source: str) -> tuple:
        code = self.reader.parse(source)
        name = code.name
        # print('matching', name)
        # if len(code.params) > 0:  # レシーバの型を調べる
        #     recv = self.match(code.params[0])
        #     if hasattr(recv, 'ret') and recv.ret is not None:
        #         lname = f'{recv.ret}.{name}'
        #         # print('@レシーバの型', recv.ret, lname)
        #         if lname in self.rules:
        #             name = lname
        while name not in self.rules and '.' in name:
            loc = name.find('.')
            name = name[loc+1:]
        if name in self.rules:
            for _, pat, pred in self.rules[name]:
                mapped = {}
                # print(f'trying {name}.. ', pat, type(code), code)
                if cmatch(pat, code, mapped):
                    for key in mapped.keys():
                        if key == 'options':
                            mapped[key] = [self.match(e) for e in mapped[key]]
                        else:
                            mapped[key] = self.match(mapped[key])
                    return pred.apply(mapped)
            # print(f'unmatched: {name}', str(code), type(code))
            if len(code.params) > 0 and isinstance(code, CApp):  
                # パラメータ圧縮する print(1,2,3) -> print(1,(2,3))
                paramsize = max(size for size, _, _ in self.rules[name])
                # print('減らす', name, paramsize,
                #       code.params[:paramsize-1], code.params[paramsize-1:])
                if len(code.params) > paramsize > 0:
                    ss = list(code.params[:paramsize-1])
                    ss.append(CSeq(code.params[paramsize-1:]))
                    code.params = tuple(ss)
                    return self.match(code)
        print('predict others..', code)
        return None

    def predict(self, code):
        tree = snipet_parser(code)
        # print(repr(tree))
        docs = self.visit(tree)
        return docs

    def acceptSource(self, tree):
        for t in tree:
            docs = self.visit(t)
        return docs

    def acceptAssignment(self, tree):
        left = self.visit(tree.left)  # xをyとする
        right = self.visit(tree.right)
        return CAssign(left, right)

    def acceptSelfAssignment(self, tree):
        name = str(tree.name)
        left = self.visit(tree.left)
        right = self.visit(tree.right)
        return CBinary(left, name, right)

    def acceptInfix(self, tree):
        name = str(tree.name)
        left = self.visit(tree.left)
        right = self.visit(tree.right)
        return CBinary(left, name, right)

    def acceptAnd(self, tree):
        left = self.visit(tree.get('left'))
        right = self.visit(tree.get('right'))
        return CAnd(left, right)

    def acceptOr(self, tree):
        left = self.visit(tree.get('left'))
        right = self.visit(tree.get('right'))
        return COr(left, right)

    def acceptUnary(self, tree):
        name = str(tree.name)
        expr = self.visit(tree.expr)
        return CUnary(name, expr)

    def acceptNot(self, tree):
        expr = self.visit(tree[0])
        return CNot(expr)

    def acceptApplyExpr(self, tree):
        name = str(tree.name)
        params = self.visit(tree.params)
        return CApp(name, *params)

    def acceptArguments(self, tree):
        return [self.visit(e) for e in tree]

    def acceptOption(self, tree):
        value = self.visit(tree[1])
        return COption(str(tree[0]), value)

    def acceptMethodExpr(self, tree):
        recv = self.visit(tree.recv)
        name = str(tree.name)
        params = self.visit(tree.params)
        if isinstance(recv, CVar):
            if self.isRuleMode() and recv.name.startswith('_'):
                return CApp(recv.name[1:] + '.' + name, *params)
            if recv.name in self.modules:
                return CApp(recv.name + '.' + name, *params)
        return CMethod(name, *([recv]+params))

    def acceptGetExpr(self, tree):
        recv = self.visit(tree.recv)
        name = str(tree.name)
        if isinstance(recv, CVar):
            if self.isRuleMode() and recv.name.startswith('_'):
                recv.name = recv.name[1:] + '.' + name
                return recv
            if recv.name in self.modules or '.' in recv.name:
                recv.name += '.' + name
                return recv
        return CField(recv, name)  # Fixme

    def acceptIndexExpr(self, tree):
        recv = self.visit(tree.recv)
        index = self.visit(tree.index)
        return CIndex(recv, index)

    def acceptName(self, tree):
        s = str(tree)
        if self.isRuleMode():
            if s in self.symbols:
                return CMetaVar(self.symbols[s], s)
        return CVar(s)

    def acceptString(self, tree):
        s = str(tree)
        if s.startswith("'") and s.endswith("'"):
            s = s[1:-1].encode('unicode-escape').decode('unicode-escape')
        if s.startswith('"') and s.endswith('"'):
            s = s[1:-1].encode('unicode-escape').decode('unicode-escape')
        return CValue(s)

    def acceptInt(self, tree):
        s = str(tree)
        if s.startswith('0b') or s.startswith('0B'):
            n = int(s[2:],2)
        elif s.startswith('0x') or s.startswith('0X'):
            n = int(s[2:],16)
        else:
            n = int(s)
        return CValue(n)

    def acceptDouble(self, tree):
        try:
            s = str(tree).replace(' ', '')
            return CValue(float(s))
        except ValueError:
            return CValue(0.0)

    def acceptTrue(self, tree):
        return CValue(True)

    def acceptFalse(self, tree):
        return CValue(False)

    def acceptNull(self, tree):
        return CValue(None)

    def acceptList(self, tree):
        es = [self.visit(t) for t in tree]
        return CList(*es)

    def acceptTuple(self, tree):
        es = [self.visit(t) for t in tree]
        return CTuple(*es)

    def acceptList(self, tree):
        es = [self.visit(t) for t in tree]
        return CList(*es)

    def acceptIf(self, tree):
        e = self.visit(tree[0])
        return CIf('if', e)

    def acceptWhile(self, tree):
        e = self.visit(tree[0])
        return CWhile('while', e)

    def acceptUndefined(self, tree):
        logger.warning(f'@undefined {repr(tree)}')
        s = str(tree)
        return CValue(s)

    def accepterr(self, tree):
        # print(repr(tree))
        raise InterruptedError

if __name__ == '__main__':
    if len(sys.argv) > 1:
        model = BTModel()
        model.load(*sys.argv[1:])
        import readline
        try:
            while True:
                line = input('Snipet >>> ')
                if line == '':
                    print('Bye')
                    sys.exit(0)
                docs = model.predict(line)
                print(line, '\t#', docs)
        except EOFError:
            print('Bye')


# def EOS(s):
#     return s if s.endswith('、') else s + '。'        

# class KotohaModel(object):
#     rules: dict
#     names: dict
#     reader: Reader

#     def __init__(self):
#         self.rules = {}
#         self.reader = Reader(self.rules)
#         self.names = {}

#     def load(self, *files):
#         for file in files:
#             with open(file) as f:
#                 source = f.read()
#                 tree = parser(source, urn=file)
#                 self.reader.visit(tree)
#         for key in self.rules:
#             d = self.rules[key]
#             if len(d) > 1:
#                 self.rules[key] = sorted(d)
#         self.names = self.reader.names

#     def translate(self, expression, suffix='。'):
#         tokibi.randomize()
#         try:
#             tree = snipet_parser(expression)
#             # print(repr(tree))
#             code = self.reader.visit(tree)
#             # print(type(code), code)
#             pred = code.match(self)
#             if tokibi.OPTION['MultipleSentence']:
#                 buffer = []
#                 main = EOS(tokibi.emit(pred, 0, '', buffer))
#                 if len(buffer) > 0:
#                     main += tokibi.alt('その際、|そこで、|') + (suffix.join(buffer))+suffix
#                 return code, main
#             return code, EOS(tokibi.emit(pred))
#         except InterruptedError:
#             return expression, None

#     def generate(self, w, *files):
#         for file in files:
#             with open(file) as f:
#                 for line in f.readlines():
#                     line = line.strip()
#                     if line == '' or line.startswith('#'):
#                         continue
#                     if '\t' in line:
#                         line = line.split('\t')[0]
#                     code, doc = self.translate(line)
#                     if doc is not None:
#                         print(code, '\t', doc, file=w)

# if __name__ == '__main__':
#     model = KotohaModel()
#     argv = sys.argv[1:]
#     rule_files = []
#     input_files = []
#     tsvfile = sys.stdout
#     for s in sys.argv[1:]:
#         if s.endswith('.py'):
#             if s.endswith('rule.py'):
#                 rule_files.append(s)
#             else:
#                 input_files.append(s)
#         if s.endswith('.tsv'):
#             tsvfile = open(s, 'w')
#         if s.endswith('=True'):
#             key, _ = s.split('=')
#             if key in tokibi.OPTION:
#                 tokibi.OPTION[key] = True
#             else:
#                 logger.warning(f'unknown option: {key}')
#         if s.endswith('=False'):
#             key, _ = s.split('=')
#             if key in tokibi.OPTION:
#                 tokibi.OPTION[key] = False
#             else:
#                 logger.warning(f'unknown option: {key}')
#     model.load(*rule_files)
#     if len(input_files) > 0:
#         model.generate(tsvfile, *input_files)
#     else:
#         import readline
#         try:
#             while True:
#                 line = input('Snipet >>> ')
#                 if line == '':
#                     print('Bye')
#                     sys.exit(0)
#                 code, doc = model.translate(line, suffix='。')
#                 print(code, '\t#', doc)
#         except EOFError:
#             print('Bye')
