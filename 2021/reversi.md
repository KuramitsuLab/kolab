# コードリーティング

コード・リーディングは、
プログラミングやソフトウェア開発の基礎となります。

今回は、与えられたコードを読んで何をしているか理解しましょう。
プログラムを実行させてみることは、コードを理解する助けになります。

* 質問1 何のプログラムでしょう？ (ヒント：何かのゲームです。)
* 質問2 リストの`board`, `WHITE`, `BLACK`, `EMPTY`は、それぞれ何のデータを表現しているのでしょう？
* 質問3 boardの状態を表示する関数はどれでしょうか？
* 質問4 boardを初期化する関数はどれでしょうか？
* 質問5 

## 来週の予習

* 来週は、ユーザと対戦しながらゲームできるようにします。
* 再来週は、ゲームAIを強化します。

コードを読んで理解できた場合は、どんどん先に進めて開発していきましょう。



# Reversi

Reversi は、いわゆるオセロゲームのことです。
オセロ・Othelloは登録商標なので、最近はReversiと呼ぶことが多くなりました。
ここでは、今まで学んできた内容の総まとめとして、
ReversiのゲームAIに挑戦していきます。

## Reversiのルール

Reversiは二人対戦のボードゲームです。

\begin{center}
\includegraphics[width=3.5cm]{figs/othello1.pdf}\\
(最初の配置）
\end{center}

* (一ゲームを短くするため)盤面は$6 \times 6$とする
* 交互に石（黒、白）を置き、相手の石を挟むと自分の色に変わる（反転）
* ひとつも反転できないときは、パスとなる
* 最終的に石が多い方が勝ちとなる


\vspace{1cm}
\begin{center}
\includegraphics[width=12cm]{figs/othello2.pdf}\\
()相手の石を挟むと反転する）
\end{center}

## データ構造を決める

まず、最初にReversiの盤面を表現するデータ構造を決めておきましょう。

今回は、
ボードゲームのAI はいくつもの状態の中から良い手を探す探索アルゴリズムを
用いることになります。（そのため、できるだけシンプルなデータ構造が望ましいです。）

ここでは、$6\times6$の２次元配列で表現しなく、
次のように盤面に位置番号(position)をふって、
１次元配列で表現することにします。

\begin{center}
\begin{tabular}{|c||c|c|c|c|c|c|}
\hline
& 0 & 1 & 2 & 3 & 4 & 5 \\\hline\hline
0& 0 & 1 & 2 & 3 & 4 & 5 \\\hline
1& 6 & 7 & 8 & 9 & 10 & 11 \\\hline
2& 12 & 13 & 14 & 15 & 16 & 17 \\\hline
3& 18 & 19 & 20 & 21 & 22 & 23 \\\hline
4& 24 & 25 & 26 & 27 & 28 & 29 \\\hline
5& 30 & 31 & 32 & 33 & 34 & 35 \\\hline
\end{tabular}
\end{center}

```py
N = 6
board = [0] * (N*N)
```

盤面の石は、次のように定数で定義しておきましょう。

```py
EMPTY = 0
BLACK = 1
WHITE = 2
```

また、人間は(x,y)のような2次元でアルゴリズムを考えた方がわかりやすいです。
そこで、1次元の位置番号(position)と2次元(x,y)を相互に変換する道具を用意しておきましょう。

```py
def xy(p):    # 1次元から2次元へ
    return p % N, p // N
```

```py
def p(x, y):    # 2次元から1次元へ
    return x + y * N
```

## 初期配置

まず、Reversiの初期配置と表示してみる関数を作ってみましょう。

```py
def init_board():
    board = [EMPTY] * (N*N)
    c = N//2
    board[p(c, c)] = BLACK
    board[p(c-1, c-1)] = BLACK
    board[p(c, c-1)] = WHITE
    board[p(c-1, c)] = WHITE
return board
```

表示は、一番簡単な`print()`文を使って
表示してみることにします。

```py
STONE = ['□', '●', '○']

def show_board(board):
    counts = [0, 0, 0]
    for y in range(N):
        for x in range(N):
            stone = board[p(x,y)]
            counts[stone] +=1
            print(STONE[stone], end='')
        print()
    print()
    for pair in zip(STONE, counts):
        print(pair, end=' ')
    print()
```

__初期状態を表示してみる__

```py
board = init_board()
show_board(board)
```

```
□□□□□□
□□□□□□
□□●○□□
□□○●□□
□□□□□□
□□□□□□
('□', 32) ('●', 2) ('○', 2)
```


## 石と反転させる

もうひとつ、石をおいて反転させる関数**put()**を道具として作ってみましょう。
石が挟めない箇所にはおけないので、挟めるかどうか反転する必要があります。

```py
def put(board, position, color):
board[position] = color
#
# ここで反転させる
#
return True  # 1つ以上反転したら
```

* borad 盤面 (64配列)
* position 石を置く位置(0~63)
* color 石の色

どうやって反転させればいいのでしょう？

ここは地道に作るしかありません。
基本的には、８方向全て順番に調べて石を挟むことができるかみてゆきます。

\begin{center}
\includegraphics[width=3.5cm]{figs/othello3.pdf}\\
(石の反転）
\end{center}

<div class="alert alert-info">

Let's try!

落ち着いて作ってみましょう
</div>

この辺りが自力で書けるようになっていれば、
相当なプログラミング力があります。

**ヒント**
* 深さ優先探索で石を挟めるか調べる
* 挟めたら、色を変更する
（油分け算の経路を表示する代わりに、色を反転させる）

まず、周囲（全方向）を調べるのはライフゲームを思い出してみましょう。

<div class="alert alert-info">

(x,y)の周囲

\begin{center}
\begin{tabular}{|c|c|c|} \hline
(x-1, y-1) & (x, y-1) & (x+1, y-1) \\\hline
(x-1, y) & (x, y) & (x+1, y) \\\hline
(x-1, y+1) & (x, y+1) & (x+1, y+1) \\\hline
\end{tabular}
\end{center}
</div>

```py
DIR = [
(-1, -1), (0, -1), (1, -1),
(-1, 0),         (1, 0),
(-1, 1), (0, 1), (1, 1),
]
```

方位のペア(例えば、(-1. -1)を(dx, dy)と表現し、(-1, -1), (-2, -2), ...
のように深く探索していきます。
次は、(dx, dy) 方向に探索し、相手の石がcolor で挟めるとき、
反転する関数です。挟めなければ False を返します。

```py
# (x,y) が盤面上か判定する
def on_borad(x, y):
return 0 <= x < N and 0 <= y < N

def try_reverse(board, x, y, dx, dy, color):
if not on_borad(x, y) or board[p(x, y)] == EMPTY:
return False
if board[p(x, y)] == color:
return True
if try_reverse(board, x+dx, y+dy, dx, dy, color):
board[p(x,y)] = color
return True
return False
```

最終的に、石をおいて反転させる関数`put_and_reverse`は次の通りになります。

```py

# 相手（反対）の色を返す
def opposite(color):
if color == BLACK: return WHITE
return BLACK

# (x,y) が　相手（反対）の色かどうか判定
def is_oposite(board, x, y, color):
return on_borad(x, y) and board[p(x, y)] == opposite(color)

def put_and_reverse(board, position, color):
if board[position] != EMPTY:
return False
board[position] = color

x,y = xy(position)
turned = False
for dx, dy in DIR:
nx = x + dx
ny = y + dy
if is_oposite(board, nx, ny, color):
if try_reverse(board, nx, ny, dx, dy, color):
turned = True
if not turned:
board[position] = EMPTY
return turned
```

関数`put_and_reverse()`を使えば、
盤上に石をおけるかどうか判定する関数も定義できます。

```py
# board上にcolor色の石をおけるか？

def can_play(board, color):
board = board[:] # コピーしてボードを変更しないようにする
for position in range(0, N*N):
if put_and_reverse(board, position, color):
return True
return False
```

## おちびAI

ReversiのAIは、boardと色を受け取り、どこに置くかを決めて返します。
次のような関数で定義することができます。

```py
def reversi_ai(board, color):
    # どこに置くか決める
    return position
```

まず、すごく簡単な（AIと呼んで良いかどうかビミョーな）AIを作ってみましょう。
Reversiのルールを覚えたばかりの子供と同じ思考なので、
おちびAI(ochibi)と名付けます。

* 盤面を位置0から位置31まで探索する
* 自分の石が置けたら、損得考えず、そこに置く

```py
def ochibi(board, color): #おチビAI
for position in range(N*N):
if put_and_reverse(board, position, color):
return position
return 0

```

## ゲームと対戦

最後にAI同士を対戦させる関数`game()`を作っておきましょう。
引数でAIの関数を受け取って対戦させます。

```py
def game(player1, player2):
board = init_board()
show_board(board)
on_gaming = True  # 　ゲームが続行できるか？
while on_gaming:
on_gaming = False  # 　いったん、ゲーム終了にする
if can_play(board, BLACK):
# player1 に黒を置かせる
position = player1(board[:], BLACK)
show_board(board)
# 黒が正しく置けたら、ゲーム続行
on_gaming = put_and_reverse(board, position, BLACK)
if can_play(board, WHITE):
# player1 に白を置かせる
position = player2(board[:], WHITE)
show_board(board)
# 白が置けたらゲーム続行
on_gaming = put_and_reverse(board, position, WHITE)
show_board(board)  # 最後の結果を表示!
```

\Run{おちび vs. おちび}
```py
game(ochibi, ochibi)
```
\Out
```py
●●●●●●
●●●●●●
●●●●●○
○●●●●○
○○●●●○
○○○○○○
('●', 24) ('○', 12)
```

「おちび vs. おちび」は、先手(●)の勝ちです。
いくつかAIを作ってみて、対戦させてみましょう。

**簡単に作れるAI**
* `random(board, color)`: ランダムにおく（簡単）
* `eager(board, color)`: 一番石が取れる場所におく

## より強いAIを求めて

Reversiは、より強いAIを作るためには、
評価関数を使って，もっとも高スコアになるように位置を決定します。

<div class="alert alert-info">

評価関数

石をおける候補に得失点のスコアをつける
</div>

評価関数の作り方はいくつか知られています。

Reversiは，例えば、４隅に置くと有利ということが知られています。
このような経験則から、盤面の位置を得点化し，得点表を評価関数とすることができます。

\begin{center}
\begin{tabular}{|c|c|c|c|c|c|} \hline
8 & 6 & 6 & 6 & 4 & 8  \\\hline
4 & 2 & 4 & 4 & 2 & 4  \\\hline
6 & 4 & 0 & 0 & 4 & 6  \\\hline
6 & 4 & 0 & 0 & 4 & 6  \\\hline
4 & 2 & 4 & 4 & 2 & 4  \\\hline
8 & 4 & 6 & 6 & 4 & 8  \\\hline
\end{tabular}
\end{center}

どんなに頑張って得点表を調整しても、人間に勝てるようにするのは難しいでしょう。
ここでは、ゲームの達人が行っている「$N$手先を読む」を探索アルゴリズムが必要となります。

ゲームを探索問題として解くためには，**ゲーム木**{game tree}を作ります。
これは，現在の盤面をトップノードとして、石を置くことができる候補を探し，次の盤面を展開します。
次に、相手側の立場にもなって、同じように候補を探し，更にゲーム木を深くしていきます。


\begin{tabular}{ll}
\begin{minipage}{0.4\hsize}
\begin{center}
\includegraphics[width=5cm]{figs/gametree.pdf}
%caption{各構文木のデータ構造}
\label{fig:word}
\end{center}
\end{minipage}
&
\begin{minipage}{0.52\hsize}
オセロゲームの場合は，探索範囲が広すぎて，完全なゲーム木を構築することができません。
そこで，適当な深さでゲーム木の構築を打ち切って評価することになります。
\end{minipage}
\end{tabular}\\

最後まで読み切ることができれば、それが最善手です。
しかし、ゲーム木の状態が大きくなりすぎるので、基本的にゲーム木の状態を減らしながら、
適当な深さまで幅優先探索していきます。

<div class="alert alert-info">

ゲーム木の探索アルゴリズム

* ミニマックス法
* $\alpha-\beta$法
* モンテカルロ法

</div>

最近は、機械学習（強化学習）を用いて、
人間より強いオセロゲームを作ることも十分に可能になっています。

ゲームは，人間より強いことが目標ではありません。強すぎても弱すぎても楽しくありません。
最近のゲームは，人間側の行動をモデル化し，自動的にコンピュータの強度を調整しています。
オセロにもこのような工夫を取り込んでみましょう。


