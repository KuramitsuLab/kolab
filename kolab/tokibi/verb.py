from sys import setrecursionlimit
from janome.tokenizer import Tokenizer

# Verb

class Verb(object):
    base: str
    vpos: str
    mode: int
    def _init__(self, base, mode, vpos=None):
        self.base = base
        self.mode = mode
        self.vpos = vpos


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

def detect_vpos(s):
    toks = [print(tok) for tok in janome.tokenize(s)]
    toks = [tok for tok in janome.tokenize(s)][::-1]
    vpos = None
    base = None
    prefix=''
    for t in toks:
        pos = t.part_of_speech
        if base is None and pos.startswith('動詞'):
            vpos = Mecab.get(t.infl_type, t.infl_type)
            base = t.base_form
            continue
        elif base is None and pos.startswith('形容詞'):
            vpos = ADJ
            base = t.base_form
            continue
        if base is not None:
            prefix = t.surface + prefix
    print(s, vpos, base, prefix)
    return vpos, base, prefix

# mode

基本形 = 0
未然形 = 1 << 0
連用形 = 1 << 1
仮定形 = 1 << 2
命令形 = 1 << 3
接続形 = 1 << 4
過去形 = 1 << 5
否定形 = 1 << 6
丁寧形 = 1 << 7
できる = 1 << 8
させる = 1 << 9
せる = 1 << 10
れる = 1 << 11
される = 1 << 12

# 補助語
# 行って／くる　　　　　　・話して／いる
# ・歌って／ほしい　　　　　・遊んで／もらう
# ・書いて／おく　　　　　　・読んで／みる
# ・寝て／しまう　　　　　　・置いて／ある

みる = 1 << 16
欲しい = 1 << 17
おく = 1 << 18
くる = 1 << 19
いく = 1 << 19
ある = 1 << 20
いる = 1 << 21

VSHIFT = 32

MODES = {
    '丁寧形': 丁寧形,
    'できる': できる,
    'させる': させる,
    'せる': せる,
    'れる': れる,
    '未然形': 未然形,
    '過去形': 過去形,
    '否定形': 否定形,
    '接続形': 接続形,
}

def detect_mode(s):
    toks = [str(tok) for tok in janome.tokenize(s)]
    mode = 0
    for t in toks:
        if '未然形' in t:
            mode |= 未然形
        elif '連用形' in t:
            mode |= 連用形
        elif '仮定形' in t:
            mode |= 仮定形
        elif '特殊・タ' in t:
            mode |= 過去形
        elif '接続助詞' in t and 'て,テ,テ' in t:
            mode |= 接続形
        elif 'させる' in t: # 動詞,接尾,*,*,一段,基本形,させる,サセル,サセル
            mode = させる
        elif 'せる' in t: #動詞,接尾,*,*,一段,基本形,せる,セル,セル
            mode = せる
        elif 'れる' in t: #動詞,接尾,*,*,一段,基本形,れる,レル,レル
            mode = れる
        # elif 'できる' in t: # 動詞,自立,*,*,一段,連用形,できる,デキ,デキ
        #     mode = できる
        elif '特殊・マス' in t:
            mode = 丁寧形
        elif '特殊・ナイ' in t:
            mode = 否定形
        elif '不変化型,基本形,ん,ン,ン' in t:
            mode |= 否定形
        elif mode & 接続形 == 接続形 and '一段' in t and ',みる,' in t:
            # 動詞,非自立,*,*,一段,基本形,みる,ミル,ミル
            # 動詞,非自立,*,*,一段,連用形,みる,ミ,ミ
            mode = (mode << VSHIFT) | みる
    detect_vpos(s)
    print(mode)
    return mode

VAR = {
    VS: (2, 'し', 'し', 'して', 'した', 'する', 'すれ', 'しろ'),
    #VZ = 'VZ'  # サ変
    #VK = 'VK'  # カ変
    V1: (1, '', '', 'て', 'た', 'る', 'れ', 'ろ'),
    VK5: (1, 'か', 'き', 'いて', 'いた', 'く', 'け', 'こ'),
    VS5: (1, 'さ', 'し', 'して', 'した', 'す', 'せ', 'そ'),
    VT5: (1, 'た', 'ち', 'って', 'った', 'つ', 'て', 'と'),
    VN5: (1, 'な', 'に', 'んで', 'んだ', 'ぬ', 'ね', 'の'),
    VM5: (1, 'ま', 'み', 'んで', 'んだ', 'む', 'め', 'も'),
    VR5: (1, 'ら', 'り', 'って', 'った', 'る', 'れ', 'ろ'),
    VW5: (1, 'わ', 'い', 'って', 'った', 'う', 'え', 'お'),
    VG5: (1, 'が', 'ぎ', 'いで', 'いだ', 'ぐ', 'げ', 'ご'),
    VB5: (1, 'ば', 'び', 'んで', 'んだ', 'ぶ', 'べ', 'ぼ'),
    ADJ: (1, 'く', 'く', 'くて', 'かった', 'い', 'けれ', ''),
    'ます': (1, 'ません', '', 'まして', 'ました', 'ます', 'ませ', '')
    # NA = 'NA'  # 形容動詞 立派だ
}

def varindex(mode):
    if mode & 接続形 == 接続形: return 3
    if mode & 過去形 == 過去形: return 4
    if mode & 未然形 == 未然形: return 1
    if mode & 連用形 == 連用形: return 2
    if mode & 仮定形 == 仮定形: return 6
    if mode & 命令形 == 命令形: return 7
    if mode == 基本形: return 5
    print('dedug mode =', mode)
    return 5

def emit_impl(base, vpos, mode):
    if mode & みる == みる:
        base = emit_impl(base, vpos, mode >> VSHIFT)
        return emit_impl('みる', V1, mode & ~みる)
    if mode & させる == させる:
        if vpos == VS or vpos == VZ:
            return emit_impl(base[:-2]+'させる', V1, mode & ~させる)
        base = emit_impl(base, vpos, 未然形) + 'させる'
        return emit_impl(base, V1, mode & ~させる)
    if mode & せる == せる:
        if vpos == VS or vpos == VZ:
            return emit_impl(base[:-2]+'させる', V1, mode & ~させる)
        base = emit_impl(base, vpos, 未然形) + 'せる'
        return emit_impl(base, V1, mode & ~せる)
    if mode & される == される:
        if vpos == VS or vpos == VZ:
            return emit_impl(base[:-2]+'される', V1, mode & ~される)
        base = emit_impl(base, vpos, 未然形) + 'される'
        return emit_impl(base, V1, mode & ~される)
    if mode & れる == れる:
        if vpos == VS or vpos == VZ:
            return emit_impl(base[:-2]+'される', V1, mode & ~れる)
        base = emit_impl(base, vpos, 未然形) + 'れる'
        return emit_impl(base, V1, mode & ~れる)
    if mode & できる == できる:
        if vpos == VS or vpos == VZ:
            return emit_impl(base[:-2]+'できる', V1, mode & ~できる)
        if vpos == V1:
            return emit_impl(base[:-1]+'られる', V1, mode & ~できる)
        ## 書く -> 書ける
        base = emit_impl(base, vpos, 仮定形)+'る'
        return emit_impl(base, V1, mode & ~できる)
    if mode & 丁寧形 == 丁寧形:
        base = emit_impl(base, vpos, 連用形) + 'ます'
        return emit_impl(base, 'MASU', mode & ~丁寧形)
    if mode & 否定形 == 否定形:
        base = emit_impl(base, vpos, 未然形) + 'ない'
        return emit_impl(base, ADJ, mode & ~否定形)
    d = VAR[vpos]
    base = base[:-d[0]]
    return base + d[varindex(mode)]
    
def modes(mode):
    ss = []
    for key in MODES:
        m = MODES[key]
        if mode & m == m:
            ss.append(f'#{key}')
    return ' '.join(ss)
    

def test(s):
    vpos, base, prefix = detect_vpos(s)
    mode = detect_mode(s)
    print(s, '=>', emit_impl(prefix+base, vpos, mode))

if __name__ == '__main__':
    test('彼はごん攻めする')
    test('入力された')
    print('入力した => ', emit_impl('入力する', VS, れる|過去形|仮定形))
    print('書かれた => ', emit_impl('書く', VK5, れる|過去形|否定形))

