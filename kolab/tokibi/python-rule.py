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

x = y  # yをxと呼ぶ
x % 2 == 0   # xが偶数かどうか
x % 2 == 1   # xが奇数かどうか
x % 2 != 0   # xが奇数かどうか
x % 2 != 1   # xが偶数かどうか
x % y == 0   # xがyの倍数かどうか
x % y == 0   # xがyの倍数でないかどうか
x == y     # xがyに等しいかどうか
x != y     # xがyに等しくないかどうか

_同一 = '同じ|同一'
x is y     # xがyと 同一かどうか
x is not y     # xがyと 同一でないかどうか

_含まれる = '含まれる|ある'
_含まれない = '含まれない|ない'
_内 = '内|の中|中'

x in y     # xがy内に 含まれるかどうか
x not in y     # xがy内に 含まれないかどうか

x ** y  # xのy乗
x | y  # xと yの論理和
x ^ y  # xと yの排他的論理和
x & y  # xと yの論理積
x << n  # xのnビット左シフト
x >> n  # xのnビット右シフト
~x  # xのビット反転

x + y  # x + y
x - y  # x `-` y
x * y  # x × y
x / y  # x / y
x // y  # x / y
x + y + z  # x + y + z
str + x  # {strとxを連結した}文字列
str + x + y  # {str、x、yを連結した}文字列
str * x   # {strをx個、連結した}文字列

_増やす = '増やす|多くする|増加させる'
_減らす = '減らす|少なくする|減少させる'

x += y # xを y[だけ|]増やす
x += 1 # xを 1つ 増やす
x -= y # xを y[だけ|]減らす
x -= 1 # xを 1つ 減らす
x *= y # xを y倍にする
x /= y # xを y分の1にする
x //= y # xを y分の1にする
x /= 2 # xを 半分にする
x //= 2 # xを 半分にする
x **= y # xをy乗にする
x %= y # xをyで割った/余りにする | xをyの徐算の余りにする
x |= y # xをyとの論理和にする
x &= y # xをyとの論理積にする
x ^= y # xをyとの排他論理和にする
x <<= y # xをyビット左にシフトする | xをyビット、左シフトする
x >>= y # xをyビット右にシフトする | xをyビット、右シフトする

x[y] # x[y]
#x[y:z] # x[y:z]

# 組み込み関数（計算）

abs(x)  # xの絶対値
bool(x)  # xが真かどうか
complex(x, y)  # x(実数部), y(虚数部)の複素数 -> complex
divmod(x, y)  # xとyの(商,余り) -> tuple

float(x)  # xの浮動小数点数

int(x)  # {xを変換した}整数値
int(x, n)  # {xを/n進数として変換した}整数値
base = x  # xを基数とする

_コードポイント = '文字コード|コードポイント'

ord(c)  # cのコードポイント

_大きな方 = '大きな値|大きな方|最大値'
_小さな方 = '小さな値|小さな方|最小値'

max(x)  # 数列xの最大値
max(x, y)  # xとyの大きな方
max(x, y, z)  # x, y, zの最大値

min(x)  # 数列xの最小値
min(x, y)  # xとyの小さな方
min(x, y, z)  # x, y, zの最小値

pow(x, y)  # xのy乗
pow(x, y, z)  # {xのy乗をzで剰余した}値

_丸める = '四捨五入する|丸める'
round(x)  # {xを丸めた}整数
round(x, n)  # {xの少数部をn桁[まで|]で丸めた}整数
math.trunc(x)  # {xの少数部を切り捨てた}整数
math.floor(x)  # x以下の最大な整数|{xを切り上げた}整数
math.ceil(x)  # x以上の最小な整数|{xを切り捨てた}整数

# 組み込み関数（文字列）

ascii(x)  # xの印字可能な文字列

bin(x)  # xの2進数文字列
hex(x)  # xの16進数文字列
oct(x)  # xの8進数文字列

chr(c)  # c(コードポイント)の文字
repr(object)  # objectの印字可能な文字列
str(x)  # xの文字列

# 組み込み関数（リスト）

x[y]  # x [ y ]

all(iterable)  # iterableの全てが 真かどうか
any(iterable)  # iterableのいずれかが 真かどうか

enumerate(x)  # xの順序数列 -> list
enumerate(x, y)  # {xのyから始まる}順序数列 -> list
start = x  # startから始まる

_長さ = '長さ|要素数|サイズ|長さ'

iter(x)  # xのイテレータ -> iterable
len(x)  # xの長さ
len(str)  # strの文字数

list(x)  # xのリスト

next(x)  # xの次

range(x)  # 0からxまでの数列
range(x, y)  # xからyまでの数列
range(x, y, z)  # xからyまでの/z間隔の数列
step = x  # 間隔はxにする

reversed(x)  # xの逆順 -> list

set(x)  # xの集合 -> set


_スライス = '部分列|スライス'

slice(x)  # 0からxまでのスライス -> list
slice(x, y)  # xからyまでのスライス -> list
slice(x, y, z)  # xからyまでのzごとによる/スライス -> list

_ソートする = 'ソートする|整列する|ソートする'

sorted(x)  # xをソートする -> list
reverse = False  # 逆順にする
key = x  # xをキーとする

_合計 = '合計値|総和|合計'
_平均 = '平均値|平均'

sum(x)  # x(数列)の合計}整数値
sum(x)/len(x)  # x(数列)の平均}整数値
tuple(x)  # xのタプル -> list

zip(x, y)  # xと yの各要素のペア列 -> list
zip(x, y, z)  # x, y, zの各要素のタプル列 -> list

# 組み込み関数（辞書）

dict, dict2 = '辞書'
key = '項目名|キー'

_エントリ = '項目|エントリ'
_アップデートする = '更新する|アップデートする'

dict(x)  # xの辞書 -> dict

dict[key]  # dictのkey(エントリ) -> x
list(dict)  # dictのキー一覧 -> list
len(dict)  # dictのエントリ数}整数値
dict.clear()  # dictの全てのエントリを消去する
dict.copy()  # dictの[浅い|]コピー -> dict

dict.get(key)  # dictのkey(エントリ) -> x
dict.get(key, x)  # dictのkey(エントリ)か、もし[存在し|]なければ x -> x
dict.items()  # 辞書のエントリ一覧 -> list
dict.keys()  # dictのエントリ一覧 -> list
dict.pop(key)  # {dictのkey(エントリ)を取り出した}値
dict.popitem()  # {dictから最後に追加したエントリを取り出した}値

dict.setdefault(key, x)  # dict内にkey(エントリ)が[存在し|]なければ、そのエントリをxにする -> x

dict.update()  # dictをアップデートする
dict.update(x)  # dictをxでアップデートする

dict.values()  # dictの値一覧

dict | dict2  # {dictとdict2をマージした}辞書
dict |= dict2  # {dictにdict2を加えた}辞書


# 組み込み関数（バイト列、IO）

encoding = 'エンコーディング|文字コード'
errors = 'エラーポリシー'
codepoint = 'コードポイント|文字コード'

bytearray(x)  # xのバイト配列
bytes(x)  # xのバイト列
errors = errors  # エラー処理をerrors(ポリシ)にする
encoding = 'utf-8'  # UTF8を用いる
errors = 'strict'  # エラー処理を厳密にする
#errors = 'ignore'  # エラー処理をしない

prompt = 'プロンプト'
input()  # {入力された}文字列
input(s)  # {s(プロンプト)に対し、入力された}文字列

memoryview(x)  # xのメモリビュー

_オープンする = '開く|オープンする'

open(filename)  # {filenameをオープンした}ファイル
open(filename, 'r')  # {filenameを/読み込みモードでオープンした}ファイル
open(filename, 'w')  # {filenameを/書き込みモードでオープンした}ファイル
open(filename, 'a')  # {filenameを/追加書き込みモードでオープンした}ファイル
mode = 'r'  # 読み込みモードを用いる
mode = 'w'  # 書き込みモードを用いる
mode = 'a'  # 追加モードを用いる
mode = 'b'  # バイナリモードを用いる
mode = 'モード'
newline = '改行コード'
buffering = -1  # バッファリングしない
buffering = x  # バッファリングは/xサイズにする

_プリントする = '表示する|出力する|プリントする'
print()  # 空行をプリントする
print(x)  # xをプリントする
print(x, y)  # xと yを[順に]プリントする
print(x, y, z)  # x、y、zを[順に]プリントする

sep = s  # sをセパレータに用いる
end = ''  # 改行がない
end = s  # sを改行の代わりに用いる
file = file  # fileを出力先に用いる
flush = False  # フラッシュを行わない
flush = True  # フラッシュを行う

# 組み込み関数（関数）

function = '関数'

callable(x)  # xが関数かどうか

eval(s)  # {s(式)を評価した}結果
globals()  # グローバル変数の一覧 

_適用して = '用いて|適用して'
filter(function, x)  # {xを/{functionを適用して}フィルタした}リスト
map(function, x)  # {xにそれぞれfunctionを適用した}リスト

# 組み込み関数（オブジェクト）

attrname = '属性|プロパティ'
class1, class2 = 'クラス'

delattr(x, attrname)  # xのattrnameを削除する
getattr(x, attrname)  # xのattrnameの値
hasattr(x, attrname)  # x がattrnameを持つかどうか
setattr(x, attrname, y)  # xのattrnameの値をyにする

hash(x)  # xのハッシュ値}整数値

isinstance(x, class1)  # xがclass1のインスタンスかどうか
issubclass(class1, class2)  # class1がclass2のサブクラスかどうか
id(x)  # xのユニークな識別値
type(x)  # xの型

# int

n, _int, _float = ''

n.bit_length()  # nの二進法表記のビット数
n.to_bytes(x)  # {整数nを変換した}xビット長のバイト列
byteorder = "big"  # ビックエンディアンを用いる
byteorder = "little"  # リトルエンディアンを用いる
_int.from_bytes(bytes)  # {bytes(バイト列)から変換した}整数

x.is_integer()  # x(浮動小数点数)が整数かどうか
x.hex()  # x(浮動小数点数)の16進文字列表現
_float.fromhex(s)  # {16進数のsから構文解析した}浮動点少数


# string
#
sub = '部分文字列'
suffix = '接尾辞'
prefix = '接頭辞'

string.ascii_letters  # アルファベット
string.ascii_lowercase  # 英小文字
string.ascii_uppercase  # 英大文字
string.digits  # 数字
string.hexdigits  # 16進文字列
string.octdigits  # 8進文字列
string.punctuation  # 記号
string.printable  # 印刷可能なASCII文字
string.whitespace  # 空白文字

str.capitalize()  # {strをキャピタライズした}文字列
str.casefold()  # {strをケースフォルドした}文字列

str.center(x)  # {strを幅xで中央寄せした}文字列
str.ljust(x)  # {strを幅xで右寄せした}文字列
str.rjust(x)  # {strを幅xで左寄せした}文字列
fillchar = c  # c(文字)で埋める

str.count(sub)  # str内のsubの出現回数

str.encode()  # {strから変換された}バイト列
str.endswith(suffix)  # strがsuffixで終わるかどうか
str.startswith(prefix)  # strがprefixで始まるかどうか

str.expandtabs()  # {str内のタブ文字を/空白文字で置き換えた}文字列
str.expandtabs(n)  # {str内のタブ文字を/n文字の空白文字で置き換えた}文字列
tabsize = x  # タブは、空白x文字分とする

_見つかる = '見つかる|発見される|出現する'
_内 = '内|の中|中'

str.find(sub)  # {str内で/subが見つかった}位置
str.find(sub)  # {str内で/subが見つかった}位置
str.find(sub)  # {str内で_subが/最初に見つかった}位置
str.find(sub, start)  # {{str内を/startから探した}とき、subが/最初に/見つかった}位置
str.find(sub, start, end)
# {{str内を/startからendまで探した}とき、subが/最初に/見つかった}位置

str.find(sub) >= 0  # {str内で/subが見つかる}かどうか
str.find(sub) == -1  # {str内で/subが見つからない}かどうか

str.index(sub)  # {str内で/subが最初に見つかった}位置
str.index(sub, start)  # {{str内を/startから探した}とき、subが/最初に見つかった}位置
str.index(sub, start, end)
# {{str内を/startからendまで探した}とき、subが/最初に見つかった}位置

str.rfind(sub)  # {str内でsubが最後に見つかった}位置
str.rfind(sub, start)  # {{str内をstartから探した}とき、subが最後に見つかった}位置
str.rfind(sub, start, end)
# {{str内をstartからendまで探した}とき、subが最後に見つかった}位置

str.rindex(sub)  # {str内でsubが最後に見つかった}位置
str.rindex(sub, start)  # {{str内をstartから探した}とき、subが最後に見つかった}位置
str.rindex(sub, start, end)
# {{str内を/startからendまで探した}とき、subが最後に見つかった}位置

_フォーマットする = '整形する|フォーマットする'
fmt = 'フォーマット|書式'
fmt.format(x)  # {fmtをxでフォーマットした}文字列
fmt.format(x, y)  # {fmtにxと yをフォーマットした}文字列
fmt.format(x, y, z)  # {fmtにx, y, zをフォーマットした}文字列

_アルファベット = "アルファベット|英字"

str.isalnum()  # strが英数字かどうか
str.isalpha()  # strがアルファベットかどうか
str.isascii()  # strがASCII文字かどうか
str.isdecimal()  # strが数字かどうか
str.isdigit()  # strが数字かどうか
str.isidentifier()  # strが識別子文字かどうか
str.islower()  # strが英小文字かどうか
str.isnumeric()  # strが数字かどうか
str.isprintable()  # strが印字可能かどうか
str.isspace()  # strが空白かどうか
str.istitle()  # strがタイトルケース文字列かどうか
str.isupper()  # strが英大文字かどうか

_ジョインする = '結合する|連結する|ジョインする'

str.join(x)  # {xの間に{strを入れて}ジョインした}文字列

str.lower()  # strの英小文字
str.upper()  # strの英大文字

_リプレースする = '置き換える|置換する|リプレースする'
_除去する = '取り除く|除去する'
_パーティションする = '区切る|分割する|パーティションする'

chars = '文字集合'
str.lstrip()  # {strの先頭から/空白を除去した}文字列
str.lstrip(chars)  # {strの先頭から/charsを除去した}文字列
str.rstrip()  # {strの末尾から/空白を除去した}文字列
str.rstrip(chars)  # {strの末尾から/charsを除去した}文字列
str.strip()  # {strの先頭と末尾から/空白を除去した}文字列
str.strip(chars)  # {strの先頭と末尾から/charsを除去した}文字列


str.partition(sep)  # {strを/sepでパーティションした}タプル
str.partition(sep)  # {strを/末尾から/sepでパーティションした}タプル

str.removeprefix(prefix)  # {strの先頭から/prefixを取り除いた}文字列
str.removesuffix(suffix)  # {strの末尾から/suffixを取り除いた}文字列

str.replace(sub, s2)  # {str内のsubを/全て/s2に置き換えた}文字列
str.replace(sub, '')  # {str内のsubを/全て/取り除いた}文字列

_スプリットする = '分割する|分ける|スプリットする'

str.split(sep)  # {strを/sepでスプリットした}文字列リスト
str.rsplit(sep)  # {strを/sepでスプリットした}文字列リスト
maxsplit = '最大分割回数'

convtable = '変換表'
str.translate(convtable)  # {strを/convtableで変換した}文字列

str.zfill(x)  # {strを/{幅xになる}ように'0'文字で埋めた}文字列
