# ライフゲームとシミュレーション

**シミュレーション**(simulation)は、
システムの挙動を、それとほぼ同等の法則をコンピュータなどによって模擬するプログラムです。
今回は、簡単なシミュレーションの題材としてライフゲームを考えます。

<div class="alert alert-warning">

ソースコードの読みやすさ、理解しやすさのため

本講義ノートは、変数名、関数名を一部、日本語表記で書いてあります。
世の中には、日本語変数に抵抗感がある人もいますので、
講義外では英語変数名を使うようにしましょう。

</div>

## ライフゲーム

生命の誕生，生存，死滅のシュミレーションになっています。

<div class="admonition tip">

**例題（ライフゲーム）**

まず、$M \times N$の格子状に区画された大地を考えます。
各区画は$(x,y)$で表され、生命のある状態（生存）と生命のない状態（死亡）のどちらかになっています。

各生命の次の世代は、周囲８つの区画の状態によって決まります。

* **誕生** 区画$(x,y)$に生命がないとき、その周囲の生命が3つあれば、新しく生えてくる
* **生存** 区画$(x,y)$に生命があるとき、その周囲の生命が2つか3つならば、そのまま生存する
* **死滅** 区画$(x,y)$に生命があるとき、その周囲の生命が1つ以下，もしくは4つ以上なら死滅する

\begin{center}
\includegraphics[width=12cm]{figs/lifegame.pdf}\\
(ライフゲームのルール：真ん中の区画に着目)
\end{center}

適切な初期状態を与えたとき，各世代ごとの生命の状態変化を表示するプログラムを作成してみよう。

</div>

## データ表現

プログラムを作るときは、**どのようにデータを表現するか**、と検討してみるところから始めます。

**ライフゲームに必要そうなデータ表現**

* 生命の状態（`生存`、`死滅`）
* $M\times N$ 区画ある地面

<div class="alert alert-info">

データ表現

データ表現は、ひとつの正解があるわけでありまえん。\\
自分でプログラムしやすい方法を試してください。
</div>

### 生命の状態

今回は、生命のある状態（生存）を$1$、生命のない状態（死滅）を$0$で表すことにします。
（多くの人が、同じようにデータ表現を考えると思います。）

ただ、他人がソースコードを読んだときにわかりやすいように`生存`, `死滅` のように定数を定義しておきます。

```py
生存 = 1
死滅 = 0
```

### ２次元のデータ表現

生命は、$M \times N$ 個の区画が格子状に並んだ地面に存在します。
この状態を表現する方法はいくつかあります。

__（素直なのは）２次元配列（リストのリスト）__

```py
地面 = [[死滅] * N for _ in range(M)]

地面[x][y] = 生存  # (x,y) に生命が生じた
```

__(x, y) のタプルをキーとした辞書__

```py
地面 = {}
for x in range(M):
    for y in range(N):
        地面[(x,y)] = 死滅
地面[(x,y)] = 生存  # 地面(x,y) に生命が生じた
```

ここは、読みやすいので後者の辞書を使う方法を採用することにします。

なお、辞書`d`は、`d[key]`の代わりに`d.get(key, value)`という便利なメソッドを提供してくれています。辞書`d`の中に`key`が存在しないときは、代わりに`value`をデフォルト値として用いてくれます。

**(x,y)が範囲外のときは0**

```py
地面.get((x,y), 0)
```

**(x,y)が範囲外が確認が必要**

```py
地面[(x,y)] if (x,y) in 地面 else 0
```

### 道具を用意する

データ構造を決まったら、あとから必要になる道具を用意しましょう。

<div class="alert alert-info">

`周囲の生命数(地面, x, y)`

(x,y)の周囲に生命がいくつあるか数える関数を定義してみよう

</div>


__(x,y)の周囲__

```
(x-1, y-1)  (x, y-1)   (x+1, y-1) 
(x-1, y)    (x, y)     (x+1, y) 
(x-1, y+1)  (x, y+1)   (x+1, y+1) 
```

これは簡単なのでさっさと定義しておきましょう。

**愚直に書くと**

```py
def 周囲の生命数(地面, x, y):
return 地面.get((x-1,y-1),0)
    + 地面.get((x,y-1),0)
    + 地面.get((x+1,y-1),0)
    + 地面.get((x-1,y),0)
    + 地面.get((x+1,y),0)
    + 地面.get((x-1,y+1),0)
    + 地面.get((x,y+1),0)
    + 地面.get((x+1,y+1),0)
```

**周囲の組み合わせから**

```py
周囲 = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]

def count_lives(地面, x, y):
    c = 0
    for dx, dy in 周囲:
        c += 地面.get((x+dx,y+dy), 0)
    return c
```


<div class="alert alert-info">

名言： 道具を用意すれば道は自ずと見える

データ構造を決めたときは、あとから必要になる道具を用意してみましょう
</div>

もし道具が用意できないということは、**データ構造があまりよろしくない**という可能性があります。オブジェクト指向プログラミングを活かして、クラスで定義してみるのも（データ構造と道具をセットで作る）よい練習になります。

## シミュレーションの構造

ライフゲームは，典型的な**シミュレーション・プログラム**の構造を持っています。

まず、初期状態（つまり、適当に生命を配置する）をデータ構造で表現します。
各世代を$t = 0$から初めて、目的の世代(MAX)まで変化させてゆきます。

\begin{center}
\includegraphics[width=8cm]{figs/sym_model.pdf}\\
\end{center}

```py
# 初期状態を用意
地面 = 初期化する()
最大時刻 = 10

for t in range(0, 最大時刻):
    # tのときの状態を表示する
    表示(地面, t)
    # 次の世代の状態を計算する
    更新(地面, t)
```

上記は、どのようなシミュレーションで当てはまる共通構造になっています。

### 初期化: init()

まず、最初の状態を用意する、（つまり、初期化する）`init()` 関数を作っておきましょう。

```py
死滅 = 0  # DEAD
生存 = 1  # ALIVE

M = 8
N = 6

def 初期化する():  # init()
    地面 = {}     # fields
    for x in range(M):
        for y in range(N):
            地面[(x,y)] = 死滅

    # とりあえず、1列に並べてみる
    地面[(1, 2)] = 生存
    地面[(2, 2)] = 生存
    地面[(3, 2)] = 生存
    地面[(4, 2)] = 生存
    地面[(5, 2)] = 生存
    return 地面
```

<div class="alert alert-info">

Let's try

初期配置や(M,N)は自由に変えてみてください

</div>

### 表示(): 地面の状態を表示する

次は，生命の状態を表示する`表示(地面, t)`を作ります。

<div class="alert alert-info">

**プログラミングのコツ:表示系**

真っ先に作る習慣を作ると、**デバッグ** が楽になる

</div>

```py
def 表示(地面, t):
    print('時刻', t)
    for y in range(N):
        for x in range(M):
            if 地面[(x, y)] == 生存:
                print('木', end='')
            else:
                print('・', end='')
        print()
```

__初期状態を表示してみる__

```py
地面 = 初期化する()
show(地面, 0)
```

\begin{center}
\includegraphics[width=4cm]{figs/lifegame_t0.pdf}\\
（「木」は、絵文字に変えてあります）
\end{center}

### シミュレーション本体

シミュレーションの本体(`更新(地面)`)は、時刻tが進んだとき、
世代が進んで生命の状態を変化させる部分になります。

```py
def 更新(地面):
    ...
```

区間$(x,y)$の周囲の生命を数える道具(`周囲の生命数(地面, x,y)`)は、先に準備してあります。

あとは落ち着いて、次のような感じで、ライフゲームのルールをコーディングしていきます。

#### 誕生のルール

区画$(x,y)$に生命がないとき、その周囲の生命が3つあれば、新しく生えてくる

```py
...
    c = 周囲の生命数(地面, x, y)
    if 地面[(x,y)] == 死滅 and c == 3:
        地面[(x,y)] = 生存
..
```

<div class="alert alert-info">

Let's try

「生存」や「死滅」のルールも書いてみましょう。

* **生存** 区画$(x,y)$に生命があるとき、その周囲の生命が2つか3つならば、そのまま生存する
* **死滅** 区画$(x,y)$に生命があるとき、その周囲の生命が1つ以下，もしくは4つ以上なら
初期配置や(M,N)は自由に変えてみてください

</div>

実は、ライフゲームの実装ではもう一箇所**難所**があります。
つまり、ひとつのループの中で数えながら同時に更新をすると、
新旧の世代の状態が混ざってしまいます。
(多少、動きがおかしくなります。)

そこで、最初に周囲の生命数を数えて、一旦、保存しておきます。
そのあと、次のように更新するとうまくいきます。

```py
def update(地面):
    生命数 = {}
    for x in range(M):
        for y in range(N):
            生命数[(x,y)] = 周囲の生命数(地面, x, y)

    for x in range(M):
        for y in range(N):
            c = 生命数[(x,y)]
    # ... あとは頑張る
```

うまく作ることができたら、表示してみましょう。

__３世代ほど表示してみる__

```py
地面 = 初期化する()
表示(地面, 0)
更新(地面)
表示(地面, 1)
更新(地面)
表示(地面, 2)
更新(地面)
```

\begin{center}
\includegraphics[width=4cm]{figs/lifegame_t2.pdf}\\
\end{center}

<div class="alert alert-info">

Let's Try!!

Wikipedia のライフゲームには，
興味深いパターンがいろいろ掲載されているので、ぜひ遊んでみよう。
</div>

## 完成版！

オブジェクト指向プログラミングで定義したライフゲームを掲載しておきます。
コードを読みながら、オブジェクト指向との違いを確認してください。

```py

# 共通するシュミレータの機能を定義する

class Simulator(object):

    def run(self, max=10):
        for t in range(0, max):
            self.show(t)
            self.update()
        self.show(max)

DEAD = 0
ALIVE = 1

class LifeGame(Simulator):
    M:int
    N:int
    fields:list
    
    def __init__(self, M=8, N=6):
        self.M = M
        self.N = N
        # 2次元配列を使う
        self.fields = [[DEAD] * N for _ in range(M)]
        # 最初の生命を配置する（自由に変更してよい）
        self.fields[1][1] = ALIVE
        self.fields[1][2] = ALIVE
        self.fields[2][2] = ALIVE
        self.fields[1][3] = ALIVE
        self.fields[2][3] = ALIVE
        self.fields[3][3] = ALIVE
        self.fields[4][3] = ALIVE
        self.fields[5][3] = ALIVE

    def show(self, t):
        print(f'時刻: {t}')
        for y in range(self.N):
            for x in range(self.M):
                if self.fields[x][y] == ALIVE:
                    print('🌲', end='')
                else:
                    print('💦', end='')
            print()

    def count_lives(self, x, y):
        c = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    c += self.fields[(x+dx)%self.M][(y+dy)%self.N]
        return c
    
    def update(self):
        # まず、生命数を数えておく
        lives = {}
        for x in range(self.M):
            for y in range(self.N):
                lives[(x,y)] = self.count_lives(x, y)

        # ルールにしたがって更新する
        for x in range(self.M):
            for y in range(self.N):
                life = self.fields[x][y]
                c = lives[(x, y)]
                if life == DEAD and c == 3:
                    self.fields[x][y] = ALIVE
                elif life == ALIVE and (c != 2 and c != 3):
                    self.fields[x][y] = DEAD

game = LifeGame(16, 9)
game.run()

```

## コースワーク

ライフゲームをアニメーション化してみよう。

% https://colab.research.google.com/drive/1bTdscYao-SM7vpnY64EazsVSHuREHp5D#scrollTo=jClgMeizhrHc