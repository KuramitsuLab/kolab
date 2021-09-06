\chapter{スタックとキュー}

Python は、リストや辞書などの複雑なデータを効率よく扱う汎用的なデータ構造を提供しています。
今回は、計算量の観点からこれらのデータ構造をみていきましょう。

## リスト

リストは、最も基本的なデータ構造です。
C/C++の配列をベースにしていますが、可変長配列として拡張されていて、
実行時に**配列の大きさを伸長する**ことができます。

```py
a = [1, 2, 3]
print(a)
a.append(4)
print(a)
a.append(5)
print(a)
```
```py
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 5]
```

リストは便利で、特にデータサイズが事前にわからないときは重宝します。
しかし、リストの内部がどのように実装されているか理解しないと、
**極めて効率の悪いプログラムを書いてしまう**ことがあります。

### リストの仕組み

リフトは、**可変長配列**{growing array}と呼ばれる方式で実装されています。

まず、リストの要素は、**配列**{array}と呼ばれるメモリ上の並んだ領域に順番に記録されます。
このとき、将来、要素が追加される可能性を見越して少し大きめの配列を用意しておきます。
リストに要素が追加されたときは、配列の空き領域に追加してゆきます。
\begin{center}
\includegraphics[width=3cm]{figs/Alist.pdf}
%caption{各構文木のデータ構造}
%\label{fig:word}
\end{center}

もし空き領域がないときは、より大きな配列の領域を確保して、**配列の内容をコピーします**。
コピーしたあと、空き領域に追加します。
\begin{center}
\includegraphics[width=5cm]{figs/Aappend.pdf}
\end{center}

ここで注意しておきたいのは、配列のコピー処理は、
**無視できないほど処理時間がかかる**点です。
そのため、
できるだけコピーの回数を減らすため、配列の空き領域を伸長するときは大きめの配列を確保します。
経験的には、2倍に増やすとよいので、
大きなリストはかなり空き領域を余分に確保しています。

### リスト操作の計算量

Python のリストは、要素を追加するだけでなく、挿入したり、取り除くことができます。
これらのメソッドは便利です。ただし、頻繁に使う時は注意が必要です。

\texttt{a.insert(i, x)}: a[i] の位置にxの挿入する\\
\begin{center}
\includegraphics[width=5cm]{figs/Ainsert.pdf}
%caption{各構文木のデータ構造}
\end{center}
\texttt{a.pop(i)}: a[i]の位置の要素を取り除く\\
\begin{center}
\includegraphics[width=5cm]{figs/Apop.pdf}
%caption{各構文木のデータ構造}
%\label{fig:word}
\end{center}

配列は、そもそも空きなく並んでいることで、高速なアクセスを実現しています。
そのため、挿入するために空きを作ったり、削除したあと空きを埋める必要があり、
毎回、配列のコピーが発生します。
これらのコストを平均計算量としてまとめると以下の通りになります。

<div class="alert alert-info">

大きさ$N$のリストの平均計算量

\begin{center}
\begin{tabular}{cccc} \hline
参照 & 追加 & 挿入 & 削除 \\\hline
`a[i]` & `a.append(x)` & `a.insert(i, x)` & `a.pop(i)` \\
$O(1)$ & $O(1)$ & $O(N)$ & $O(N)$ \\\hline
\end{tabular}
\end{center}
</div>

## 連結リスト

**連結リスト**{linked list}は、ノードとリンクで構成されるリストです。
最も簡単なリストは、次のとおり、単方向のリンクによって構成される連結リストです。

\begin{center}
\includegraphics[width=5cm]{figs/LLlist.pdf}
%caption{各構文木のデータ構造}
%\label{fig:word}
\end{center}

連結リストは、リンク先を変更するだけで、要素の挿入や削除ができるため、
挿入や削除の操作が多いとき、よく利用されます。

### リンクと参照

連結リストを作るためには、Python 上で**リンク**{link}を表現する必要があります。

Python上の値は、整数であっても全てオブジェクトです。
オブジェクトは、メモリ上に確保された領域にデータを保存しています。
Python の組み込み関数 `id()`を用いると、
オブジェクトを保存したメモリのアドレスを知ることができます。

```py
id(1)
```
```py
4497766960
```

Python の変数は、
このアドレスを**オブジェクトへのリンクとして**保持しています。

```py
x = 1
id(x)
```
```py
4497766960
```

次のようにリストを作り、変数 a, b に代入します。
そのあと、変数 bのリストを変更したら、変数 a のリストも変更されています。
両者は、同じリストへの参照だからです。（リンクのことを参照と呼びます。）

```py
a = [1,2,3]
b = a
b[0] = 0
print(a)
print(b)
```
```py
[0, 2, 3]
[0, 2, 3]
```

<div class="alert alert-info">

Pythonの変数

オブジェクトへの**参照**{reference}
</div>

### 連結リスト

連結リストは、オブジェクト指向を使って定義します。
まず、ノードをクラスとして定義してみます。

```py
class Node(object):
value: object
next: object
def __init__(self, value, next=None):
self.value = value
self.next = next
```
* \texttt{value}: ノードの値を表す
* \texttt{next}: 次のノードを表す

`None`は、
Python における特別なオブジェクトで**存在しないことを表すオブジェクト**になります。
つまり、\texttt{next} プロパティの値が`None`のときは、連結リストの終端になります。

```py
head = Node(3, None)
head = Node(2, head)
head = Node(1, head)
```
\begin{center}
\includegraphics[width=5cm]{figs/LLlist.pdf}
%caption{各構文木のデータ構造}
%\label{fig:word}
\end{center}

これだけでは、連結リストがどうなっているのかわからないので、表示する関数を定義してみましょう。

\Run{連結リストを表示する}
```py
def show(node):
while node.next != None:
print(node.value, "->")
node = node.next
print(node.value)

show(head)
```
\Out
```py
1 ->
2 ->
3
```

\hr
\HBold{例題（連結リストの最後尾に追加する）}
連結リストの先頭(head)が与えられたとき、最後尾に値を追加する関数
`append(head, value)`を定義してみよう。

\hr

まず、与られたノードから最後尾のノードを探す関数`tail(node)`を探す関数を定義します。

```py
def tail(node):
while node.next != None:
node = node.next
return node
```

あとは最後尾のノードのnext に新しいノードを作って追加すればおしまいです。

```py
def append(head, value):
node = tail(head)
node.next = Node(value, None)

append(head, 10)
show(head)
```


\Out
```py
1 ->
2 ->
3 ->
10
```

<div class="alert alert-info">

Let's try

連結リストの参照、追加、削除の計算量を考えてみよう。
</div>

## スタックとキュー

**スタック**{stack}は、
リストに対するLIFO(Least In First Out, 後入れ先出し)操作を行うデータ構造です。
名前が示すとおり、荷物を積んでいくときの操作に似ています。

\begin{center}
\includegraphics[width=0.45\paperwidth]{./figs/stack.pdf}
\end{center}

**キュー（待ち行列）**{queue}は、
リストに対する**FIFO(First In First Out, 先入れ先出し)**操作を行うデータ構造です。
スタックと対をなす基本データ構造なので、こちらもマスターしておきましょう。

\begin{center}
\includegraphics[width=0.35\paperwidth]{./figs/queue.pdf}
\end{center}

### スタックの実装

スタックは、連結リストを利用して実装することもできます。
ポイントは、一番頂上のノード(top)をプロパティで覚えておくことです。

```py
class Stack(object):
top: Node
def __init__(self):
self.top = None

def push(self, x):
self.top = Node(x, self.top)

def pop(self):
if self.top != None:
x = self.top.value
self.top = self.top.next
return x
```

\Run{スタックに積む}
```py
stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
```
\Out
```py
2
```

<div class="alert alert-info">

注意: リストを使っても良い

スタックの操作は、リストの`append(v)`, `pop()`でも同じ操作になります。
通常は、こちらを使えば十分です。
</div>

\Run{スタックに積む}
```py
stack = []
stack.append(1)
stack.append(2)
stack.pop()
```
\Out
```py
2
```

### 回文判定

スタックの練習として典型的な問題を解いておきましょう。

\hr
\HBold{例題(回文)}
**回文**{palindrome}とは、
始めから（通常通り）読んでも、
終わりから（通常と逆に）読んでも、同じになる文のことである。

例. Was it a car or a cat I saw?

与えられた文字列$s$が回文であるか判定する関数`palindrome(s)`を定義してみよう。
なお、文字は英字に限定し、英大文字/小文字の違いや空白、句点等は無視すること。

\hr

**解放**
* 文字列を空白、句点を取り除きます。`s.replace()`を使う
* $s$英小文字に統一します。`s.upper()`
* 文字列$s$の真ん中で分割します。
* 前半の文字列を全部スタックに積みます。
* スタックからpopしながら、後半と比較します。

### キューの実装

キューも、連結リストを利用して実装することもできます。
ポイントは、ノードの先頭(head)と最後尾(tail)の両方とも
プロパティで覚えておくことです。

```py
class Queue(object):
head: Node
tail: Node

def __init__(self):
self.head = None
self.tail = None

def enqueue(self, x):
if self.tail == None:
self.tail = Node(x, None)
self.head = self.tail
else:
tail = Node(x, None)
self.tail.next = tail
self.tail = tail

def dequeue(self):
if self.head == None:
return None
value = self.head.value
self.head = self.head.next
return value
```

\Run{キューから取り出す}
```py
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
```
\Out
```py
1
```

<div class="alert alert-info">

注意: キューは計算量に注意

キューの操作は、リストの`append(v)`, `pop(0)`でも同じ操作になりますが、\\
{\large {\tt pop(0)} は計算量が大きい}です。
</div>

\section*{チャレンジ課題}

逆ポーランド記法で与られた数式(文字列s)を計算するプログラム`p(s)`を作ってみよう。

**例**
* `s = "1 2 +"`のとき, `p(s)`は$3$
* `s = "1 2 + 2 3 + *"`のとき、`p(s)`は$15$

<div class="alert alert-info">

数式の記法

* **前置記法**{ポーランド記法, prefix notation} \\
演算子を被演算子（オペランド）の前に記述する
* 例. `(+3 4)` (LISP)
* 例. `add 3 4` (アセンブリ)
* **中置記法**{infix notation} \\
演算子を被演算子（オペランド）の間に記述する
* `3 + 4`
* **後置記法**{逆ポーランド記法, postfix notation}\\
演算子を被演算子（オペランド）の後に記述する
* 例. `3 4 +` (forth, postscript)
* 例. `3 と 4 を加算する` (日本語)
</div>


\HBold{ヒント} 後置記法は、
****スタックマシン**{stack machine**と呼ばれる計算モデル}で
前から順番に字句を処理することで簡単に計算することができます。
スタックマシンは、{\CS}の基礎なので、仕組みを抑えておきましょう。

\begin{lbox}{スタックマシン}

**スタック**{stack}を計算結果を一時的に保持するメモリとして用いる

* 数値は、スタックにそのまま数値を push する
* 演算子は、スタックの上２つの値を pop し、その計算結果を push する
\end{lbox}


%\subsection{回文}


\if0
\HUnder{ヒント} スタックを使う

%\subsection{待ち行列}

\vspace{2cm}
\HBold{課題(パン屋の待ち行列)} 大人気のパン屋がある。
$n$人の客が順番に並んでいる。
$i$番目の客$(i \ge 0)$は、それぞれ欲しいパンの個数 $N_i > 0$がある。

パン屋は，先頭の買い占めを防ぐため，次のようにパンを販売することにした。

* １回で最大10個までパンを販売する。
* 希望個数を購入できなかった客は、待ち行列の最後尾に並び直し，次の販売を待つ。

パンの総販売個数は100個である。
今、各客の欲しいパンの個数のリストが与えられたとき，
i番目の客が購入できるパンの個数を表示するプログラムを作れ。

%この問題は，パンを欲しい個数変えなかったときは，後ろに並び直します。
%これは，dequeue し，そのあと enqueue することになる。
\fi

\subsection*{\Extra}

* **Stack (ALDS1\_3\_A)**
逆ポーランド記法で与えられた数式の計算結果を出力せよ\\
\url{http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A\&lang=jp}
* **Stack (ALDS1\_3\_B)**
ラウンドロビンスケジューリングをシミュレートせよ\\
\url{http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B\&lang=jp}






