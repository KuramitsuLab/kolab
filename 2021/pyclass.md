
\begin{note}[テーマ]
オブジェクト指向を理解する
\end{note}

* オブジェクト指向
* クラスとインスタンス（オブジェクト)
* クラス継承 (多相性)
* 演算子オーバーロード

## オブジェクト指向とは

\begin{center}
\includegraphics[width=0.75\paperwidth]{./pyimg/oo.pdf}
\end{center}

### オブジェクトとメッセージ通信

全てを**オブジェクト**{object} と考える

\begin{center}
\includegraphics[width=0.60\paperwidth]{./pyimg/oo2.pdf}
\end{center}

プログラムは、オブジェクト間の**メッセージ通信**{message} と考える

### オブジェクトとメッセージ通信(2)

* 全てを**オブジェクト**{object}
* プログラムは、オブジェクト間の**メッセージ通信**{message}

$1 + 2$ という式は

\begin{center}
\includegraphics[width=0.50\paperwidth]{./pyimg/oo3.pdf}
\end{center}

### クラスとオブジェクト

オブジェクトは

* **クラス**{class}と呼ばれる設計書で設計する
* クラスからインスタンス化することで生成される

\begin{center}
\includegraphics[width=0.40\paperwidth]{./pyimg/class0.pdf}
\end{center}

### オブジェクト指向設計

* オブジェクト（事物）の性質を考え、抽象化する

\begin{center}
\includegraphics[width=0.70\paperwidth]{./pyimg/class1.pdf}
\end{center}

### クラス継承 (class inheritance)

* 既存のクラス（{\em スーパークラス}）の性質を継承し、新しいクラス（{\em サブクラス}）を作る

\begin{center}
\includegraphics[width=0.60\paperwidth]{./pyimg/class2.pdf}
\end{center}

利点
* 再利用性が高まる -- 差分だけプログラムすればよい
* **多相性**{polymorphism}を持たせることができる

## クラス

**クラス**{class}とは、データとデータへの操作を{\em ひとまとめ}にしたもの

\begin{block}{用語}
クラスとしてまとまったデータのことを

* {\em インスタンス変数} (Python, Smalltalk)
* {\em フィールド} (Java, C\#)
* メンバー変数　(C++)

{\em データへの操作}のことを

* メソッド (Python, Java, C\#)
* メンバー関数 (C++)
と呼ぶ.
\end{block}

### クラス定義

\begin{block}{class 定義}
```py
class ＜クラス名＞(＜上位クラス＞):
__slots__ = [＜変数名のリスト＞]

def __init__(self):
#フォールド名の初期化

def ＜メソッド名＞(self):
#フィールドへの操作
...
```
\end{block}

* \PCC{__init__} は、フォールドの初期化を行う特別なメソッド（{\em コンストラクタ}と呼ぶ)
* \PCC{__xxx___}のような名前は、Python 内で特別な意味をもった名前
* \PCC{self} は、自己参照（自分自身へのアクセスするため）の変数名

### クラス定義: Counter クラス

\begin{center}
\includegraphics[width=0.45\paperwidth]{./pyimg/class1.pdf}
\end{center}


```py
class Counter(object):
__slots__ = [cnt]

def __init__(self):
self.cnt = 0

def show(self):
return self.cnt

def count(self):
self.cnt += 1

def reset(self):
self.cnt = 0
```


* インスタンス変数
* 内部状態を保持する変数
* {\tt cnt}
* メソッド
* 外部とメッセージをやり取りする関数
* \PCC{__init__}, {\tt show}, {\tt count}, {\tt reset}

### インスタンス化

クラスからオブジェクトを生成すること

\begin{block}{インスタンス化}
クラス名を（まるで関数名）のように呼ぶ.
```py
c = ＜クラス名＞()
```
\end{block}

* フィールドを保存するメモリが確保される
* \PCC{__init__}が呼ばれ初期化される
* メソッドを通してオブジェクトへの操作が可能になる

### インスタンス化の例


```py
class Counter(object):
__slots__ = [cnt]
def __init__(self):
self.cnt = 0
def show(self):
return self.cnt
def count(self):
self.cnt += 1
def reset(self):
self.cnt = 0
```


```py
# ひとつインスタンス化
c = Counter()

# もうひとつインスタンス化
c2 = Counter()
```


## クラス継承


```py
class Counter(object):
__slots__ = [cnt]
def __init__(self):
self.cnt = 0
def count(self):
self.cnt += 1
def reset(self):
self.cnt = 0
#便利なメソッド
def __repr__(self):
return str(self.cnt)
```


1回で2個カウントする（インチキ）カウンター

```py

class DoubleCounter(Counter):
def count(self):
self.cnt += 2

```


\vspace{1cm}
\begin{block}{練習}
カウンター数をゼロリセットできない{\tt SafeCounter} クラスを定義せよ
\end{block}

### 多態性(多相性) polymorphism

メソッドは、同じ名前でもオブジェクトの種類（クラス）で振る舞いが異なる

\begin{multicols}{3}

```py
c = Counter()
c.count()
c.reset()
```


```py
c = DoubleCounter()
c.count()
c.reset()
```


```py
c = SafeCounter()
c.count()
c.reset()
```


変数 c のクラスが何かは、実行してみるまでわからないことが多い

```py
def test(c):
c.count()
c.reset()
```

<div class="alert alert-info">

動的束縛

実行時に、クラスをみて、どのメソッドを呼ぶか決めること\\
(条件分岐に等しい)
</div>

## 中間試験

* 筆記 (持ち込み不可)
* 実技

\paragraph{問} 下のソースコードを参照しながら、
クラス、メソッド、インスタンス化、クラス継承、多態性の各用語について説明せよ。


```py
class Counter(object):
def __init__(self):
self.cnt = 0
def count(self):
self.cnt += 1
def reset(self):
self.cnt = 0
#便利なメソッド
def __repr__(self):
return str(self.cnt)
```


```py

class DoubleCounter(Counter):
def count(self):
self.cnt += 2

class SafeCounter(Counter):
def reset(self):
pass

```


