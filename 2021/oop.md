
\chapter{オブジェクト指向}

まずは、データ構造を表現する手法として
**\OOP**{object-oriented programming}を導入して学んでいきます。

## データ構造

Python は、今まで学んだきた通り、便利なデータ型を提供してくれます。

* **論理値**{\Tx{bool}}: `True`, `False`
* **整数**{\Tx{int}}
* **浮動少数点数**{\Tx{float}}
* **文字列**{\Tx{str}}

ところが、世の中のデータは、
これらのデータ型だけで**十分に**表現できるものではありません。

### 例: xy平面上の点



xy平面上の点を考えてみましょう。

点$P$のx座標, y座標はそれぞれ浮動小数点数で表現できますが、
px, py のように変数が２つ必要になります。
点としては**２つの値の組**として、
１つの変数でひとまとまりで扱いたくなります。


\begin{center}
\includegraphics[width=0.20\paperwidth]{./figs/xy.pdf}
\end{center}

<div class="alert alert-info">

データ構造

複数の値からなるデータをひとつの変数から扱えるようにすること
</div>

### データ構造: タプル

Pythonは、既にご存知のとおり、
**リスト**や**タプル**などの複数の値をまとめて扱うデータ構造があります。

\Run{データ構造なし}
```py
px = 1
py = 2
qx = 2
qy = 3
print(f'P座標 ({px}, {py})')
print(f'Q座標 ({qx}, {qy})')
```
\Out
```py
P座標 (1, 2)
Q座標 (2, 3)
```
\Run{データ構造(タプル)版}
```py
p = (1, 2)
q = (2, 3)


print(f'P座標 ({p[0]}, {p[1]})')
print(f'Q座標 ({q[0]}, {q[1]})')
```
\Out
```py
P座標 (1, 2)
Q座標 (2, 3)
```

平面上の点は、x座標とy座標で高々２つの値しか含まれていませんが、
x座標とy座標がバラバラにならないように、
**まとまったデータ**として扱った方が便利です。

しかし、タプルを平面上の点に流用すると問題も発生します。

* x,y座標を直感的に操作しにくい\\
以下は、何を計算しているのでしょうか？
```py
sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2))
```
* 点p,q を加算したら、$(3, 3)$とならない
```py
p+q
```
```py
(1, 2, 2, 1)
```

平面座標上の点$(x, y)$を表現するための、
**より目的に特化したデータ構造**があるといいと思いませんか？

<div class="alert alert-info">

オブジェクト指向言語

目的にあったデータ構造を定義する機能を提供
</div>

## クラスとオブジェクト


{\OOP}は：

* **クラス**{class}と呼ばれる単位でデータを設計する
* クラスから**インスタンス化**することでデータ構造（値）を作る


\begin{center}
\includegraphics[width=0.30\paperwidth]{./fig/class0.pdf}
\end{center}

<div class="alert alert-info">

オブジェクト

クラスから作られたデータのことを**オブジェクト**{object}と呼ぶ
</div>

### クラス定義: 例 Point クラス

まずは、先ほどの平面上の点(x,y)を表す Point クラスを作ってみましょう。

* x座標とy座標の値は、**プロパティ**と呼ばれる変数に記録する
* （プロパティを初期化する）コンストラクタ（`__init__`）を作る
* コンストラクタは、
クラスからインスタンス化する（オブジェクトを生成する）ときに用いられる

\Run{初めてのクラス定義}
```py
class Point(object):
x: int                 # プロパティ x の定義 (省略可)
y: int                 # プロパティ y の定義 (省略可)

def __init__(self, x, y):
self.x = x
self.y = y

```

クラス定義自体は、変数定義や関数定義と同じく、実行結果は表示されません。
ただし、クラス名 {\tt Point} は環境に登録されて使えるようになります。

\Run{クラス定義の確認}
```py
Point
```
\Out
```py
__main__.Point
```

### インスタンス化

{\tt Point} クラスは、平面上の(x,y)を表すことを意図した**データ構造の設計図**です。
{\tt Point} クラス自体は、何らかの具体的な値をもった**実体のある**データではありません。

<div class="alert alert-info">

インスタンス化

クラスに対し、実体のあるデータを生成する操作\\
生成されたデータは、**インスタンス**{実体, instance}、もしくはオブジェクトと呼ぶ。
</div>

Python では、インスタンス化は、クラス名を関数名として呼ぶことで行います。
インスタンス化すると、xy平面上の値をもったオブジェクトとして利用できるようになります。

\Run{P, Qのインスタンス化}
```py
p = Point(1, 2)
q = Point(2, 3)

print(f'P座標 ({p.x}, {p.y})')
print(f'Q座標 ({q.x}, {q.y})')
```
\Out
```py
P座標 (1, 2)
Q座標 (2, 3)
```

\vspace{-1cm}
\begin{lbox}{プロパティへのアクセス}

プロパティは、変数として参照と代入できます。

\begin{tabular}{ll}
{\tt o.x } & オブジェクト{\tt o}のプロパティ{\tt x}の値を得る\\
{\tt o.x = y } & オブジェクト{\tt o}のプロパティ{\tt x}に {\tt y}を代入する
\end{tabular}

\end{lbox}

\begin{lbox}{x のクラスを確認する方法}

* `type(x)`: クラス名を得る
* `isinstance(x, C)`: x はクラスCのインスタンスか判定する

\Run{type(p) }
```py
type(p)
```
\Out
```py
__main__.Point
```
\Run{isinstance(p, Point)}
```py
isinstance(p, Point)
```
\Out
```py
True
```
\end{lbox}


### 点P,Qの中間点を求める

練習で2つの点の中間点を関数を定義してみましょう。

\hr
\HBold{例題}　点P, Qの中間点を求める関数`mid(p,q)`を定義せよ

\hr

関数`mid(p,q)`は、座標を計算したあと、
新しく{\tt Point クラス}をインスタンス化して、{\tt Point}オブジェクトとして返すようにします。

\Run{中間点を求める関数}
```py
def mid(p, q):
mx = (p.x + q.x) / 2
my = (p.y + q.y) / 2
return Point(mx, my)

```

\Run{2点の中間点を求める}
```py
p = mid(Point(2, 2), Point(4, 4))

print(f'中間座標 ({p.x}, {p.y})')
```
\Out
```py
中間座標 (3.0, 3.0)
```

<div class="alert alert-info">

Let's try

２点間の距離を求める{\tt distance(p, q)}も定義してみよう。
</div>

## クラスとメソッド

メソッドは、**オブジェクトに対する操作**を記述する**関数**です。
メソッドを定義すると、オブジェクトが**ますます便利に**使えるようになります。

まずは、先ほどの\texttt{mid(p,q)}関数をメソッドにしてみます。
メソッド化の方法は、クラス内のブロック内に関数定義を移動させ、
全体的をインデントを下げることを忘れないで、関数の第一引数を{\tt self}に変更します。

```py
class Point(object):
x: int                 # 省略してもよい
y: int                 # 省略してもよい
def __init__(self, x, y):
self.x = x
self.y = y

def mid(self, q):   # 先ほどのmid(p,q)のメソッド化
mx = (self.x + q.x) / 2
my = (self.y + q.y) / 2
return Point(mx, my)

```

**メソッドの定義**
* クラス定義(class)内で定義する
* 操作の**対象となるオブジェクト**は**自分自身({\tt self**)}で参照する（自己参照）
* Pythonでは、メソッドは**常に第一引数に{\tt self**を指定する}

<div class="alert alert-info">

メソッドにすると

\texttt{mid(p,q)}の代わりに、{\Large \texttt{p.mid(q)}} のように書ける\\
'{\tt p.mid(q)}の`p`がメソッド定義の`self`に相当する）
</div>

\Run{2点の中間点（メソッド版）}
```py
p = Point(2, 2)
q = Point(4, 4)
p = p.mid(q)

print(f'中間座標 ({p.x}, {p.y})')
```
\Out
```py




中間座標 (3.0, 3.0)
```

クラス定義では、自己参照 \texttt{self}の意味が最も理解しにくいところです。
{\Colab}は試してみるのに優れた環境なので、何度かメソッドを書いてみてください。
多くの学生が何度か書いたら、**「突然わかる」ようになっています。**

<div class="alert alert-info">

Let's try

２点間の距離を求める{\tt distance(p, q)}もメソッドとして定義してみよう。
</div>

### オブジェクトの表示： \CC{__repr__

Python では、`__repr__(self)`というメソッド名は、
オブジェクトの内部を表示のための特別なメソッド名になっています。

```py
class Point(object):
x: int                 # プロパティ x の定義 (省略可)
y: int                 # プロパティ y の定義 (省略可)
def __init__(self, x, y):
self.x = x
self.y = y

# 以下を追加する
def __repr__(self):
return f'({self.x}, {self.y})'

```

オブジェクトの内部状態を文字列として返すように
`__repr__(self)`を定義すると、{\tt Point}オブジェクトが表示されるようになります。

**`__repr__`の定義前 **
```py
Point(1, 2)
```
```py
<__main__.Point object
at 0x106282f40>
```
**`__repr__`の定義後**
```py
Point(1, 2)
```
```py
(1, 2)
```

<div class="alert alert-info">

クラスを定義したら：

`__repr__(self)`を定義しておくと、開発がしやすくなる
</div>

## 空間上の点を表現する

ここまでの練習として、空間上の点を表現するクラスを定義してみましょう。

\hr
\HBold{例題}　空間上の点$(x,y,z)$を表現するクラスを定義せよ。
また、２点間の中間点({\tt mid})と距離({\tt distance})を求めるメソッドも定義せよ。

\hr

クラス名は、平面上の点({\tt Point})と重ならないように、
{\tt Point3}として定義しておきましょう。

まずは答えを見ずに自力で定義してみましょう。
正しく定義できたら、{\tt Point}と{\tt Point3}は、それぞれ、次のように動作するはずです。

**2次元 **
```py
p = Point(1, 2)
q = Point(2, 3)
print(p)
```
```py
(1, 2)
```
\Run{中間点}
```py
p.mid(q)
```
```py
(2.0, 3.5)
```
\Run{距離}
```py
p.distance(q)
```
```py
1.4142135623730951
```
**3次元**
```py
p = Point3(1, 2, 3)
q = Point3(2, 3, 4)
print(p)
```
```py
(1, 2, 3)
```
\Run{中間点}
```py
p.mid(q)
```
```py
(2.0, 3.5, 5.0)
```
\Run{距離}
```py
p.distance(q)
```
```py
1.7320508075688772
```

<div class="alert alert-info">

Let's try

まずは、次のページを見ないで定義してみて
</div>


\Run{{\tt Point3}の定義例}
```py
import math

class Point3(object):
x: int
y: int
z: int
def __init__(self, x, y, z):
self.x = x
self.y = y
self.z = z

def __repr__(self):
return f"({self.x}, {self.y}, {self.z})"

def mid(self, q):
x = (self.x + q.x) / 2
y = (self.y + q.y) / 2
z = (self.z + q.z) / 2
return Point3(x, y, z)

def distance(self, q):
dx = self.x - q.x
dy = self.y - q.y
dz = self.z - q.z
return math.sqrt(dx**2 + dy**2 + dz**2)

```

### 動的束縛

クラス{\tt Point}と{\tt Point3}を比較したとき、注目したいところはメソッド名です。
同じメソッド名が使えて、しかも**クラスごとに異なる処理**を行わせています。
さらに、注目して欲しいのは、２次元版も３次元版も全く同じコード({\tt p.distance(q)})で距離を求めています。

<div class="alert alert-info">

2次元？3次元？どちらのメソッド？

{\Large {\tt p.distance(q)}}
</div>

{\OOP}の大きな特徴に**動的束縛**{dynamic binding}という機構があります。
これは、実行時に、**クラスの種類によって呼び出すメソッドを実行時に決定してくれる**ものです。
実は、**実は{\tt if**文などの条件分岐と等価な役割を果たしています。}\\

\Run{もし関数でdistance(p, q)を書いたら}
```py
def distance(p, q):
if isinstance(p, Point):
dx = p.x - q.x
dy = p.y - q.y
return math.sqrt(dx ** 2 + dy ** 2)
if isinstance(p, Point3):
dx = p.x - q.x
dy = p.y - q.y
dz = p.z - q.z
return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
```

<div class="alert alert-info">

\tt isinstance(x, c)

x が クラス c のインスタンスであるか判定する

** 整数(int) **
```py
isinstance(1, int)
```
```py
True
```
** 文字列(str) **
```py
isinstance("1", int)
```
```py
False
```
</div>

動的束縛を活かしたプログラミングは、
次回、**ポリモーフィズム**としてさらに詳しく取り上げます。

## 演算子オーバーロード

\if0
Python では、`__repr__`のように、
`__`で始まるメソッドは、特殊な意味をもったメソッドになっています。

その中のいくつかは、演算子の役割をはたすメソッドになっています。

\begin{center}
\begin{tabular}{lr}
メソッド名 &  演算 \\
`__add__(self, y)` &  `x + y` \\
`__sub__(self, y)`    & `x - x` \\
`__mul__(self, y)`    & `x * x` \\
`__truediv__(self, y)`    & `x / x` \\
\end{tabular}\\

\end{center}
\fi


**演算子オーバーロード**{operator overloading}とは、
**特殊なメソッドを定義することで、演算子を再定義する**{\OOP}の機能です。
まず、Pythonにおいて、そもそも演算子がどのように実装されているか、
確認するところから始めましょう。

Python は、純粋な{\OOP}言語なので、
**全ての値はオブジェクト**になっており、操作はメソッドで行われます。

だから、\fbox{\LARGE $1 + 2$} という式は:

* 整数 1, 2 は、クラス`int`のオブジェクト
* 加算は、`(1).__add__(2)` という特別なメソッドの処理

毎回\texttt{(1).\_\_add\_\_(2)} のように書くのはつらいので、
糖衣構文として\texttt{1+2}が用意されています。

<div class="alert alert-info">

糖衣構文(syntax sugar)

機械的に置き換えられる簡易記法\\
\begin{tabular}{lcllcl}
`x + y` & {\color{red} $\Rightarrow$} & `x.__add__(y)` &
`x == y` & {\color{red} $\Rightarrow$} & `x.__eq__(y)` \\

`x - y` & {\color{red} $\Rightarrow$} & `x.__sub__(y)` &
`x != y` & {\color{red} $\Rightarrow$} & `x.__ne__(y)` \\

`x * y` & {\color{red} $\Rightarrow$} & `x.__mul__(y)` &
`x < y` & {\color{red} $\Rightarrow$} & `x.__lt__(y)` \\

`x / y` & {\color{red} $\Rightarrow$} & `x.__truediv__(y)` &
`x <= y` & {\color{red} $\Rightarrow$} & `x.__le__(y)` \\

`x // y` & {\color{red} $\Rightarrow$} & `x.__floordiv__(y)` &
`x > y` & {\color{red} $\Rightarrow$} & `x.__gt__(y)` \\

`x % y` & {\color{red} $\Rightarrow$} & `x.__mod__(y)` &
`x >= y` & {\color{red} $\Rightarrow$} & `x.__ge__(y)` \\
\end{tabular}\\
(これ以外のもたくさんあります)\\
\URL{https://docs.python.org/ja/3/library/operator.html}
</div>

だから、`__add__(self, y)`を定義すれば、
加算の演算子が使えるようになります。

### 点P,Qをベクトルとして加算する

\hr
\HBold{例題}
P, Qをベクトルとして加算できるようにしてみよう。

\hr

{\tt Point3}クラスに、以下のメソッドを追加します。

```py
class Point3(object):

... # 以下を追加する
def __add__(self, a):
x = self.x + a.x
y = self.y + a.y
z = self.z + a.z
return Point3(x, y, z)

```

\Run{点の(ベクトルとしての)加算}
```py
p = Point3(1, 2, 3)
q = Point3(2, 3, 4)

p + q
```
\Out
```py
(3, 5, 7)
```

<div class="alert alert-info">

Let's try

演算子オーバーロードは、次のコースワークで練習してみましょう。
</div>

\section*{コースワーク：有理数}

\HBold{課題}有理数をクラスで定義する


\begin{enumerate}
***有理数クラス Q を定義する** (クラス名は、\UTT{Q} とする)

<div class="alert alert-info">

有理数

二つの整数 $a,b$ （ただし $b$ は $0$ でない）をもちいて $a/b$ という分数で表せる数.

b = 1 とすることにより、任意の整数は有理数となる.

\[
\mathbb{Q} = \left\{{a \over b} \mid a, b \in \mathbb{Z}, b\ne 0\right\}
\]

</div>

***有理数をインスタンス化し表示できるようにする**

```py
q = Q(1, 2)
q
```
```py
1/2
```

***約分も忘れずに**
\[
{n \over m}={b\times d \over a\times d}={b \over a}
\]

```py
Q(2, 4)
```
```py
1/2
```

***分母が1のときは省略できるようにする**
```py
Q(3)
```
```py
3
```

<div class="alert alert-info">

引数の初期値

関数やメソッドを定義するとき、初期値を与えると、省略可能になる
```py
def init(a=0, b=1):
```
</div>

* **メソッド add で２つの有理数オブジェクト加算できるようにする**
```py
q1 = Q(1, 2)
q2 = Q(1, 3)
q1 + q2
```
```py
5/6
```

* **四則演算を全部サポートする**
\[
{a \over b} + {c \over d} = {ad + bc \over bd},\quad {a \over b} \times {c \over d} = {ac \over bd}
\]
\[
{a \over b}-{c \over d}={a \over b}+\left(-{c \over d}\right)={ad-bc \over bd},\quad {a \over b}\div {c \over d}={a \over b}\times \left({c \over d}\right)^{{-1}}={ad \over bc}
\]

```py
q1 = Q(1, 2)
q2 = Q(1, 3)
q1 - q2
```
```py
1/6
```


***(上級者向け) 有理数の演算に整数を混ぜられるようにする**

```py
q = Q(1, 2)
q / 2
```
```py
1/4
```

* ヒント:  \Google{\texttt{isinstance()}} を用いる

\end{enumerate}

<div class="alert alert-info">

コースワーク

（無理にならない範囲で)できるところまで取り組んでください。\\
(manabaの感想でわからなかったところを報告して頂ければ十分です)
</div>


\chapter{クラス継承}

実世界でモデル化して、
より複雑なプログラムを開発する
オブジェクト指向設計手法について学びます。

## オブジェクト指向とは

そもそも、オブジェクト指向プログラミングとは、

* 全てを**オブジェクト**{object} と考える
* プログラムは、オブジェクト間の**メッセージ通信**{message} と考える

だから、$1 + 2$ という数式であっても：
* **1 というオブジェクト**への通信
* **\_\_add\_\_(2)** というメッセージを送る
* 計算 3 が返信される
\begin{center}
\includegraphics[width=0.40\paperwidth]{./fig/ooadd.pdf} \\
\texttt{(1).\_\_add\_\_(2) とオブジェクト通信}
\end{center}

<div class="alert alert-info">

オブジェクト指向的な考え方

プログラムをオブジェクトとメッセージのやり取りとみなす
</div>

## オブジェクト指向設計法

オブジェクト（事物）の性質を考え、**抽象化**{abstraction}します。

* どのようなメッセージのやりとりがあるか？
* どのような状態を用いうる化

<div class="alert alert-info">

抽象化

不要な情報を捨てて、より本質のみ焦点を当てること
</div>

ここでは、カウンターを例に考えます。カウンターをイメージしてください。

* カウンターとは、どのような情報のやりとりがありますか？
* これは、メソッドの設計になる
* カウンターの内部には、どのような情報がありますか？
* これは、プロパティの設計になる

\begin{center}
\includegraphics[width=0.60\paperwidth]{./fig/class1.pdf}
\end{center}

<div class="alert alert-info">

インターフェース

オブジェクトと外部間で情報をやりとりをするメソッドのこと\\
ソフトウェアの設計でもっとも重要な概念となる
</div>

### UMLクラス図

クラス設計は、どのオブジェクト指向プログラミングであっても、
基本的に共通です。
プログラミングに依存せず、クラス設計を図示する手法として、
UMLクラス図があります。

\begin{center}
\includegraphics[width=0.25\paperwidth]{./figs/UMLclass.pdf} \\
(UML クラス図)
\end{center}

大規模なソフトウェア開発では、
まずUMLクラス設計図を用いてクラス設計だけ先に行うことがあります。
もちろん、UMLクラス図を用いず、
Pythonなどのプログラミング言語で直接、
ソースコードで設計することもあります。

### クラス定義を定義する

Counter クラスの設計に基づいて、Python クラスを定義してみよう。

\begin{center}
\includegraphics[width=0.35\paperwidth]{./figs/UMLclass.pdf} \\
(UML クラス図)
\end{center}
\Run{Counterの定義}
```py
class Counter(object):
cnt : int
def __init__(self):
self.cnt = 0

def count(self):
self.cnt += 1

def reset(self):
self.cnt = 0

def show(self):
print(self.cnt)

```

オブジェクト指向プログラミングでは、**クラス設計**が重要になります。
クラス設計がしっかりしていれば、各メソッドの実装は意外と簡単です。
大規模なソフトウェア開発では、クラス設計とメソッド開発は分業して行うことも少なくありません。

### カウンタ・プログラム

インスタンス化の練習を兼ねて、{\OOP}を練習しておきましょう。

\hr
\HBold{（例題）}
1から$n$までの整数のうち、
3の倍数、5の倍数の数を数える関数`stat_fz(n, c, d)`を定義せよ。
なお、`c`, `d`はそれぞれ、3の倍数、5の倍数を数える`Counter`とする。

\hr

FizzBuzz と同じ原理なので、詳しい解説は入らないでしょう。

\Run{関数定義}
```py
def stat_fz(n, c, d):
for i in range(1, n+1):
if i % 3 == 0:
c.count()
if i % 5 == 0:
d.count()
```


\Run{100まで数える}
```py
c = Counter()
c2 = Counter()
stat_fz(100, c, c2)
c.show()
c2.show()
```

\Out
```py
33
20
```

<div class="alert alert-info">

考えてみよう

5の倍数を２重に数えたいときは、どう直したらいいのだろうか？\\
(一切`stat_fz(n, c, d)`関数を直さない方法があります。)
</div>


## クラス継承

**クラス継承**{class inheritance}は、
オブジェクト指向プログラミングの効率を向上させる手段です。
難解な概念がありますが、まずは操作的意味論による解釈で理解していきましょう。

<div class="alert alert-info">

（操作的意味論による解釈）クラス継承

新しいクラスを定義するとき、既存のクラスから拡張すること
</div>


まず用語からおさえておきましょう。\\

オブジェクト指向言語では、継承元のクラスのことを**スーパークラス**{super class}、もしくは**親クラス**{parent class}、
継承されたクラスのことを**サブクラス**{subclass}、もしくは**子クラス**{child class}と呼びます。


\begin{center}
\includegraphics[width=0.40\paperwidth]{./figs/UMLextend.pdf} \\
(UML クラス継承)
\end{center}

<div class="alert alert-info">

サブクラスは

* スーパークラスの**プロパティとメソッドをそのまま使うことができる**
* 新しくプロパティやメソッドを追加することができる
* スーパークラスのメソッドを異なる処理をするように書き換えることができる
* ただし、スーパークラスのプロパティとメソッドを取り除くことは\Bou{できない}
</div>

### クラス継承

これも具体例を考えながらみていきましょう。
ここでは、1回の{\tt count()}操作で、2回カウントする{\tt DoubleCounter} クラスを考えます。

もし今まで通りクラスを定義すると、左の{\tt DoubleCounter} クラスになります。
一方、右の{\tt DoubleCounter} クラスはクラス継承を用いたバージョンになります。

**今まで通り**
```py
class DoubleCounter(object):
cnt : int
def __init__(self):
self.cnt = 0

def count(self):
self.cnt += 2

def reset(self):
self.cnt = 0

def show(self):
print(self.cnt)

```
**Counter からの継承**
```py
class DoubleCounter(Counter):
def count(self):
self.cnt += 2
```

<div class="alert alert-info">

注目

**{\tt count()**メソッドだけ}を定義しています。\\
他のメソッドやプロパティは{\tt Counter} クラスをそのまま使うことができます。
</div>

さて、どちらの{\tt DoubleCounter}クラスも同じように使えます。

```py
c = DoubleCounter()
c.count()
c.show()  # 2と表示される。
```

<div class="alert alert-info">

考えてみよう

どちらがコーディングの効率がよいのだろうか？
</div>

オブジェクト指向プログラミングでは、
クラス継承を活用することで、
**既存のクラスを再利用して効率よくクラスを定義できる**ようになります。

### ポリモーフィズム(多相性)

もしコーディングの効率を気にしないのであれば、
クラス継承を無理に使わなくても良い気がしたかもしれません。
本当に使わなくても良いのでしょうか？
実は、クラス継承には、ポリモーフィズムという**効率より優れた効果**があります。

<div class="alert alert-info">

クイズ

`stat_fz(n,c,d)`を一切、変更することなく、
５の倍数だけ２重にカウントするにはどうすればいいのでしょう。

```py
def stat_fz(n, c, d):
for i in range(1, n+1):
if i % 3 == 0:
c.count()
if i % 5 == 0:
d.count()
```

</div>

\HBold{ヒント} `DoubleCounter`を使います。

```py
c = Counter()
c2 = DoubleCounter()
stat_fz(100, c, c2)
c.show()
c2.show()
```

\Out
```py
33
40
```

{\tt DoubleCounter} カウンタは、
**{\tt Counter**クラスの一種}なので、{\tt Counter}クラスの代わりに使うことができます。
なぜ、代わりに使ってよいのかといえば、
**サブクラスはスーパークラスのプロパティやメソッドを全てもっている**からです。

<div class="alert alert-info">

型理論：部分型

サブクラス (D)は、スーパークラス(C)の部分型$D <:C$である。\\
部分型$D <:C$が成り立つとき、$C$型の代わりに$D$型を使っても**型エラー**にならない。
</div>

クラス継承を用いると、部分型であることが保証されます。
だから、安全にクラスを切り替えて、プログラムの動作を変えることができるようになるわけです。

### 型安全性

\hr
\HBold{（例題）}
`stat_fz(n,c, d)`を一切、変更することなく、
３の倍数をカウントしないで済むように、{\tt DummyCounter} クラスを定義せよ。

```py
def stat(n, c, d):
for i in range(1, n+1):
if i % 3 == 0:
c.count()
if i % 5 == 0:
d.count()
```

\hr

数をカウントしないためには、{\tt Counter}クラスを継承して、
数を数えないカウンタクラスを定義してあげればよいことになります。
クラス継承では{\tt count()}メソッドは取り除くことできないので、
代わりに空の何もしないメソッドとして定義します。

**DummyCounter**
```py
class DummyCounter(Counter):
def count(self):
#何もしない
pass
```
**ありがちな失敗**
```py
class DoubleCounter2(object):
def show(self):
print(0)
```

ありがちな失敗は、何もしなから要らないだろうと、`count()`メソッドを消してしまうことです。
`count()`を消してしまえば、**型エラー**になってしまいます。

\if0
\begin{center}
\includegraphics[width=0.40\paperwidth]{./figs/UMLCounter.pdf} \\
({\tt Counter}, {\tt DoubleCounter}, {\tt EmptyCounter} )
\end{center}
\fi

オブジェクト指向プログラミング言語では、サブクラスは常に部分型になります。
これによって、型安全性が保たれています。

<div class="alert alert-info">

型安全性

**型エラー**{type error}が発生しないことが保証される
</div>

\section*{コースワーク： 数式}

\hr
\HBold{問題} 数式（四則演算）をクラスで定義し計算する

\hr

\HBold{ヒント1} 数式は**「計算できるオブジェクト」**とモデル化して考える。
「計算できる」というのは、「計算する」メソッドをもつことになる。
「計算する」メソッドは、プログラミング用語の**評価**{evaluation}からとって、
`eval()`としてみよう。

<div class="alert alert-info">

式オブジェクト {\tt e

{\tt \Large e.eval()} が数値を返せばよい
</div>

\HBold{ヒント２} クラス階層は次の通りにするとよい（かも）

\begin{center}
\includegraphics[width=12cm]{figs/UMLExpr.pdf}
\end{center}

\vspace{1cm}

\begin{enumerate}
***{\tt Expr**クラスを定義する}\\
抽象クラスなので、`eval()`メソッドはとりあえず0を返しておきましょう。

```py
e = Expr()
e.eval()
```
```py
0
```

***{\tt Number**クラスを定義する}\\
数値なので、`eval()`メソッドはそのままの値を返します。

```py
e = Number(1)
e.eval()
```
```py
1
```

```py
e = Number(9)
e.eval()
```
```py
9
```

***{\tt Add**クラスを定義する}\\
足し算なので、`eval()`メソッドは和を返します。

```py
e = Add(1, 2)
e.eval()
```
```py
3
```

<div class="alert alert-info">

希望

ここまでは自力でできて欲しいです\\
以下、何気に激ムズの予感.
</div>

***$1+2+3$も計算してみよう**\\
足し算なので、`eval()`メソッドは和を返します。

```py
e = Add(1, Add(2, 3))
e.eval()
```
```py
6
```

\HBold{ヒント}: いきなりは難しいので、まずこちらを動くようにしてみましょう。

```py
e = Add(Number(1), Number(2))
e.eval()
```
```py
3
```

<div class="alert alert-info">

考えてみてね

なぜ{\tt Number}クラスを定義したのか？\\
(答えを確かめたいときは、Zoomで質問してください)
</div>

***(あとは蛇足気味だけど,)引き算、掛け算、割り算も**

```py
e = Add(1, Mul(2, 3))
e.eval()
```
```py
7
```

\end{enumerate}



<div class="alert alert-info">

コースワークについて

（無理にならない範囲で)できるところまで取り組んでください。\\
(manabaの感想でわからなかったところを報告して頂ければ十分です)
</div>


\if0
そして、部分型の型安全性が保証されるので、
利用者はクラスを新しく定義して、プログラムを書くことができます。
このとき、メソッドの処理を変えれば、異なるプログラム動作が実現されます。
このような性質を**ポリモーフィズム**{polymorphism, 多態性, 多相性}と呼びます。

## クラス階層とデザインパターン

最後に、クラス階層（クラスの親子関係）は、どのように設計したら良いのでしょうか？

まず、オブジェクト指向プログラミングが登場した初期に考えられたことは、
実世界の概念関係や分類構造をそのまま反映できる、少なくとも反映しやすいと考えられてきました。
しかし、オブジェクト指向プログラミングが普及して、開発経験が蓄積されると、
クラス階層を設計するのは難しいとわかってきました。

**デザインパターン**{design pattern}は、
過去のソフトウェア設計者が発見し編み出した設計ノウハウを蓄積し、
名前をつけ、再利用しやすいように特定の規約に従ってカタログ化されたものです。

<div class="alert alert-info">

GoF

コンピュータのプログラミングで、
素人と達人の間では驚くほどの生産性の差があり、
その差はかなりの部分が経験の違いからきている。
そんな達人たちが同じ問題に取り組んだ場合、典型的にはみな同じパターンの解決策に辿り着く。
</div>

** 生成に関するパターン**
***Abstract Factory** - 関連する一連のインスタンスを状況に応じて、適切に生成する方法を提供する
***Builder** - 複合化されたインスタンスの生成過程を隠蔽する。
***Factory** -  Method 実際に生成されるインスタンスに依存しない、インスタンスの生成方法を提供する
***Prototype** -       同様のインスタンスを生成するために、原型のインスタンスを複製する
***Singleton** -       あるクラスについて、インスタンスが単一であることを保証する

** 構造に関するパターン**
***Adapter** - 元々関連性のない2つのクラスを接続するクラスを作る
***Bridge** - クラスなどの実装と、呼出し側の間の橋渡しをするクラスを用意し、実装を隠蔽する
***Composite** - 再帰的な構造を表現する
***Decorator** - あるインスタンスに対し、動的に付加機能を追加する。**Filter**とも呼ばれる
***Facade** - 複数のサブシステムの窓口となる共通のインタフェースを提供する
***Flyweight** - 多数のインスタンスを共有し、インスタンスの構築のための負荷を減らす
***Proxy** - 共通のインタフェースを持つインスタンスを内包し、利用者からのアクセスを代理する。**Wrapper**とも呼ばれる

** 振る舞いに関するパターン**
***Chain of Responsibility** - イベントの送受信を行う複数のオブジェクトを鎖状につなぎ、それらの間をイベントが渡されてゆくようにする
***Command** - 複数の異なる操作について、それぞれに対応するオブジェクトを用意し、オブジェクトを切り替えることで、操作の切替えを実現する
***Interpreter** - 構文解析のために、文法規則を反映するクラス構造を作る
***Iterator** - 複数の要素を内包するオブジェクトのすべての要素に対して、順番にアクセスする方法
を提供する
***Mediator** - オブジェクト間の相互作用を仲介するオブジェクトを定義し、オブジェクト間の結合度
を低くする
***Memento** - データ構造に対する一連の操作のそれぞれを記録しておき、以前の状態の復帰または操作の再現が行えるようにする
***Observer** -  インスタンスの変化を他のインスタンスから監視できるようにする。**Listener**とも呼ばれる
***State** - オブジェクトの状態を変化させることで、処理内容を変えられるようにする
***Strategy** - データ構造に対して適用する一連のアルゴリズムをカプセル化し、アルゴリズムの切替
えを容易にする
***Template Method** - あるアルゴリズムの途中経過で必要な処理を抽象メソッドに委ね、その実装を変えることで処理が変えられるようにする
***Visitor** -  データ構造を保持するクラスと、それに対して処理を行うクラスを分離する

デザインパターンは暗記しても、あまり意味がありません。
オブジェクト指向プログラミングを書いていくと、各所に登場しますので、
その度にマスターして自分で使いこなせるようにしましょう。

\fi
