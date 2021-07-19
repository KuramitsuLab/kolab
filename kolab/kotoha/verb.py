from janome.tokenizer import Tokenizer

# VPOS タイプ

VS = 'VS'  # サ変　
VZ = 'VZ'  # サ変
VK = 'VK'  # カ変
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
NA = 'NA'  # 形容動詞 立派だ

# mode

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
NOUN = 1 << 15  # 連体形

# 補助語
# 行って／くる　　　　　　・話して／いる
# ・歌って／ほしい　　　　　・遊んで／もらう
# ・書いて／おく　　　　　　・読んで／みる
# ・寝て／しまう　　　　　　・置いて／ある

TRY = 1 << 16
WANT = 1 << 17
GETIT = 1 << 18
OKU = 1 << 18
KURU = 1 << 19
GO = 1 << 19
ARU = 1 << 20
EXIST = 1 << 20
IRU = 1 << 21
ING = 1 << 21

MODES = {
    'pol': POL,
    'can': CAN,
    'pav': PAV,
    'let': LET,
    'case': CASE,
    'cmd': CMD,
    'past': PAST,
    'not': NOT,
    'then': THEN,
    'noun': _N,
    'try': TRY,
    'want': WANT,
    'go': KURU,
    'ing': ING,
    'getit': OKU,
}


def modes(mode):
    ss = []
    for key in MODES:
        m = MODES[key]
        if mode & m == m:
            ss.append(f'#{key}')
    return ' '.join(ss)


def _PAST(mode):
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
        return w+'かった' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'くて'
    if mode & CASE == CASE:
        return w + 'ければ'  #
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
        return w+'た' + _PAST(mode)
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
        return w + 'した' + _PAST(mode)
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


def emitVZ(w, mode):  # 論じる
    w = w[:-2] if w.endswith('ずる') else w
    if mode & POL == POL:
        return emitPOL(w+'じま', mode & ~POL)
    if mode & PAV == PAV:
        return emitV1(w+'ざせられ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'ざせ', mode & ~LET)
    if mode & CAN == CAN:
        return emitV1(w+'でき', mode & ~CAN)
    if mode & NOT == NOT:
        return emitADJ(w+'じな', mode & ~NOT)
    if mode & PAST == PAST:
        return w + 'じた' + _PAST(mode)
    if mode & THEN == THEN:
        return w + 'じて'
    if mode & CMD == CMD:
        return w + 'ぜよ'  #
    if mode & _N == _N:
        return w
    if mode & _I == _I:
        return w + 'じ'
    if mode & _A == _A:
        return w + 'じ'  # ない
    if mode & _E == _E:
        return w + 'ずれ'  # ば
    if mode & _O == _O:
        return w + 'じよ'  # う
    return w + 'ずる'


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
        return w + 'であった' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'で'
    if mode & CASE == CASE:
        return w + 'ならば'
    if mode & _I == _I or mode & _N == _N:
        return w
    if mode & NOUN == NOUN:
        return w + 'な'
    return w + 'である'


def emitPOL(w, mode):  # 書きま
    w = w[:-1] if w.endswith('す') else w
    if mode & THEN == THEN:
        return w+'して'
    if mode & NOT == NOT:
        return w+'せんでした' + _PAST(mode) if mode & PAST == PAST else w + 'せん'
    if mode & PAST == PAST:
        return w+'した' + _PAST(mode)
    return 'ます'


def emitVK(w, mode):  # くる
    w = w[:-2] if w.endswith('くる') else w
    if mode & POL == POL:
        return emitPOL('きま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1('これ', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'これ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'こせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'こな', mode & ~NOT)
    if mode & PAST == PAST:
        return w + 'きた' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'きて'
    if mode & CASE == CASE:
        return w + 'くれば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'き'
    if mode & _A == _A:
        return w + 'こ'  # ない
    if mode & _E == _E:
        return w + 'くれ'  # ば
    if mode & _O == _O:
        return w + 'こい'  # う
    return w + 'くる'


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
        return w + 'いた' + _PAST(mode)
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
        return w+'した' + _PAST(mode)
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


def emitVT5(w, mode):  # 勝つ
    w = w[:-1] if w.endswith('つ') else w
    if mode & POL == POL:
        return emitPOL(w+'ちま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'て', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'たれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'たせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'たな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'った' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'って'
    if mode & CASE == CASE:
        return w + 'てば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'ち'
    if mode & _A == _A:
        return w + 'た'  # ない
    if mode & _E == _E:
        return w + 'て'  # ば
    if mode & _O == _O:
        return w + 'と'  # う
    return w + 'つ'


def emitVN5(w, mode):  # 死ぬ
    w = w[:-1] if w.endswith('ぬ') else w
    if mode & POL == POL:
        return emitPOL(w+'にま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'ね', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'なれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'なせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'なな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'んだ' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'んで'
    if mode & CASE == CASE:
        return w + 'ねば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'に'
    if mode & _A == _A:
        return w + 'な'  # ない
    if mode & _E == _E:
        return w + 'ね'  # ば
    if mode & _O == _O:
        return w + 'の'  # う
    return w + 'ぬ'


def emitVM5(w, mode):  # 読む
    w = w[:-1] if w.endswith('む') else w
    if mode & POL == POL:
        return emitPOL(w+'みま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'め', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'まれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'ませ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'まな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'んだ' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'んで'
    if mode & CASE == CASE:
        return w + 'めば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'み'
    if mode & _A == _A:
        return w + 'ま'  # ない
    if mode & _E == _E:
        return w + 'め'  # ば
    if mode & _O == _O:
        return w + 'も'  # う
    return w + 'む'


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
        return w+'った' + _PAST(mode)
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


def emitVW5(w, mode):  # 笑う
    w = w[:-1] if w.endswith('う') else w
    if mode & POL == POL:
        return emitPOL(w+'いま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'え', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'われ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'わせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'わな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'った' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'って'
    if mode & CASE == CASE:
        return w + 'えば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'い'
    if mode & _A == _A:
        return w + 'わ'  # ない
    if mode & _E == _E:
        return w + 'え'  # ば
    if mode & _O == _O:
        return w + 'お'  # う
    return w + 'う'


def emitVG5(w, mode):  # 防ぐ
    w = w[:-1] if w.endswith('ぐ') else w
    if mode & POL == POL:
        return emitPOL(w+'ぎま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'げ', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'がれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'がせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'がな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'いだ' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'いで'
    if mode & CASE == CASE:
        return w + 'げば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'ぎ'
    if mode & _A == _A:
        return w + 'が'  # ない
    if mode & _E == _E:
        return w + 'げ'  # ば
    if mode & _O == _O:
        return w + 'ご'  # う
    return w + 'ぐ'


def emitVB5(w, mode):  # 遊ぶ
    w = w[:-1] if w.endswith('ぶ') else w
    if mode & POL == POL:
        return emitPOL(w+'びま', mode & ~POL)
    if mode & CAN == CAN:
        return emitV1(w+'べ', mode & ~CAN)
    if mode & PAV == PAV:
        return emitV1(w+'ばれ', mode & ~PAV)
    if mode & LET == LET:
        return emitV1(w+'ばせ', mode & ~LET)
    if mode & NOT == NOT:
        return emitADJ(w+'ばな', mode & ~NOT)
    if mode & PAST == PAST:
        return w+'んだ' + _PAST(mode)
    if mode & THEN == THEN:
        return w+'んで'
    if mode & CASE == CASE:
        return w + 'べば'  #
    if mode & _I == _I or mode & _N == _N:
        return w + 'び'
    if mode & _A == _A:
        return w + 'ば'  # ない
    if mode & _E == _E:
        return w + 'べ'  # ば
    if mode & _O == _O:
        return w + 'ぼ'  # う
    return w + 'ぶ'


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
        if verb.endswith('くる') or verb.endswith('来る'):
            return VK
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
    if mode & ING == ING:
        if pos != ADJ:
            return emit(w, THEN, pos) + emitV1('い', mode & ~ ING)
    return emit(w, mode, pos)


def test(w):
    pos = guess_vpos(w)
    print(conjugate(w, _U, pos),
          conjugate(w, THEN, pos), conjugate(w, PAST | TRY | POL, pos),
          conjugate(w, NOT, pos), conjugate(w, NOT | CASE, pos),
          conjugate(w, LET, pos), conjugate(w, CAN, pos),
          conjugate(w, CAN | PAST | CASE, pos), conjugate(w, NOT | POL, pos))


# test('書く')
# test('使用する')
# test('赤い')
# test('立派である')


# 遊ぶ #polite #not #past
# 遊ぶ
# print(_Then(_Not(Verb('遊ぶ')), Noun('人')).emit(_U))

def lemma_mode(s):
    lemma = s
    mode = 0
    if '#' in s:
        ss = s.split('#')
        lemma = ss[0]
        for m in ss[1:]:
            mode |= MODES.get(m, 0)
    return lemma, mode


def pj(s):
    lemma, mode = lemma_mode(s)
    return conjugate(lemma, mode)

# print(pj('等しい#not#case'))


janome = Tokenizer()

Mecab = {
    '一段': V1,
    'サ変・スル': VS,
    '五段・カ行イ音便': VK5,
    '五段・サ行': VS5,
    '五段・タ行': VT5,
    '五段・ナ行': VN5,
    '五段・ワ行': VW5,
    '五段・ワ行促音便': VW5,
    '五段・マ行': VM5,
    '五段・ラ行': VR5,
    '五段・ガ行': VG5,
    '五段・バ行': VB5,
    'サ変・−ズル': VZ,
}


def parse(s):
    mode = 0
    toks = [tok for tok in janome.tokenize(s)]
    tok = toks[0]
    start = 1
    w = tok.base_form
    pos = tok.part_of_speech
    if pos.startswith('形容詞'):
        vpos = ADJ
    elif pos.startswith('名詞'):
        vpos = NA
    elif pos.startswith('動詞'):
        if s.startswith('する'):  #「する」は擦るではない
            vpos = VS
        else:
            vpos = Mecab.get(tok.infl_type, tok.infl_type)
    else:
        print('TODO:', s, tok)
    for tok in toks[start:]:
        w2 = str(tok)
        if '特殊・ナイ' in w2 or ',ん,' in w2:
            mode |= NOT
        elif '特殊・タ' in w2:
            mode |= PAST
        elif 'サ変・スル' in w2 and vpos == NA:
            w += 'する'
            vpos = VS
        elif '助詞' in w2 and ('て' in w2 or 'で' in w2):
            mode |= THEN
        elif '助詞' in w2 and (',ば,' in w2):
            mode |= CASE
        elif '特殊・マス' in w2 or '特殊・デス' in w2:
            mode |= POL
        elif '名詞,' in w2 and vpos == NA:
            w += tok.base_form
        elif '五段・ラ行アル' in w2:
            pass
        elif '連用タ接続,ない' in w2:
            mode |= (NOT | PAST | ING)
        elif '連用テ接続,ない' in w2:
            mode |= (NOT | ING)
        elif '動詞,非自立' in w2 and mode & THEN == THEN:
            if 'みる' in w2:
                mode = (mode & ~THEN) | TRY
            elif 'いる' in w2:
                mode = (mode & ~THEN) | ING
            else:
                #print('TODO(て): ', tok)
                pass
        elif '形容詞,非自立' in w2 and mode & THEN == THEN:
            if 'ホシイ' in w2:
                mode = (mode & ~THEN) | WANT
        else:
            pass
            #print('TODO: ', tok)
    #print(w, vpos, mode)
    if vpos == NA:
        return s, vpos, mode
    return w, vpos, mode


def parse_test(s):
    w, vpos, mode = parse(s)
    print(s, w, vpos, modes(mode), mode, conjugate(w, mode, vpos))


if __name__ == '__main__':
    print(parse('する'))
    print(conjugate('食事する', THEN))
    print(conjugate('する', THEN))

'''
parse_test('置換する')
parse_test('真である')
parse_test('読みましたら')
parse_test('読みません')
parse_test('読みませんでした')
parse_test('読まなかったとき')
parse_test('読んでなかった')
parse_test('読んでいなかった')
parse_test('読んだら')
parse_test('読めば')
'''
