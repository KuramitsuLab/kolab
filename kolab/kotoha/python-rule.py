# 準備
import string
import math

object = ''
x, y, z, n = ''
num, n, n2 = ''  # 数値
str, _str, s, s2, s3, str2 = '文字列'
c, c2 = '文字'
list, list2 = 'リスト'
tuple, tuple2 = 'タプル'
iterable, iterable2 = '列|イテレータ'  # symbol
file = "ファイル"
filename = "ファイル名"

_用いる = '使う|する|用いる'
_プリントする = '表示する|出力する|プリントする'
_セパレータ = '区切り記号|区切り文字列|セパレータ'


# 演算子

x = y  # yを/xと呼ぶ
x % 2 == 0   # xが/偶数かどうか
x % 2 == 1   # xが/奇数かどうか
x % 2 != 0   # xが/奇数かどうか
x % 2 != 1   # xが/偶数かどうか
x % y == 0   # xが/yの倍数かどうか
x % y == 0   # xが/yの倍数でないかどうか
x == y     # xが/yに等しいかどうか
x != y     # xが/yに等しくないかどうか

_同一 = '同じ|同一'
x is y     # xが/yと/同一かどうか
x is not y     # xが/yと/同一でないかどうか

_含まれる = '含まれる|ある'
_含まれない = '含まれない|ない'
_内 = '内|の中|中'

x in y     # xが/y内に/含まれるかどうか
x not in y     # xが/y内に/含まれないかどうか

x ** y  # xのy乗 -> int
x | y  # xとyの/論理和 -> int
x ^ y  # xとyの/排他的論理和 -> int
x & y  # xとyの/論理積 -> int
x << n  # xの/nビット左シフト -> int
x >> n  # xの/nビット右シフト -> int
~x  # xの/ビット反転 -> int

x + y  # x + y
x - y  # x `-` y
x * y  # x × y
x / y  # x / y
x // y  # x / y
x + y + z  # x + y + z
str + x  # strとxを/連結する -> str
str + x + y  # str、x、yを/連結する -> str
str * x   # strを/x個、/連結する -> str

# 組み込み関数（計算）

abs(x)  # xの/絶対値 -> int
bool(x)  # xが/真かどうか
complex(x, y)  # x(実数部), y(虚数部)の/複素数 -> complex
divmod(x, y)  # xとyの/(商,余り) -> tuple

float(x)  # xの浮動小数点数

int(x)  # xを/整数に/変換する -> int(値)
int(x, n)  # xを/n進整数に/変換する -> int(値)
base = x  # xを/基数とする

_コードポイント = '文字コード|コードポイント'

ord(c)  # cの/コードポイント

_大きな方 = '大きな値|大きな方|最大値'
_小さな方 = '小さな値|小さな方|最小値'

min(x)  # 数列xの/最大値 -> int
max(x, y)  # xと yの/大きな方 -> int
max(x, y, z)  # x, y, zの/最大値 -> int

min(x)  # 数列xの/最小値 -> int
min(x, y)  # xとyの/小さな方 -> int
min(x, y, z)  # x, y, zの/最小値 -> int

pow(x, y)  # xのy乗 -> int
pow(x, y, z)  # xのy乗を/zで/剰余する -> int

_丸める = '四捨五入する|丸める'
round(x)  # xの丸める -> int
round(x, n)  # xの少数部を/n桁[まで|]で丸める -> int
math.trunc(x)  # xの少数部を/切り捨てる -> int
math.floor(x)  # x以下の最大の整数 -> int
math.ceil(x)  # x以上の最小の整数 -> int

# 組み込み関数（文字列）

ascii(x)  # xの/印字可能な文字列 -> str

bin(x)  # xの/２進数文字列 -> str
hex(x)  # xの/16進数文字列 -> str
oct(x)  # xの/8進数文字列 -> str

chr(c)  # c(コードポイント)の/文字 -> str
repr(object)  # objectの/印字可能な文字列 -> str
str(x)  # xの/文字列 -> str

# 組み込み関数（リスト）

x[y]  # x [ y ]

all(iterable)  # iterableの全ての要素が/真かどうか -> bool
any(iterable)  # iterableのいずれかの要素が/真かどうか -> bool

enumerate(x)  # xの/順序数列 -> list
enumerate(x, y)  # xのyから始まる/順序数列 -> list
start = x  # startから始まる

_長さ = '長さ|要素数|サイズ|長さ'

iter(x)  # xの/イテレータ -> iterable
len(x)  # xの/長さ -> int
len(str)  # strの/文字数 -> int

list(x)  # xからの/リスト -> list

next(x)  # xの/次

range(x)  # 0からxまでの/数列 -> list
range(x, y)  # xからyまでの/数列 -> list
range(x, y, z)  # xからyまでの/zごとによる/数列 -> list
step = x  # 間隔はxにする

reversed(x)  # xの/逆順 -> list

set(x)  # xの/集合 -> set


_スライス = '部分列|スライス'

slice(x)  # 0からxまでの/スライス -> list
slice(x, y)  # xからyまでの/スライス -> list
slice(x, y, z)  # xからyまでの/zごとによる/スライス -> list

_ソートする = 'ソートする|整列する|ソートする'

sorted(x)  # xを/ソートする -> list
reverse = False  # 逆順にする
key = x  # xを/キーとする

_合計 = '合計値|総和|合計'
_平均 = '平均値|平均'

sum(x)  # x(数列)の合計 -> int
sum(x)/len(x)  # x(数列)の平均 -> int
tuple(x)  # xのタプル -> list

zip(x, y)  # xと yの各要素のペア列 -> list
zip(x, y, z)  # x, y, zの各要素のタプル列 -> list

# 組み込み関数（辞書）

dict, dict2 = '辞書'
key = '項目名|キー'

_エントリ = '項目|エントリ'
_アップデートする = '更新する|アップデートする'

dict(x)  # xの辞書 -> dict

dict[key]  # dictの/key(エントリ) -> x
list(dict)  # dictの/キー一覧 -> list
len(dict)  # dictの/エントリ数 -> int
dict.clear()  # dictの全てのエントリを/消去する
dict.copy()  # dictの/[浅い|]コピー -> dict

dict.get(key)  # dictの/key(エントリ) -> x
dict.get(key, x)  # dictのkey(エントリ)か、もし[存在し|]なければ x -> x
dict.items()  # 辞書の/エントリ一覧 -> list
dict.keys()  # dictの/エントリ一覧 -> list
dict.pop(key)  # dictのkey(エントリ)を/取り出す -> x
dict.popitem()  # dictから/最後に追加したエントリを/取り出す -> x

dict.setdefault(key, x)  # dict内にkey(エントリ)が[存在し|]なければ、そのエントリを/xにする -> x

dict.update()  # dictを/アップデートする
dict.update(x)  # dictを/xで/アップデートする

dict.values()  # dictの/値一覧 -> list

dict | dict2  # dictと/dict2を/マージする -> dict
dict |= dict2  # dictに/dict2を/加える -> dict


# 組み込み関数（バイト列、IO）

encoding = 'エンコーディング|文字コード'
errors = 'エラーポリシー'
codepoint = 'コードポイント|文字コード'

bytearray(x)  # xのバイト配列 -> bytes
bytes(x)  # xのバイト列 -> bytes
errors = errors  # errorsに/したがう
encoding = 'utf-8'  # UTF8を/用いる
errors = 'strict'  # エラー処理は/厳密にする
errors = 'ignore'  # エラー処理は/しない

prompt = 'プロンプト'
input()  # 入力された 文字列 -> str
input(s)  # s(プロンプト)に対し、入力される -> str

memoryview(x)  # xのメモリビュー

_オープンする = '開く|オープンする'

open(filename)  # filenameを/オープンする -> file
open(filename, 'r')  # filenameを/読み込みモードで/オープンする -> file
open(filename, 'w')  # filenameを/書き込みモードで/オープンする -> file
open(filename, 'a')  # filenameを/追加書き込みモードで/オープンする -> file
mode = 'r'  # 読み込みモードを/用いる
mode = 'w'  # 書き込みモードを/用いる
mode = 'a'  # 追加モードを/用いる
mode = 'b'  # バイナリモードを/用いる
mode = 'モード'
newline = '改行コード'
buffering = -1  # バッファリングしない
buffering = x  # バッファリングは/xサイズにする

_プリントする = '表示する|出力する|プリントする'
print()  # 空行を/プリントする
print(x)  # xを/プリントする
print(x, y)  # xと yを/[順に]/プリントする
print(x, y, z)  # x、y、zを/[順に]/プリントする

sep = s  # sを/セパレータに/用いる
end = ''  # 改行が/ない
end = s  # sを/改行の代わりに/用いる
file = file  # fileを/出力先に/用いる
flush = False  # フラッシュを/行わない
flush = True  # フラッシュを/行う

# 組み込み関数（関数）

function = '関数'

callable(x)  # xが/関数かどうか

eval(s)  # s(式)を/評価する -> x
globals()  # グローバル変数の/一覧 -> list

_適用して = '用いて|適用して'
filter(function, x)  # xの各要素にfunctionを適用して、フィルタする -> list
map(function, x)  # xの各要素に/functionを/適用する -> list

# 組み込み関数（オブジェクト）

attrname = '属性|プロパティ'
class1, class2 = 'クラス'

delattr(x, attrname)  # xのattrnameを/削除する
getattr(x, attrname)  # xのattrnameの/値 -> x
hasattr(x, attrname)  # x が/attrnameを/持つかどうか -> bool
setattr(x, attrname, y)  # xのattrnameの値を/yにする

hash(x)  # xのハッシュ値 -> int

isinstance(x, class1)  # xがclass1の/インスタンスかどうか -> bool
issubclass(class1, class2)  # class1がclass2の/サブクラスかどうか -> bool
id(x)  # xのユニークな/識別値 -> int
type(x)  # xの/型 -> type

# int

n, _int, _float = ''

n.bit_length()  # nの二進法表記の/ビット数 -> int
n.to_bytes(x)  # nを/x長のバイト列に/変換する -> bytes
byteorder = "big"  # ビックエンディアンを/用いる
byteorder = "little"  # リトルエンディアンを/用いる
_int.from_bytes(bytes)  # bytes(バイト列)から整数に/変換する -> int

x.is_integer()  # x(浮動小数点数)が/整数かどうか
x.hex()  # x(浮動小数点数)の16進文字列表現 -> str
_float.fromhex(s)  # s(16進文字列表現)を/構文解析する -> float


# string
#
sub = '部分文字列'
suffix = '接尾辞'
prefix = '接頭辞'

string.ascii_letters  # アルファベット -> str
string.ascii_lowercase  # 英小文字 -> str
string.ascii_uppercase  # 英大文字 -> str
string.digits  # 数字 -> str
string.hexdigits  # 16進数字 -> str
string.octdigits  # 16進数字 -> str
string.punctuation  # 記号 -> str
string.printable  # 印刷可能なASCII文字 -> str
string.whitespace  # 空白文字 -> str

str.capitalize()  # strを/キャピタライズする -> str
str.casefold()  # strを/ケースフォルドする -> str

str.center(x)  # strを/幅xで/中央寄せする -> str
str.ljust(x)  # strを/幅xで/右寄せする -> str
str.rjust(x)  # strを/幅xで/左寄せする -> str
fillchar = c  # c(文字)で/埋める

str.count(sub)  # str内のsubの/出現回数

str.encode()  # strを/エンコードする -> bytes
str.endswith(suffix)  # strが/suffixで/終わるかどうか
str.startswith(prefix)  # strが/prefixで/始まるかどうか

str.expandtabs()  # str内のタブを/空白文字で/置き換える -> str
str.expandtabs(n)  # str内のタブを/n文字の空白文字で/置き換える -> str
tabsize = x  # タブは、空白x文字分とする

_見つかる = '見つかる|発見される|出現する'
_内 = '内|の中|中'

str.find(sub)  # str内で、subが/見つかる -> int(位置)
str.find(sub)  # str内で、subが/見つかる -> int(位置)
str.find(sub)  # str内で、subが/最初に/見つかる -> int(位置)
str.find(sub, start)  # str内をstartから探したとき、subが/最初に/見つかる -> int(位置)
str.find(sub, start, end)
# str内をstartからendまで探したとき、subが/最初に/見つかる -> int(位置)

str.find(sub) >= 0  # str内で/subが/見つかるかどうか -> bool
str.find(sub) == -1  # str内で/subが/見つからないかどうか -> bool

str.index(sub)  # str内で/subが/最初に/見つかる -> int(位置)
str.index(sub, start)  # str内をstartから探したとき、subが/最初に/見つかる -> int(位置)
str.index(sub, start, end)
# str内をstartからendまで探したとき、subが/最初に_/見つかる -> int(位置)

str.rfind(sub)  # str内で/subが/最後に/見つかる -> int(位置)
str.rfind(sub, start)  # str内をstartから探したとき、subが/最後に/見つかる -> int(位置)
str.rfind(sub, start, end)
# str内をstartからendまで探したとき、subが/最後に/見つかる -> int(位置)

str.rindex(sub)  # str内でsubが/最後に/見つかる -> int(位置)
str.rindex(sub, start)  # str内をstartから探したとき、/subが/最後に/見つかる -> int(位置)
str.rindex(sub, start, end)
# str内をstartからendまで探したとき、subが/最後に/見つかる -> int(位置)

_フォーマットする = '整形する|フォーマットする'
fmt = 'フォーマット|書式'
fmt.format(x)  # fmtを/xでフォーマットする -> str
fmt.format(x, y)  # fmtに/xと yを/フォーマットする -> str
fmt.format(x, y, z)  # fmtに/x, y, zを/フォーマットする -> str

_アルファベット = "アルファベット|英字"

str.isalnum()  # strが/英数字かどうか
str.isalpha()  # strが/アルファベットかどうか
str.isascii()  # strが/ASCII文字かどうか
str.isdecimal()  # strが/数字かどうか
str.isdigit()  # strが/数字かどうか
str.isidentifier()  # strが/識別子文字かどうか
str.islower()  # strが/英小文字かどうか
str.isnumeric()  # strが/数字かどうか
str.isprintable()  # strが/印字可能かどうか
str.isspace()  # strが/空白かどうか
str.istitle()  # strが/タイトルケース文字列かどうか
str.isupper()  # strが/英大文字かどうか

_ジョインする = '結合する|連結する|ジョインする'

str.join(x)  # xを/strを間に入れて/ジョインする -> str

str.lower()  # strの/英小文字 -> str
str.upper()  # strの/英大文字 -> str

_リプレースする = '置き換える|置換する|リプレースする'
_取り除く = '取り除く|除去する'
_パーティションする = '区切る|分割する|パーティションする'

chars = '文字集合'
str.lstrip()  # strの先頭から/空白を/取り除く -> str
str.lstrip(chars)  # strの先頭から/charsを/取り除く -> str
str.rstrip()  # strの末尾から/空白を/取り除く -> str
str.rstrip(chars)  # strの末尾から/charsを/取り除く -> str
str.strip()  # strの先頭と末尾から/空白を/取り除く -> str
str.strip(chars)  # strの先頭と末尾から/charsを/取り除く -> str


str.partition(sep)  # strを/sepで/パーティションする -> tuple
str.partition(sep)  # strを/末尾から/sepで/パーティションする -> tuple

str.removeprefix(prefix)  # strの先頭から/prefixを/取り除く -> str
str.removesuffix(suffix)  # strの末尾から/suffixを/取り除く -> str

str.replace(sub, s2)  # str内のsubを/全て/s2に/置き換える -> str
str.replace(sub, '')  # str内のsubを/全て/取り除く -> str

_スプリットする = '分割する|分ける|スプリットする'

str.split(sep)  # strを/sepで/スプリットする -> list
str.rsplit(sep)  # strを/sepで/スプリットする -> list
maxsplit = '最大分割回数'

convtable = '変換表'
str.translate(convtable)  # strを/convtableに基づいて/変換する -> str

str.zfill(x)  # strを/幅xになるように/'0'文字で/埋める -> str
