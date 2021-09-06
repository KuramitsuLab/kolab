# NumPyとグラフ

データサイエンスや機械学習の基礎となるNumPyとMatplotlibの使い方を学びます。

## 準備

Pythonで拡張機能を用いたプログラミングをするときは、まずモジュールをインポートして使います。

### Numpyとは

Numpyは、科学計算やデータサイエンス、機械学習で最もよく使われる基本的なライブラリです。
多次元配列を効率よく処理することができます。

Numpy モジュールを`np`という名前でインポートします。

```py
import numpy as np
import numpy.random as random
%precision 3
```

### Matplotlib

Matplotlib は、NumPy配列などを描画する定番のライブラリです。
出版に耐えうる高品質なグラフが作画できます。

```py
import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline
```

Colab上で、グラフを日本語表示したいときは、
日本語化されたmatplotlibをあらかじめインストールして用います。

```
!pip install japanize_matplotlib
import japanize_matplotlib #日本語化 matplotlib 
sns.set(font="IPAexGothic") #日本語フォント設定
```

最初にまとめて、一度にインポートするようにしておくと良いでしょう。

__モジュールの準備__

```py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    import japanize_matplotlib #matplotlibの日本語化  
except ModuleNotFoundError:
    !pip install japanize_matplotlib
    import japanize_matplotlib 
sns.set(font="IPAexGothic") #日本語フォント設定

```

## リストと配列

リストは、複数のデータを列として扱うデータ構造です。
次のように`[ ]` で囲んでリストを作ります。

__リストの例__

```py
data = [1, 2, 3, 4, 5, 6] 
print(data)
```

NumPy配列は、科学技術計算のため開発されたリストの高効率＆高速版です。

__NumPyの配列__: リストの高速版

```py
data = np.array([1, 2, 3, 4, 5, 6])
print(data)
```

データサイエンスや機械学習では配列を使うことが多いので、
NumPyの配列の使い方を学びます。

### リスト/配列の基本操作

リストや配列は、インデックス(添字)によって内部の値を取り出すことができます。

<div class="admonition danger">

**例題（配列）**

次の配列`a`に対し、次の値を求める操作を書いてみよう

入力例：

```py
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
```

1. `a`の最初の要素
2. `a`の要素数を得る
3. `a`の先頭と末尾の和
4. `a`の先頭を取り除いた配列
5. `a`を逆順にした配列
6. `a`の総和
7. `a`の平均値

</div>

__最初の要素__

```py
print(a[0])
```

<div class="admonition warning">

**$N$個数える**

プログラミング(Python)では、原則、「**0から**$N-1$まで」のように0から数えます。

</div>

__要素数を得る__

```py
len(a)
```

__`a`の先頭と末尾の和__

```py
a[0]+a[len(a)-1]
```

添字を`-n`にすると、末尾から位置を指定できます。

```py
a[0]+a[-1]
```

__`a`の先頭を取り除いた配列__

```py
a[1:]
```

__`a`を逆順にした配列__

```py
a[::-1]
```

__`a`の総和__

```py
a.sum()
```

__`a`の平均値__

```py
a.mean()
```

### まとめ

|数列(数学)|リスト(Python)|意味      |
|--------|------------|-----------|
|$\|a\|$ | `len(a)`   |個数  |
|$a_1$|`a[0]`         |先頭の値     |
|$a_2$|`a[1]`         |      |
|$a_i$|`a[i]`         |i番目の値    |
|$a_{N-1}$|`a[len(a)-2]`もしくは`a[-2]` |  |
|$a_{N}$|`a[len(a)-1]`もしくは`a[-1]` |末尾の値|

### 配列の演算

Numpyの配列は、科学技術計算用に開発されたため、データは演算はベクトルとして解釈されます。

```py
a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 0, 1])
```

__配列の和__

```py
a + b
```

__配列の差__

```py
a + b
```

__配列のスカラー積__

```py
a * 2
```

__内積__

```py
a * b
```

__次元の変更__

```py
a.reshape(2,2)
```

### 数列の生成

最後に、データサイエンスで用いる便利な数列の生成を紹介しておきます。

__等差数列__ (つまり、`range(x)`のNumPy版)

```py
np.arange(10)  # 0から10未満までの整数列
```

```py
np.arange(1, 101, 5)  # 1から100までの5刻みの整数列
```

__区間を指定した数列__

こちらは、要素の数をズバリ指定します。

```py
np.linspace(-10, 10, 20)  # 区間[-10, 10] 要素数20の数列
```

__同じ値の数列__

20個の0からなる数列

```py
np.zeros(20)  # 0が20個
```

```py
np.ones(15)  # 1が15個
```

__乱数列__

```py
np.random.rand(100)   # 0.0から1.0までの乱数列(100個)
```

```py
np.random.randint(1, 6, 100) #1から6までの乱数列(100個)
```

## グラフの描画

数列は、グラフ化すると、視覚的にみやすく、特徴が理解しやすくなります。

例えば、x, yの数列を表示してみても、xとyの関係性はわかりません。

```py
x = np.linspace(-10, 10, 100)
y = np.sin(x)
print(x)
print(y)
```

Matplotlib でグラフに表示してみると、わかります。

```py
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.grid(True)
```

__例: sin(x)のユニバーサル関数__


```py
a = np.array([0.0, 0.1, 0.2])
np.sin(a)

```

<div class="admonition warning">

ユニバーサル関数: `np.sin()`

`np.sin(x)`は、NumPy用の$sin(x)$関数です。配列`x`の各要素ごとに$sin(x)$を計算します。

</div>

### グラフの書き方

$y = sin(x)$の例から、グラフの書き方を学びましょう

1. x 軸の数列を作成する
2. y 軸の数列を計算する
3. グラフの大きさ、ラベルなどを設定
4. `plt.plot(x, y)` でグラフにプロット

```py
x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 2)) #グラフの大きさを指定
plt.plot(x, y, label='sin(x)')
plt.legend() #ラベルの表示

plt.title('y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True) #グリッド

```

<div class="admonition danger">

Let's try

1. $y=cos(x)$のグラフに書き換えてみよう
2. $y=sin(x)$と$y=cos(x)$を同じグラフに書いてみよう
3. $y=sin(x), y=sin(2x), y=sin(3x), ..$ と同じグラフに書いてみよう

</div>

### 関数グラフの描画

自分で定義した関数もグラフで描画することができます。

$f(x) = x^2 - 2x + 1$

```py
def f(x):
    return x ** 2 - 2*x + 1
```

```py
x = np.linspace(-4, 4, 100) # 区間[-4, 4]にする
y = f(x)

plt.figure(figsize=(5, 3)) #グラフの大きさを指定
plt.plot(x, y, label='f(x)')
plt.legend() #ラベルの表示

plt.title('$y=x^2-2x+1$') # latex の数式
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
```

### 円の描画 (媒介変数)

円は、$x^2 + y^2 = 1$ ですね。つまり、媒介変数$t$を用いると、次のように直せますね。

1. $x = cos(t)$
2. $y = sin(t)$

```py
t = np.linspace(-np.pi, np.pi, 100)
x = np.cos(t)
y = np.sin(t)
plt.figure(figsize=(5,5))
plt.plot(x, y)
```

楕円も描画することができます。

```py
t = np.linspace(-np.pi, np.pi, 100)
x = np.cos(t)
y = np.sin(t)
plt.figure(figsize=(5,5))
plt.plot(x, 0.5 * y)
plt.ylim(-1.0, 1.0)
```

<div class="admonition danger">

Let's try

[リサジュー図形](https://ja.wikipedia.org/wiki/リサジュー図形)を描画してみよう。
</div>

## 色々なグラフ

Matplotlibは色々なグラフを描画することができます。少し例をみながら書き方を学びましょう。

### 散布図 (`plt.scatter(x,y)`)

散布図は、2つのデータの組み合わせに対して、xy座標上にプロットしたグラフです。散布図を書くと、ふたつのデータの関連性が見えてきます。

__一様乱数列 X, Yの散布図__

```py
x = np.random.rand(100)
y = np.random.rand(100)
plt.figure(figsize=(4,4))
plt.scatter(x, y, marker='x')
```

__色分けして表示する例__

[モンテカルロ法](https://ja.wikipedia.org/wiki/モンテカルロ法)で、円周率を求めるとき、半径１の円の中にあるかないかで色分けしてみます。

```py
# モンテカルロ法
x = np.random.rand(200)
y = np.random.rand(200)
d = np.hypot(x, y)   # 原点から(x,y)の距離

# 原点からの距離で分ける
x_inside = x[d<1.0]  
y_inside = y[d<1.0]
x_outside = x[d>=1.0]
y_outside = y[d>=1.0]

plt.figure(figsize=(5,5))
plt.scatter(x_inside,y_inside, c='pink')　# ピンク色
plt.scatter(x_outside,y_outside, c='cyan') # シアン色

```

<div class="admonition warning">

フィルタ

フィルタは、条件にマッチした値だけ残す操作です。少し特殊ですが`配列[条件式]`のように書きます。

```py
a = np.array([1,2,3,4,5,6,7,8,9])
a[a % 2 == 0] # 偶数かどうか
```
</div>

### 棒グラフ `plt.bar()`

棒グラフは、カテゴリーごとの数値を比較したい時に使います。
```py
x = [1, 2, 3]
y = [10, 1, 4]

plt.figure(figsize=(5,3))
plt.bar(x, y, align='center', width=0.5)
plt.xticks(x, ['A', 'B', 'C'])

```

### ヒストグラム

ヒストグラムは、縦軸に度数、横軸に階級をとり、データの分布状況を視覚的に認識するために定番のグラフです。

__サイコロを60回ふったときの各目の出現__

```py
x = np.random.randint(1, 7, 60) #1以上7未満の60個の乱数
print(x)
plt.hist(x, bins=6, rwidth=0.8) 
plt.axhline(y = 10, color='red', linestyle='--') #期待値に赤点戦を引く
```

<div class="admonition note">

Let's try: [大数の法則](https://ja.wikipedia.org/wiki/大数の法則)

サイコロをふる回数を増やしてみて、偏りが平坦になることを確認してみよう（つまり、60を大きくしてみよう。）
</div>

### Subplot 複数の図を表示する

Subplotの機能を使えば、複数の図をみやすいように一枚にまとめて描画することができます。

```py
# https://matplotlib.org/tutorials/introductory/pyplot.html より
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(2,1,1)  # 1枚目の位置
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(2,1,2)  # 2枚目の位置
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
```

<div class="admonition warning">

subplot の理解するためには

グラフを1枚追加して、`plt.subplot(3,1,3)`で描画してみよう。もしくは、`subplot()`のパラメータを変更してどうなるか変わるか調べてみよう。

</div>

### もっと Matplotlibを使いこなすには？

Matplotlibは、科学論文誌において定番的に用いられるグラフ作成術です。
機能は豊富で短期間にマスターし尽くせるものでもありません。

今後、Matplotlib を使ってグラフを描画するサンプルをみることが増えますが、
気になるところがあったら、Webで調べながら技を増やしていきましょう。

ぜひ、Webの情報を活用して使いこなしていきましょう。

https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9

## コースワーク

<div class="admonition danger">

**演習問題（サイコロの目の和）**

$n$個のサイコロを1000回振ったときの**サイコロの目の和**を考える。サイコロの数を$1$から$8$に増やしていくと、サイコロの目の和の頻度分布をヒストグラムとして描画せよ。また、サイコロの数が増えたとき、最終的にどのような分布に近づくか考察せよ。
</div>

__例__：(可能であれば１枚にまとめてみましょう。
![c3_example.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/5347cd65-5a95-6e49-de47-d444af60b7fa.png)

