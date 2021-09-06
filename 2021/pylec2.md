%%%%% test.tex %%%%%
\documentclass[a4j,landscape,papersize,12pt,openany,dvipdfmx,uplatex]{jsbook}

\title{{\Huge 講義資料 \\ {\HUGE 数値計算法II } \\ オブジェクトと計算}}
\author{倉光君郎}
\date{2018}

\usepackage{../enpit/lecnote}
\usepackage{synttree}

\newcommand{\This}{本講義 }
\usepackage{plistings}

\begin{document}

\LARGE

\maketitle

\chapter*{本講義資料について}

本講義資料は、
日本女子大学理学部数物科学科３年生向けの講義資料です。

* Python 入門
* オブジェクトと計算
* (最終目標) スモール言語を作る

\setcounter{chapter}{6}

\chapter{コースワーク}

\begin{note}[テーマ]
有理数の計算機、つまり `1/2 + 1/3 = 5/6` となる計算機を作る
\end{note}

ここからは、より実践的にコースワークを進める.

* ヒントを\Google{repr メソッド} のように与えるので、Google検索しながら開発すること.
* 全然わからないときは、まず友達に聞くこと

## コースワーク

\begin{block}{コースワーク課題}

ユーザが入力した数式をinput()で読み取り、
構文解析し、{\em 有理数}として計算する計算機プログラムを作る

```py
>>> 1/2 + 1/3
5/6
```

* ソースコードを添付すること
* 実行画面も追加すること
* 独自に工夫した機能があれば書くこと
* (余力があれば)スタックマシーンも作ってみる
\end{block}

### コースワークの意図

浮動少数点数(float)では精度に限界がある.

```py
>>> 1/10 + 2/10
0.30000000000000004
```

浮動少数点数の代わりに**有理数**{rational number}を作ってみることで、
精度を気にしない計算をしてみる.

計算機を作ってみることで、言語処理系の基本的な仕組みを学ぶ


### コースワークの意図(2)

中規模なプログラム（１回）の開発を通して、
問題を分割しながら開発する方法を学ぶ.

* １回目 有理数をオブジェクト指向で表現する
* (学ぶこと) 演算子オーバーロード、言語拡張
* ２回目 式を表現する
* ポリモーフィズム、抽象クラス vs. ダックタイピング
* ３回目　構文解析を頑張る
* 再帰下降構文解析、言語仕様を考える

<div class="alert alert-info">

反転学習っぽく

先に手を動かして、あとから仕組みの理解を深める
</div>

## 有理数

二つの整数 $a,b$ （ただし $b$ は $0$ でない）をもちいて $a/b$ という分数で表せる数.

b = 1 とすることにより、任意の整数は有理数となる.

\[
\mathbb{Q} = \left\{{a \over b} \mid a, b \in \mathbb{Z}, b\ne 0\right\}
\]

\vspace{1cm}
<div class="alert alert-info">

課題1: 有理数のオブジェクト表現

有理数をclass Qとして定義してみよう\\
ヒント \Google{repr メソッド}, \Google{Python 引数の初期値}
</div>

### 有理数: class Q

<div class="alert alert-info">

有理数の表現

有理数をクラスQとして定義してみよう
</div>

```py
>>> q = Q(1, 2)
>>> q
1/2

>>> q = Q(3)
>>> q                                #分母が1のときは表示しない
3
```

<div class="alert alert-info">

約分も忘れずに

\[
{n \over m}={b\times d \over a\times d}={b \over a}
\]
</div>

### 有理数の演算

加法・乗法
\[
{a \over b} + {c \over d} = {ad + bc \over bd},\quad {a \over b} \times {c \over d} = {ac \over bd}
\]

減法・減法
\[
{a \over b}-{c \over d}={a \over b}+\left(-{c \over d}\right)={ad-bc \over bd},\quad {a \over b}\div {c \over d}={a \over b}\times \left({c \over d}\right)^{{-1}}={ad \over bc}
\]

反数・逆数
\[
-\left({a \over b}\right)={-a \over b}={a \over -b},\quad \left({c \over d}\right)^{{-1}}={d \over c}
\]

### 有理数の演算

<div class="alert alert-info">

課題2: 有理数のクラス表現

クラスQを拡張子し、有理数の四則演算ができるようにしよう \\
ヒント: 次のページ
</div>

```py
>>> q = Q(1, 2)
>>> q2 = Q(1, 3)
>>> q + q2
5/6

```

### 演算子オーバーロード

<div class="alert alert-info">

演算子オーバーロード

決められたメソッドを定義することで、演算子を拡張すること
</div>

\begin{center}
\begin{tabular}{ll}
`__add__(self, x)`    & self + x \\
`__sub__(self, x)`    & self - x \\
`__mul__(self, x)`    & self * x \\
`__truediv__(self, x)`    & self / x \\
\end{tabular}
\end{center}

例.

```py
class Q:
...
def __add__(self, x):
return Q(self.a * x.b + self.b * x.a, self.b * x.b)
```

### もうアイディアを伸ばしてみよう

有理数の演算に整数を混ぜて行うためにはどうしたらよいのだろうか？

```py
>>> q = Q(1, 2)
>>> q / 2
1/4

```



## 式

式とはプログラムの一種です。

\begin{block}{**式**{expression}}
* 計算
* 実行
* **評価**{evaluation, eval}
* **簡約**{reduction}
すると、**値**{value}になるプログラムのこと
\end{block}

プログラミング言語処理系で広くつかわれる「{\em 評価 (eval)}」という用語を用いる.

\subsection*{式の例}

**式の例**
```py
1
1+1
5*2
1+2*3
```

**評価された値**
```py
1
2
10
7
```

<div class="alert alert-info">

ポイント

値自身も式の一種とみなす
</div>

### 式のオブジェクト表現


\begin{center}
\includegraphics[width=0.35\paperwidth]{./pyimg/expr1.pdf}
\end{center}


式は、オブジェクトと見なせば、

* `eval()` メソッドを持つ
* `eval()` を呼ぶと値を返す


\vspace{1cm}
<div class="alert alert-info">

ポリモーフィズム

評価のふるまいは、式の種類ごとに異なるのでポリモーフィズムで設計する
</div>

### 抽象クラス

**抽象クラス**{abstract class}とは、インスタンス化されることはないが、共通の設計を記述したクラス

\begin{center}
\includegraphics[width=0.55\paperwidth]{./pyimg/expr2.pdf}
\end{center}


```py
# 抽象クラス
class Expr(object):
def eval(self):
pass
```


```py
class Val(Expr):
def __init__(self, v):
self.value = value
def eval(self):
return self.value
```


### 式と評価器

<div class="alert alert-info">

課題3: 四則計算の評価器

四則演算を表す Add, Sub, Mul, Div をクラスで定義し、
eval() すると計算結果が得られるようにする
</div>

```py
>>> e = Add(Val(1), Val(2))
>>> e.eval()
3

>>> e = Mul(Add(Val(1), Val(2)), Val(3))
>>> e.eval()
9

```

### 有理数の四則演算

<div class="alert alert-info">

課題4: 有理数の評価器

課題3の評価器を拡張し、整数の代わりに有理数を扱えるようにしてみよう
</div>

\vspace{1cm}

```py
>>> e = Div(Val(Q(1)), Div(Q(2)))
>>> e.eval()
1/2

```

### もうアイディアを伸ばしてみよう

* 変数を扱えるようにするには？
* 関数を定義できるようにするには？


### オブジェクトと木表現 (前回)

```py
>>> e = Add(Val(1), Val(2))
>>> e.eval()
3

>>> e = Mul(Add(Val(1), Val(2)), Val(3))
>>> e.eval()
9

```
\vspace{1cm}
\texttt{Add(Val(1), Mul(Val(2), Val(3))} $~~~\to~~~$ \\
\synttree{3}[Add[Val(1)][Mul[Val(2)][Val(3)]]] $~~~$


\texttt{Add(Mul(Val(1),Val(2)),Val(3))} $~~~\to~~~$ \\
\synttree{3}[Add[Mul[Val(1)][Val(2)]][Val(3)]]

## 構文解析

構文解析とは、入力文字列を**構文木**{syntax tree}に変換すること

\texttt{1 + 2 * 3} $~~~\to~~~$
\synttree{3}[+[1][*[2][3]]] $~~~$


\texttt{1 * 2 + 3} $~~~\to~~~$
\synttree{3}[+[*[1][2]][3]]

\vspace{1cm}
\begin{block}{構文木}
入力言語の構文を木構造で表現したデータ構造. \\
式のオブジェクト表現(Add, Mul など)も構文木とみなせる.
\end{block}

### 構文解析(今回)

\begin{block}{課題５}
文字列の入力を構文解析して、
式のオブジェクト表現に変換する
\end{block}

\vspace{1cm}

\texttt{1 + 2 * 3} $~~~\to~~~$
\texttt{Add(Val(1), Mul(Val(2), Val(3))}

\texttt{1 * 2 + 3} $~~~\to~~~$
\synttree{3}[Add[Mul[Val(1)][Val(2)]][Val(3)]]



### 再帰下降構文解析法

基本的なアイディア

* 再帰をうまく活用する構文解析

\begin{center}
\includegraphics[width=0.55\paperwidth]{./pyimg/rdp1.pdf}
\end{center}

<div class="alert alert-info">

でも

演算子の優先度が正しく解析されない
</div>

### (先読み付き)再帰下降構文解析法

アドホックだけど.. 先読みを用いる

\begin{center}
\includegraphics[width=0.55\paperwidth]{./pyimg/rdp2.pdf}
\end{center}

<div class="alert alert-info">

注意

構文が複雑になるとお手上げ => 形式文法
</div>

## コースワーク

\begin{block}{コースワーク課題}

ユーザが入力した数式をinput()で読み取り、
構文解析し、有理数として計算する計算機プログラムを作れ

```py
>>> 1/2 + 1/3
5/6
```

* ソースコードを添付すること
* 実行画面も追加すること
* 独自に工夫した機能があれば書くこと
* (余力があれば)スタックマシーンも作ってみる

\end{block}

## (最終)自由課題

自由にプログラムを開発して発表する

* スモール言語を設計し作ってみる [高得点]
* フィボナッチ関数が定義でき、計算できれば素晴らしい
```py
(defun fib (n)
(if (< n 2)
1
(+ (fib (- n 1))
(fib (- n 2)))))
(fib 10)
```
* スモール言語を作ったら、Github で公開しよう.

* 全く自由なプログラムを書いてみる
\vspace{1cm}
* グループ3人まで(一人でもよい)
* グループなら、スモール言語と自由プログラムの両方作ること
* 最終回にノートPCでプログラムの動作を発表する


## (復習)再帰の復習

再帰構造とは、問題 $P(n)$の解法が $P(n-1)$ の解を利用できる構造のこと.

たとえば、$n$階乗を求める問題は、代表的な再帰構造.


\begin{equation}
F_n = \left \{
\begin{array}{lr}
1　&(n = 1) \\
n \times F_{n-1}　& (n > 1) \\
\end{array}
\right. \notag
\end{equation}
\begin{equation}
f(n) = \left \{
\begin{array}{lr}
1　&(n = 1) \\
n \times f(n-1)　& (n > 1) \\
\end{array}
\right. \notag
\end{equation}

再帰構造は、**再帰呼び出し**{recursivce call}を用いると解決できる.

\begin{center}
```py

def f(n):
if(n == 1) return 1;
return n * f(n – 1);

```
\end{center}

### 再帰構造の発見

再帰は，苦手な人が多い.

再帰構造を発見するコツは,
小さな方からいくつか例を書き出してみること.

\begin{equation}
\begin{array}{lcl}
fact(1) & =  & 1 \\
fact(2) & =  & 2 \times 1 \\
fact(3) & =  & 3 \times 2 \times 1 \\
fact(4) & =  & 4 \times 3 \times 2 \times 1 \\
fact(5) & = & ...
\end{array}
\notag
\end{equation}

<div class="alert alert-info">

よく見ると

右辺の一部を fact(1), fact(2), fact(3) で置き換えられませんか？
</div>

### 置き換えた例

\begin{equation}
\begin{array}{lcl}
fact(1) & =  & 1 \\
fact(2) & =  & 2 \times fact(1) \\
fact(3) & =  & 3 \times fact(2) \\
fact(4) & =  & 4 \times fact(3) \\
fact(5) & = & ...
\end{array}
\notag
\end{equation}

<div class="alert alert-info">

よく見ると

変数$n$を使って、パラメータ化（抽象化）できませんか？
</div>

### パラメータ化

\begin{equation}
\begin{array}{lcl}
fact(1) & =  & 1 \\
fact(n) & =  & n \times fact(n-1) ~~~~ (n \ne 1) \\
\end{array}
\notag
\end{equation}

このように漸化式に書き直すことができれば、あとは再帰関数に置き換えるだけ.

\begin{center}

```py

def f(n):
if(n == 1) return 1;
return n * f(n – 1);

```

\end{center}

### 練習：再帰構造の発見

$m^n$を効率よく計算してみよう.

\begin{equation}
\begin{array}{lcl}
3^{16} & =  & 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \\
%        & =  & (3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3) ^ 2  \\
%        & =  & ((3 \times 3 \times 3 \times 3) ^ 2) ^ 2 \\
%        & =  & (((3 \times 3 ) ^ 2 ) ^ 2) ^ 2 \\
\end{array}
\notag
\end{equation}

\vspace{2cm}

\begin{note}[ヒント]
$\times$ の回数を少なくする
\end{note}

### 練習：再帰構造の発見

$m^n$を効率よく計算してみよう.

\begin{equation}
\begin{array}{lcl}
3^{16} & =  & 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \\
& =  & (3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3 \times 3) ^ 2  \\
& =  & ((3 \times 3 \times 3 \times 3) ^ 2) ^ 2 \\
& =  & (((3 \times 3 ) ^ 2 ) ^ 2) ^ 2 \\
\end{array}
\notag
\end{equation}

これを一般化して、$pow(m, n)$という漸化式で書き直してみる.

### 繰り返し二乗法

繰り返し二乗法と呼ばれる
$m^n$の計算を効率よく行う計算法({\em 分割統治法})となる.

\begin{equation}
pow(m, n) = \left \{
\begin{array}{lr}
m　&(n = 1 \mbox{のとき}) \\
pow(m^2, n/2)　&(n \mbox{が偶数のとき}) \\
pow(m^2, n/2) \times m　&(n \mbox{が奇数のとき})
\end{array}
\right. \notag
\end{equation}

### ハノイの塔

ハノイの塔は，典型的な再帰アルゴリズムの例題.

一見難しそうなパズルの問題も，再帰構造に着目すると，驚くほどエレガントに解ける.

\begin{itembox}[r]{★★}
ハノイの塔は、3 本の塔($X, Y, Z$)と、中央に穴の開いた大きさの異なる $n$ 枚の円盤からなる
パズルゲームである。  次のようなルールで遊ぶ。

* 最初はすべての円盤が小さいものが上になるように$X$に積み重ねられている
* 円盤は1回に一枚ずつどこかの塔に移動させることができる
* 小さな円盤の上に大きな円盤を載せることはできない
* 最初の塔と同じ積み方で別の塔にすべて移動できたら終了

円盤数が4のときの円盤を移動させる手順を表示するプログラムを作ろう.

\end{itembox}

### 解法

ハノイの塔は，
再帰構造をうまく活かせば，どうパズルを解くかを考えなくても解ける.

まず、円盤 $1$ から $n$ をXからYに移動させる方法を次のように分解する.

* 円盤 $1$ から $(n-1)$ を{\em「何らかの方法」}で、Y 以外に移動する
* 円盤$n$を Y に移動する
* 円盤$1$ から $(n-1)$ を{\em「何らかの方法」}で、Y の 円盤 $n$ の上に移動させる

\vspace{1cm}

<div class="alert alert-info">

「何らかの方法」

ここで，{\em「何らかの方法」}の部分は、実は再帰的構造になっている.
</div>

### ハノイの塔と再帰構造

再帰構造は、問題$P(n)$ を解決するために、問題$P(n-1)$ の解を再帰的に利用する.

ハノイの塔では，$P(n)$を「$1$ から $n$ 枚目までの円盤を移動させる解」とすると、
$P(n)$は$P(n-1)$と「$n$ 枚目 だけ移動させる解」の組み合わせに分解できる.

* P(n): 1 〜 $n$ の円盤を$X$から$Y$に移動させる
* P(n-1): 1 〜 $n-1$の円盤を$X$から$Z$に移動する
* 円盤$n$を$X$から$Y$に移動させる
* P(n-1): 1 〜 $n-1$の円盤を$Z$から$Y$に移動する

### コード例: ハノイ塔

move(n, 'X', 'Y', 'Z'): n 枚の円盤を　$X$から $Y$に移動する手順を表示する

```py
step = 0;
def move(n, from, to, other) :
if (n > 0) :
move(n-1, from, other, to)
print("Step", step, "move disk", n, "from", from, "to", to)
step +=1
move(n-1, other, to, from)
```

## 言語処理系

* インタプリタ
* コンパイラ

\begin{center}
\includegraphics[width=0.65\paperwidth]{./pyimg/lang.pdf}
\end{center}

### スタックマシン

**スタックマシン**{stack machine} とは、メモリがスタックの形式になっている計算モデルを意味する.


\begin{center}
\includegraphics[width=0.65\paperwidth]{./pyimg/stackmachine.pdf}
\end{center}

### 記法

* 前置記法(ポーランド記法)
* 例. {\HUGE \tt (* (+ 1 2) 3)}
\vspace{1cm}
* 中置記法
* 例. {\HUGE \tt (1 + 2) * 3}
\vspace{1cm}
* 後置記法(逆ポーランド記法)
* 例. {\HUGE \tt 1 2 + 3 *}
\vspace{1cm}

<div class="alert alert-info">

逆ポーランド記法

そのままスタックマシンで処理できる
</div>

## スモール言語へ

* 式(Expr)の種類を増やす
* 変数
* if 式
* 関数定義 (再帰関数)

<div class="alert alert-info">

チューリング完全

プログラミング言語には、\Google{チューリング完全性}が必要
</div>

### 言語設計のヒント

スモール言語を作るときは、構文解析が難所

* S式
* 解析表現文法 (PEGPY)　こちらは倉光に確認

<div class="alert alert-info">

S式

\Google{LISP}のS式が構文解析を書きやすく、言語処理系も作りやすい
</div>

## (最終)自由課題

自由にプログラムを開発して発表する

* スモール言語を設計し作ってみる [高得点]
* フィボナッチ関数が定義でき、計算できれば素晴らしい
```py
(defun fib (n)
(if (< n 2)
1
(+ (fib (- n 1))
(fib (- n 2)))))
(fib 10)
```
* スモール言語を作ったら、Github で公開しよう.

* 全く自由なプログラムを書いてみる
\vspace{1cm}
* グループ3人まで(一人でもよい)
* グループなら、スモール言語と自由プログラムの両方作ること
* 最終回にノートPCでプログラムの動作を発表する

\end{document}
%%%%%

