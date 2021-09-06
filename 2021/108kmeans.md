# クラスタリングしてみよう

クラスタリング（clustering）とは、データ間の類似度にもとづいて、データをグループ分けする手法です。
データ分析のはじめにデータの特徴を把握するために活用されます。
また、機械学習アルゴリズムとしても __教師なし学習__ として重要です。

今回は、代表的なクラスタリングアルゴリズムをハンズオン演習しながら、
クラスタリングを行う技法を学んでいきましょう。

__モジュールの準備__
```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
try:
    import japanize_matplotlib #日本語化 matplotlib 
except ModuleNotFoundError:
    !pip install japanize_matplotlib
    import japanize_matplotlib 
sns.set(font="IPAexGothic") #日本語フォント設定

```
## クラスタリング

クラスタリングとは、データ間の類似度にもとづいて、データをグループ分けする手法です。クラスタリングによってできた、似たもの同士が集まったグループのことをクラスタと呼びます。

<img src="https://scikit-learn.org/stable/_images/sphx_glr_plot_cluster_comparison_001.png" width="80%" align="center">

__活用例__

* 顧客のセグメンテーション
* 学生をグループ分け
* テキストマイニング
* 画像の分類

「データ間の類似度にもとづいてデータをグループ分けする」という特徴の活かし方次第で、さまざまな問題に応用できます。

<!--
### クラスタリングの種類
-->


### K-means法 (K-平均法)

**K-means法**は、クラスタリングで最も広く使われている手法です。
非階層型クラスタリングのアルゴリズであり、クラスタの平均を用い、与えられたクラスタ数$k$個に分類します。

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/K-means_convergence.gif" width="50%" align="center"/>

原理：k-means法は、$n$次元のデータを$k$個のクラスタに分割する。

1. ランダムに$k$個クラスタの重心点（$n$次元ベクトル）$V_{1},\dotsc ,V_{k}$をおく
2. 各データに対し、クラスタと最も近いものをクラスタ所属とする。
3. 全てのデータに対して、クラスタ番号が決まったのち、それぞれのクラスタの重心（平均）を計算し、新しいクラスタの重心点ととする。
4. 重心移動距離が十分に小さくなるまで、2 と 3 を繰り返す。

$$
{\displaystyle \operatorname {arg\,min} _{V_{1},\dotsc ,V_{k}}\sum _{i=1}^{n}\min _{j}\left\|x_{i}-V_{j}\right\|^{2}}
$$

結果は、最初のクラスタのランダムな割り振りに大きく依存します。何度か繰り返して行って最良の結果を選択する手法や、**k-means++法**のように最初のクラスタ中心点の振り方を工夫する手法などが使用されることがあります。

sklearn では、KMeans クラスをインポートして利用できます。

```python
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
```
### 主成分分析(PCA)

**主成分分析（principal component analysis; PCA）**は、相関のある多数の変数から相関のない少数で全体のばらつきを最もよく表す主成分と呼ばれる変数を合成する多変量解析の一手法です。

原理：主成分を与える変換は、第一主成分の分散を最大化し、観測値の変化に対する説明能力を可能な限り主成分に持たせます。続く主成分はそれまでに決定した主成分と直交するという拘束条件の下で分散を最大化するようにして選びます。

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f5/GaussianScatterPCA.svg" width="50%" align="center" />

用途：主成分分析は、**データの次元を削減する**ときの定番的手法です。特に、次元数の多いデータを可視化するとき、主成分分析によってより２次元や３次元に集約することで可視化が容易になります。

sklearn では、PCAクラスをインポートして利用できます。

```python
from sklearn.decomposition import PCA
model = PCA(n_components=2)
```

## 身長と体重からクラスタリング

ここからは、sklearn モジュールの K-means法アルゴリズムを使いながら、
実際にクラスタリングを行っていきます。

<img src="https://miro.medium.com/max/12094/1*IXGsBrC9FnSHGJVw9lDhQA.png" width="40%" align="center"/>

### データ用意と確認

データは、第４回目のコースワークで作成したスポーツ選手の身長と体重を集計した表データを用いてみます。
自分で集計したデータをそのまま利用しても構いませんが、
一応、以下の通り、ダウンロードもできます。

```
!wget https://KuramitsuLab.github.io/data/bmi.csv
```

まず、pandasを使って表データの内容を確認しましょう。
```py
data = pd.read_csv('bmi.csv')
data.head()
```
### 散布図でデータを確認

身長と体重の分布の様子を散布図とヒストグラムで表示して見ましょう。
__散布図__

データは、あらかじめ職業としてクラス分類されているため、
職業ごとに色分けして散布図を書いてみます。
後から、K-means法でクラスタリングした結果も描画しますので、比べてみましょう。
```py
colors = ['blue', 'red', 'green']
ax = None
for i, group in enumerate(data.groupby('職業')):
  ax = group[1].plot(kind='scatter', x='身長', y='体重', alpha=0.3, c=colors[int(i)], ax=ax)
```
重なり具合を確かめるため、ヒストグラムをみて見ましょう。

* 身長は、全ての色が重なっています。
* 体重は、重なっていない部分があります。
```py
for i, group in enumerate(data.groupby('職業')):
  group[1]['身長'].plot(kind='hist', alpha=0.5, bins=20, title='身長')

```
```py
for i, group in enumerate(data.groupby('職業')):
  group[1]['体重'].plot(kind='hist', alpha=0.5, bins=20, title='体重')

```
### ３クラスターに分類
K-means 法は、先にクラスター数（グループ数）を指定して、グループ分けをします。

* クラスタ数: ３種類の職業があったので、とりあえず、３グループ
* 初期状態: `random` （指定しなければ、K-means++法になる）

まず、初期値を与えてモデルを生成します。
```py
from sklearn.cluster import KMeans
model = KMeans(init='random', n_clusters=3)
model

```
今回は、表データのうち、`身長`と`体重`の２属性、つまり２次元データを対象とします。

実際のクラスタリングは、データをフィット(fit)させることで、学習済みモデルを作ります。
```py
model.fit(data[['身長', '体重']])
```
モデルの学習が済んだら、データに対する予想の形で、クラスタ番号を取り出すことができます。
クラスタ番号は、0から$k-1$の番号で表現されます。
```py
model.predict([(170, 80)])
```
表データに各身長と体重から分類されるクラスタを属性として追加してみましょう。
```py
data['クラスタ'] = model.predict(data[['身長', '体重']])
data.head()
```
`クラスタ`ごとに色分けして散布図を書いてみましょう。
```py
ax=None
plt.figure(figsize=(5,5))
for i, gd in enumerate(data.groupby('クラスタ')):
  ax = gd[1].plot(kind='scatter', x='身長', y='体重', c=colors[i], alpha=0.3, ax=ax)

```
必ずしも職業ごとの分布と同じグループ分ではありませんが、３つのクラスターに分類された様子が確認できました。

<div class="admonition warning">

クラスタリングとクラス分類

クラスタリングは、クラス分類が目的ではありません。したがって、職業等のクラス分類と異なったものになります。散布図をみると、クラスタリングは境界に曖昧なところがなく、綺麗に分類されているのが特徴です。
</div>

## エルボー法: 適切なクラスター数を調べる

エルボー法は、クラスターの重心点と所属データ点の距離の総和に着目して、クラスター数を事前に見積もる手法です。

__距離の総和の求め方__
```py
print(model.inertia_)
```
クラスタ数を1から10まで大きくしながら、総和の変化をグラフ化してみます。
```py
dist = []
for i in range(1, 11):
  km = KMeans(init='random', n_clusters=i)
  km.fit(data[['身長', '体重']])
  dist.append(km.inertia_)

plt.xlabel('クラスタ数')
plt.ylabel('距離の総和')
plt.plot(range(1, 11), dist, marker='+')

```
クラスター数が適切になるまでは、総和は相応に減少することが期待できます。
一方、いったん適切な数を超えてしまうと、総和の減少はなくなります。
したがって、クラスター数は2 か 3の辺りが適切なクラスター数といえます。

<div class="admonition note">

エルボー法の由来

適切なクラスター数がエルボー（肘）のように見えるところから

</div>
クラスター数２の散布図を調べてみよう
```py
model = KMeans(init='random', n_clusters=2)
model.fit(data[['身長', '体重']])
data['クラスター'] = model.predict(data[['身長', '体重']])
ax=None
plt.figure(figsize=(5,5))
for i, gd in enumerate(data.groupby('クラスター')):
  ax = gd[1].plot(kind='scatter', x='身長', y='体重', c=colors[i], alpha=0.3, ax=ax)


```
## 乳がんデータと主成分分析

乳がんデータセットは、Breast Cancer Wisconsin (Diagnostic) Data Setに由来し、乳腺腫瘤の穿刺吸引細胞診のデジタル画像から計算されたデータです。


<img src="https://cdn-ak.f.st-hatena.com/images/fotolife/e/ensekitt/20181102/20181102002649.jpg" width="40%"/>

1993 W.N. Street, W.H. Wolberg and O.L. Mangasarian
Nuclear feature extraction for breast tumor diagnosis 
IS&T/SPIE 1993 International Symposium on Electronic Imaging: Science and Technology, volume 1905, pages 861-870, San Jose, CA, 1993. (abstract)
Figure2 図中一部を引用

乳がんのデータを使って主成分分析も試していきます。

__データの用意__

```
!wget https://KuramitsuLab.github.io/data/cancer_ja.csv
```

オリジナルデータを日本語化したデータを用意しました。
良性は`1`、悪性は`0`のフラグがついています。
```py
import pandas as pd
data = pd.read_csv('cancer_ja.csv')
data.head()
```
### データの理解

データの統計量を調べたり、可視化して、データの特徴を捉えましょう。

<div class="admonition note">

Let's try

良性がんと悪性がんの分布に法則性があるか調べてみましょう

</div>

良性か悪性かで色分けして、分布図を書いてみます。属性の組み合わせは、自由に変えて試してみましょう。
```py
colors = ['red', 'green']
plt.figure(figsize=(5,5))
ax=None
for i, gd in enumerate(data.groupby('良性')):
  ax = gd[1].plot(kind='scatter', x='平均半径', y='平均密集度', c=colors[i], alpha=0.3, ax=ax)

```
三次元の散布図を作成したいときは、`Axes3D`をインポートして用います。
```py
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(8,8))
ax = Axes3D(fig)
ax.set_xlabel("平均半径")
ax.set_ylabel("平均密集度")
ax.set_zlabel("平均凹部")
for i, gd in enumerate(data.groupby('良性')):
    ax.plot(gd[1]['平均半径'],gd[1]['平均密集度'],gd[1]['平均凹部'],marker="o",linestyle='None',c=colors[i], alpha=0.3)

```
### 次元削減

乳がんデータは、30次元の変数からなります。
データの特徴を残しながら次元を削減し、表示してみます。
このとき、活用するのが**主成分分析(PCA)**です。

__主成分分析(PCA)による2次元への圧縮__
```py
from sklearn.decomposition import PCA

data_x = data[data.columns[1:]]

pca = PCA(n_components=2)
pca.fit(data_x)

print('固有ベクトル: ', pca.components_)
print('分散:', pca.explained_variance_)
print('分散割合:', pca.explained_variance_ratio_)
```
__主成分分析の結果__

* **固有ベクトル**: `pca.components_`: 新しい特徴空間の軸の向き
* **各主成分の分散**: `pca.explained_variance_` 
* **各主成分の持つ分散割合**: `pca.explained_variance_ratio_`: 第一主成分で98%の情報を保持

さて、主成分分析の結果を用いて乳がんデータを変換しましょう。
```py
data_pca = pca.transform(data_x)  #　主成分分析による変換
print('data_std(shape):', data_x.shape)
print('data_pca(shape):', data_pca.shape)
```
30次元のデータが2次元に削減されていることが確認できるはずです。
なお、`transform()`で得られるデータは、
NumPyの2次元配列なので、表データに変換して、`data_pca`としておきます。
```py
pd.DataFrame(data_pca, columns=['pc1', 'pc2']).head()
```
```py
data_pca = pd.concat([pd.DataFrame(data_pca, columns=['pc1', 'pc2']), data], axis=1)
data_pca.head()
```
第一主成分(pc1)をx軸、第二主成分(pc2)をy軸として散布図を書いてみます。
```py
plt.figure(figsize=(5,5))
ax=None
for i, gd in enumerate(data_pca.groupby('良性')):
  ax = gd[1].plot(kind='scatter', x='pc1', y='pc2', c=colors[i], alpha=0.3, ax=ax)
```
### スケーリング：標準化

乳がんデータは、さまざまな属性が含まれており、単位が異なります。最大値や最小値も大きくばらついています。
```py
data.describe()
```
データ分析では、大きな値の属性があると、分析結果は小さな値の属性の影響が小さくなります。そのような影響を排除するため、スケーリング（標準化）は常套手段です。

__標準化__: サンプル値$x$から平均$\bar{x}$を引き、標準偏差$\sigma$で割る

$$
z = \frac{x - \bar{x}}{\sigma}
$$

sklearnモジュールでは、StandardScaler クラスとして提供されています。
使用法は、PCAクラスと同じで、モデルを学習し、その後、変換します。

__StandardScalerによる標準化__
```py
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# print(data.columns) カラム名
sc.fit(data[data.columns[1:]])

# 標準化
data_std = sc.transform(data[data.columns[1:]])
pd.DataFrame(data_std, columns=data.columns[1:]).head()
```
標準化したデータセットに対し、主成分分析をしてみましょう。
```py
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(data_std)
data_pca = pca.transform(data_std)
print('data_std(shape):', data_std.shape)
print('data_pca(shape):', data_pca.shape)

```
```py
data = pd.concat([pd.DataFrame(data_pca, columns=['pc1', 'pc2']), data], axis=1)
data.head()
```
```py
plt.figure(figsize=(5,5))
ax=None
for i, gd in enumerate(data.groupby('良性')):
  ax = gd[1].plot(kind='scatter', x='pc1', y='pc2', c=colors[i], alpha=0.3, ax=ax)
```
<div class="admonition note">

Let's try

標準化した乳がんデータセットに対して、k-means法でクラスタリングしてみよう。

</div>
## コースワーク

<div class="admonition tip">

**例題（成績表）**

基本情報処理でおなじみの成績データを用いて、３グループに分割してみよう。

1. 成績順にソートしてグループ分けする (属性名: `成績G`)
2. k-means 法でグループに分類する (属性名: `K平均G`)
3. 英数国社理を、理系/文系科目の２次元に減らし、k-means法でグループ分けする
4. 主成分分析を用いて２次元に削減したのち、k-means法でグループ分けする

それぞれのグループ分けの結果を散布図でグラフ化し、特徴など気づいたことを議論してみよう。

</div>

__データ__

次のテキストデータからCSVファイルを作成して作業しましょう。

```
%%file 成績.csv
名前,英,数,国,社,理
佐藤,84,45,77,69,48
鈴木,75,69,65,77,69
高橋,69,81,45,82,79
田中,92,75,83,79,62
伊藤,62,91,68,61,93
渡辺,54,63,48,52,50
山本,48,53,71,83,45
中村,77,85,62,55,82
小林,82,88,89,79,85
加藤,47,48,57,53,63
吉田,75,36,85,73,51
山田,66,73,79,65,66
佐々木,64,95,48,59,91
山口,73,86,52,70,77
松本,55,75,63,67,80
```
