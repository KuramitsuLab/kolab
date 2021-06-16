# suffix

_U = 1 << 0
_A = 1 << 1
_I = 1 << 2
_E = 1 << 3
_O = 1 << 4
THEN = 1 << 5
PAST = 1 << 6
NOT = 1 << 7
CMD = 1 << 8
CASE = 1 << 9
_N = 1 << 10
POL = 1 << 11
CAN = 1 << 12
PAV = 1 << 13
LET = 1 << 14

# 補助語
# 行って／くる　　　　　　・話して／いる
# ・歌って／ほしい　　　　　・遊んで／もらう
# ・書いて／おく　　　　　　・読んで／みる
# ・寝て／しまう　　　　　　・置いて／ある

TRY = 1 << 15

# POS タイプ
VS = 'VS'  # サ変　
VZ = 'VZ'  # サ変
V1 = 'V1'  # 上一段、下一段
VK5 = 'VK5'  # カ行五段活用
VS5 = 'VS5'  # サ行五段活用
VT5 = 'VT5'  # タ行五段活用
VN5 = 'VN5'  # ナ行五段活用
VM5 = 'VM5'  # マ行五段活用
VR5 = 'VR5'  # ラ行五段活用
VW5 = 'VW5'  # ワ行五段活用
VG5 = 'VG5'  # ガ行五段活用
VB5 = 'VB5'  # バ行五段活用
ADJ = 'ADJ'  # 形容詞
NA = 'NA'


def PASTTHEN(mode):
    if mode & CASE == CASE:
        return 'ら'
    return '際に' if mode & THEN == THEN else ''


def emitADJ(w, mode):  # ない 赤い
    w = w[:-1] if w.endswith('い') else w
    if mode & CAN == CAN:
        return emitVR5(w+'くな', mode & ~CAN)
    if mode & LET == LET:
        return emitVS(w+'く', mode & ~LET)
    if mode & NOT == NOT and mode & POL == POL:
        return emitPOL(w+'くありま', mode & ~POL)
    if mode & NOT == NOT:
        return emitADJ(w+'くな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'かった' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'くて'
    if mode & CASE == CASE:
        return w + 'けば'  #
    if mode & _N == _N:
        return w + 'さ'
    if mode & _I == _I:
        return w + 'く'
    if mode & _A == _A:
        return w + 'く'  # ない
    if mode & _E == _E:
        return w + 'けれ'  # ば
    return w + 'い'


def emitV1(w, mode):  # 高める
    w = w[:-1] if w.endswith('る') else w
    if mode & POL == POL:
        return emitPOL(w+'ま', mode & ~POL)
    if mode & CAN == CAN or mode & PAV == PAV:
        return emitV1(w+'られ', mode & ~(CAN | PAV))
    if mode & LET == LET:
        return emitV1(w+'させ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'な', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'た' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'て'
    if mode & CASE == CASE:
        return w+'れば'
    if mode & CMD == CMD:
        return w+'よ'  #
    if mode & _I == _I or mode & _N == _N:
        return w
    if mode & _A == _A:
        return w  # ない
    if mode & _E == _E:
        return w+'れ'  # ば
    if mode & _O == _O:
        return w+'よ'  # う
    return w + 'る'


def emitVS(w, mode):
    w = w[:-2] if w.endswith('する') else w
    if mode & POL == POL:
        return emitPOL(w+'しま', mode & ~POL)
    if mode & PAV == PAV:
        return emitV1(w+'させられ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'させ', mode & ~LET)
    if mode & CAN == CAN:
        return emitV1(w+'でき', mode & ~CAN)
    if mode & NOT == NOT:
        return emitADJ(w+'しな', mode & ~NOT)
    if mode & PAST == PAST:
        return w + 'した' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w + 'して'
    if mode & CMD == CMD:
        return w + 'せよ'  #
    if mode & _N == _N:
        return w
    if mode & _I == _I:
        return w + 'し'
    if mode & _A == _A:
        return w + 'し'  # ない
    if mode & _E == _E:
        return w + 'すれ'  # ば
    if mode & _O == _O:
        return w + 'しよ'  # う
    return w + 'する'


def emitVZ(lemma, c):  # 論じる
    if c & THEN == THEN:
        return lemma[:-2]+'じて'
    if c & PAST == PAST:
        return lemma[:-2]+'じた'
    if c & _N == _N:
        return lemma[:-2]
    if c & _I == _I:
        return lemma[:-2]+'じ'
    if c & _A == _A:
        return lemma[:-2]+'じ'  # ない
    if c & _E == _E:
        return lemma[:-2]+'ずれ'  # ば
    if c & _O == _O:
        return lemma[:-2]+'じよ'  # う
    if c & CMD == CMD:
        return lemma[:-2]+'ぜよ'  #
    return lemma


def emitNA(w, mode):  # 立派
    w = w[:-3] if w.endswith('である') else w
    w = w[:-3] if w.endswith('でない') else w
    w = w[:-1] if w.endswith('な') else w
    if mode & POL == POL:
        if mode & NOT == NOT:
            return emitPOL(w+'でありま', mode & ~(POL | NOT))
        return w+'です'
    if mode & CAN == CAN:
        return emitVR5(w+'にな', mode & ~CAN)
    if mode & NOT == NOT:
        return emitADJ(w+'でな', mode & ~NOT)
    if mode & PAST == PAST:
        return w + 'であった' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'で'
    if mode & _I == _I or mode & _N == _N:
        return w
    return w + 'な'


def emitPOL(w, mode):  # 書きま
    w = w[:-1] if w.endswith('す') else w
    if mode & THEN == THEN:
        return w+'して'
    if mode & NOT == NOT:
        return w+'せんでした' + PASTTHEN(mode) if mode & PAST == PAST else w + 'せん'
    if mode & PAST == PAST:
        return w+'した' + PASTTHEN(mode)
    return 'ます'


def emitVK5(w, mode):  # 書く
    w = w[:-1] if w.endswith('く') else w
    if mode & POL == POL:
        return emitPOL(w+'きま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'け', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'かれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'かせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'かな', mode & ~NOT)
    if mode & PAST == PAST:
        return w + 'いた' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'いて'
    if mode & CASE == CASE:
        return w + 'けば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'き'
    if mode & _A == _A:
        return w + 'か'  # ない
    if mode & _E == _E:
        return w + 'け'  # ば
    if mode & _O == _O:
        return w + 'こ'  # う
    return w + 'く'


def emitVS5(w, mode):  # 探す
    w = w[:-1] if w.endswith('す') else w
    if mode & POL == POL:
        return emitPOL(w+'しま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'せ', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'され', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'させ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'さな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'した' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'して'
    if mode & CASE == CASE:
        return w + 'せば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'し'
    if mode & _A == _A:
        return w + 'さ'  # ない
    if mode & _E == _E:
        return w + 'せ'  # ば
    if mode & _O == _O:
        return w + 'そ'  # う
    return w + 'す'


def emitVT5(lemma, c):  # 勝つ
    if c & THEN == THEN:
        return lemma[:-1]+'って'
    if c & PAST == PAST:
        return lemma[:-1]+'った'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'ち'
    if c & _A == _A:
        return lemma[:-1] + 'た'  # ない
    if c & _E == _E:
        return lemma[:-1]+'て'  # ば
    if c & _O == _O:
        return lemma[:-1]+'と'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'て'  #
    return lemma


def emitVN5(lemma, c):  # 死ぬ
    if c & THEN == THEN:
        return lemma[:-1]+'んで'
    if c & PAST == PAST:
        return lemma[:-1]+'んだ'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'に'
    if c & _A == _A:
        return lemma[:-1] + 'な'  # ない
    if c & _E == _E:
        return lemma[:-1]+'ね'  # ば
    if c & _O == _O:
        return lemma[:-1]+'の'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'ね'  #
    return lemma


def emitVM5(lemma, c):  # 読む
    if c & THEN == THEN:
        return lemma[:-1]+'んで'
    if c & PAST == PAST:
        return lemma[:-1]+'んだ'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'み'
    if c & _A == _A:
        return lemma[:-1] + 'ま'  # ない
    if c & _E == _E:
        return lemma[:-1]+'め'  # ば
    if c & _O == _O:
        return lemma[:-1]+'も'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'め'  #
    return lemma


def emitVR5(w, mode):  # 切る, なる
    w = w[:-1] if w.endswith('る') else w
    if mode & POL == POL:
        return emitPOL(w+'りま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'れ', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'られ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'らせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'らな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'った' + PASTTHEN(mode)
    if mode & THEN == THEN:
        return w+'って'
    if mode & CASE == CASE:
        return w + 'れば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'り'
    if mode & _A == _A:
        return w + 'ら'  # ない
    if mode & _E == _E:
        return w + 'れ'  # ば
    if mode & _O == _O:
        return w + 'ろ'  # う
    return w + 'る'


def emitVW5(lemma, c):  # 笑う
    if c & THEN == THEN:
        return lemma[:-1]+'って'
    if c & PAST == PAST:
        return lemma[:-1]+'った'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'い'
    if c & _A == _A:
        return lemma[:-1] + 'わ'  # ない
    if c & _E == _E:
        return lemma[:-1]+'え'  # ば
    if c & _O == _O:
        return lemma[:-1]+'お'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'え'  #
    return lemma


def emitVG5(lemma, c):  # 防ぐ
    if c & THEN == THEN:
        return lemma[:-1]+'いで'
    if c & PAST == PAST:
        return lemma[:-1]+'いだ'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'ぎ'
    if c & _A == _A:
        return lemma[:-1] + 'が'  # ない
    if c & _E == _E:
        return lemma[:-1]+'げ'  # ば
    if c & _O == _O:
        return lemma[:-1]+'ご'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'げ'  #
    return lemma


def emitVB5(lemma, c):  # 遊ぶ
    if c & THEN == THEN:
        return lemma[:-1]+'んで'
    if c & PAST == PAST:
        return lemma[:-1]+'んだ'
    if c & _I == _I or c & _N == _N:
        return lemma[:-1] + 'び'
    if c & _A == _A:
        return lemma[:-1] + 'ば'  # ない
    if c & _E == _E:
        return lemma[:-1]+'べ'  # ば
    if c & _O == _O:
        return lemma[:-1]+'ぼ'  # う
    if c & CMD == CMD:
        return lemma[:-1]+'べ'  #
    return lemma


verb_lemma_suffix = {
    'く': VK5,
    'す': VS5,
    'つ': VT5,
    'ぬ': VN5,
    'む': VM5,
    'る': VR5,
    'う': VW5,
    'ぐ': VG5,
    'ぶ': VB5,
    'い': ADJ,
}

# VERB1c = [鋳診観視見経簸着看獲煮流歴恐得干居射寝割似出ゐ] CK_VERB1 !'し' //
# HVERB1c = [れみへひねにでてせきえうい] CK_VERB1


def guess_vpos(verb):
    if verb.endswith('る'):
        if verb.endswith('である'):
            return NA  # 　
        if verb.endswith('する'):
            return VS  # 　さ変
        if verb.endswith('ずる'):
            return VZ  # ざ変 論ずる
        if verb.endswith('る') and len(verb) > 2 and verb[-2] in 'きべえげりえれけせめびてじぎい':
            return V1
    return verb_lemma_suffix.get(verb[-1], NA)


def emit(w, mode=_U, pos=None):
    if pos is None:
        pos = guess_vpos(w)
    return globals()[f'emit{pos}'](w, mode)


def conjugate(w, mode=_U, pos=None):
    if pos is None:
        pos = guess_vpos(w)
    if mode & TRY == TRY:
        if pos == ADJ:
            return emit(w, LET | THEN, pos) + emitV1('み', mode & ~ TRY)
        return emit(w, THEN, pos) + emitV1('み', mode & ~ TRY)
    return emit(w, mode, pos)


def test(w):
    pos = guess_vpos(w)
    print(conjugate(w, _U, pos),
          conjugate(w, THEN, pos), conjugate(w, PAST | TRY | POL, pos),
          conjugate(w, NOT, pos), conjugate(w, NOT | CASE, pos),
          conjugate(w, LET, pos), conjugate(w, CAN, pos),
          conjugate(w, CAN | PAST | CASE, pos), conjugate(w, NOT | POL, pos))


test('書く')
test('使用する')
test('赤い')
test('立派である')

####


class Word(object):
    def emit(self, c=_U):
        return ''

    def isNoun(self):
        return False

    def __str__(self):
        return self.emit()


class Noun(Word):
    w: str

    def __init__(self, w):
        self.w = w

    def isNoun(self):
        return True

    def __repr__(self):
        return str(self.w)

    def emit(self, c=_U):
        if isinstance(self.w, Word):
            return self.w.emit(_N)
        return str(self.w)


class Neg(object):  # 否定あり
    pass


class Verb(Word, Neg):
    w: str  # 標準形
    pos: str

    def __init__(self, lemma, pos=None):
        self.w = lemma
        self.pos = guess_verb_pos(lemma) if pos is None else pos

    def __repr__(self):
        return self.w

    def emit(self, c=_U):
        return globals()[f'emit{self.pos}'](self.w, c)


class Suffix(Word):
    inner: Word
    suffix: str

    def __init__(self, inner, suffix=''):
        self.inner = inner
        self.suffix = suffix

    def updateInner(self, inner):
        return Suffix(inner, self.suffix)

    def emit(self, c=_U):
        return self.inner.emit(_U) + self.suffix


class Past(Suffix):
    inner: Word

    def __init__(self, inner):
        Suffix.__init__(self, inner, '')

    def updateInner(self, inner):
        return Past(inner)

    def emit(self, c=_U):
        return self.inner.emit(PAST)


class Can(Suffix, Neg):
    inner: Word

    def __init__(self, inner):
        Suffix.__init__(self, inner, '')

    def updateInner(self, inner):
        return Can(inner)

    def emit(self, c=_U):
        if isinstance(self.inner, Verb):
            if self.inner.pos == VS:  # 検索できる 検索できない
                return emitV1(self.inner.emit(_N)+'できる', c)
            if self.inner.pos == V1:  # 高められる 高められない
                return emitV1(self.inner.emit(_N)+'られる', c)
        return emitV1(self.inner.emit(_E)+'る', c)


class Passive(Suffix, Neg):
    inner: Word

    def __init__(self, inner):
        Suffix.__init__(self, inner, '')

    def updateInner(self, inner):
        return Passive(inner)

    def emit(self, c=_U):
        if isinstance(self.inner, Verb):
            if self.inner.pos == VS:  # 検索される 検索されない
                return emitV1(self.inner.emit(_N)+'される', c)
            if self.inner.pos == V1:  # 高められる 高められない
                return emitV1(self.inner.emit(_N)+'られる', c)
        return emitV1(self.inner.emit(_A)+'れる', c)


class Not(Suffix):
    inner: Word

    def __init__(self, inner):
        Suffix.__init__(self, inner, '')

    def updateInner(self, inner):
        return Not(inner)

    def emit(self, c=_U):
        return self.inner.emit(_A) + Verb('ない', ADJ).emit(c)


COMMA = '、'


class Then(Suffix):
    inner: Word
    c: int

    def __init__(self, inner, c=_I, suffix=COMMA):
        Suffix.__init__(self, inner, suffix)
        #self.inner = inner
        #self.suffix = suffix
        self.c = c

    def updateInner(self, inner):
        return Then(inner, self.c)

    def emit(self, c=_U):
        return self.inner.emit(self.c) + self.suffix


class IfCase(Suffix):
    inner: str

    def __init__(self, inner, suffix=COMMA):
        Suffix.__init__(self, inner, suffix)

    def updateInner(self, inner):
        return IfCase(inner, self.suffix)

    def __repr__(self):
        return f'{self.w}#case'

    def emit(self, c=_U):
        if self.suffix == COMMA:
            return self.inner.emit(_E) + 'ば' + COMMA
        return self.inner.emit(_U) + self.suffix


def noun_(w):
    if isinstance(w, Word) and w.isNoun():
        return w
    return Noun(w)


def can_(w):
    if isinstance(w, Verb):
        return Can(w)
    return w


def passive_(w):
    if isinstance(w, Verb):
        return Passive(w)
    return w


def past_(w):
    if isinstance(w, Verb) or isinstance(w, Not):
        return Past(w)
    return w


def not_(w):
    if isinstance(w, Neg):
        return Not(w)
    if isinstance(w, Suffix):
        if isinstance(w, Not):
            return w.inner
        else:
            return w.updateInner(not_(w.inner))
    return w


def and_(w):
    return Then(w)


def then_(w):
    return Then(w, c=THEN)


def case_(w):
    return IfCase(w)


class _Polite(object):
    inner: Verb

    def __init__(self, inner):
        self.inner = inner

    def emit(self, c=_U):
        prefix = self.inner.emit(AND, '')
        if c & THEN == THEN:
            return prefix + 'まして'
        if c & PAST == PAST:
            return prefix + 'ました'
        if c == NOT:
            return prefix + 'ません'
        return prefix + 'ます'


# 遊ぶ #polite #not #past
# 遊ぶ
# print(_Then(_Not(Verb('遊ぶ')), Noun('人')).emit(_U))


def pj_suffix(verb, ss):
    suffix = f'{ss[0]}_'
    if suffix in globals():
        verb = globals()[suffix](verb)
    if len(ss) > 1:
        return pj_suffix(verb, ss[1:])
    return verb


def pj(s):
    if '#' in s:
        ss = s.split('#')
        return pj_suffix(pj(ss[0]), ss[1:])
    pos = guess_verb_pos(s)
    if pos == 'N':
        return Noun(s)
    return Verb(s, pos)


# print(pj('等しい#not#case'))
# print(pj('等しい#then'))
# print(pj('等しい#and'))
# print(pj('書く#past'))
# print(pj('書く#past#not'))
# print(pj('書く#not#past#case'))

# print(pj('書く#can'), pj('書く#can#not'))
# print(pj('高める#can'), pj('高める#can#not'))
# print(pj('検索する#can'), pj('検索する#can#not'))

# print(pj('書く#passive#past'), pj('書く#passive#not#past'))
# print(pj('高める#passive'), pj('高める#passive#not'))
# print(pj('検索する#passive'), pj('検索する#passive#not'))
