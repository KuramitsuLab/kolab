### ユニバーサル関数

NumPyの配列上で、要素ごとに演算を行い、同一サイズの配列を返す関数を[ユニバーサル関数](https://docs.pyq.jp/python/pydata/numpy/universal_function.html)といいます。

__例: sin(x)のユニバーサル関数__


```py
a = np.array([0.0, 0.1, 0.2])
np.sin(a)

```
<div class="admonition note">

ユニバーサル関数と高階関数map

ユニバーサル関数は、要するに高階関数のmapやリスト内包記法を組み合わせるのと同じですが、こちらの方がより高速に処理できます。

__map関数__
```
np.array(map(sin, a))  #　np.sin(a)と同じ
```

__リスト内包記法__
```
np.array([sin(x) for x in a])　#　np.sin(a)と同じ
```

</div>

### フィルタ


### 次元の変更

`reshape`を用いれば、次元を変更し、ベクトルと行列（２次元配列）を変換できます。

```py
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
a.reshape(3, 3)
```

<div class="admonition note">

行列の計算

Numpyの真価が発機されるのは、行列演算に応用したときです。
本講義では、行列演算は深入りしませんが、
興味があったら行列計算についても調べてみよう。

</div>


## 時系列データ(★)

時系列データとは、時間の順番に並んだデータです。
**コンピュータが記録するデータ（ログ）**は、時系列データになっていることが多く、
データ分析を始める前に理解しやすい形に集計しなおす必要があります。

<div class="admonition warning">

この節は、Pandas 初心者は、スキップして構いません。

時系列データは、データサイエンスの前処理で重要なデータ形式です。

しかし、初めて Pandas を習ったような場合は、
内容が多すぎて理解が追いつかなくなる可能性があります。
（スキップしてもらって、[コースワーク](#コースワーク)に進んでもらって構いません。）

</div>

__データの入手__

UNIXコマンド `wget`で以下のURLから取り寄せてください。

```
!wget https://KuramitsuLab.github.io/data/elearn2018.csv
```
```py
data = pd.read_csv('elearn2018.csv')
data.head()
```
データの内容は、E-ラーニング教材の学習ログです。

* 解答者(name)
* 解答した時間(date)
* 問題番号(problem)
* 得点（point)

__解答者一覧と回答数__

解答者ごとの回答数を調べてみましょう。
```py
data['name'].value_counts()
```

### 日付

学習ログの日付は、文字列として記録されています。
このまま処理しても構いませんが、扱いやすいようにpandas の日付データに変換しておきます。
```py
data['date'] = pd.to_datetime(data['date'])
data.head()
```
すると、日付はメソッド操作で様々な値に変換しやすくなります。
```py
print('日付', data['date'][0])
print('年', data['date'][0].year)
print('エポック秒', int(data['date'][0].timestamp()))
```
エポック秒とは、UNIX上で使われる1970年1月1日を起点にした秒です。
エポック秒に変換すると、整数値として、日付が処理しやすくなります。
エポック秒に変換し、新しいカラム`epoch`を作っておきましょう。
```py
data['epoch'] = data['date'].map(pd.Timestamp.timestamp).astype(int)
data
```
ここから、2018年５月１日を起点に、一週間ごとにデータを区切って、各週ごとの学習状況をみてみたいと思います。

__2018年5月1日のエポック秒を調べる__
```py
import datetime
import time
d = datetime.datetime(2018, 5, 1, 0, 0, 0) # 2018/05/01 のエポック秒
int(time.mktime(d.timetuple()))
```
一週間の秒数から、区切りの境界になるエポック秒をリスト化します。
```py
epoch_of_week = 7 * 24 * 60 * 60
bins = [1525132800 + i * epoch_of_week for i in range(0, 21)]
print(bins)

```
<div class="admonition note">

ビン分割（ビニング処理）

連続値を任意の境界値で区切りカテゴリ分けして離散値に変換する処理のこと

</div>

Pandasでは、`pd.cut()`でビン分割します。ラベルは、第１週を1とします。
```py
data['week'] = pd.cut(data['epoch'], bins, labels=list(range(1,21))).astype(int)
data
```
### クロス集計

週単位でビン分割できたので、各週ごとの集計ができるようになりました。

__週ごとの得点集計__
```py
data.groupby('week')['point'].sum()
```
ピボット表を用いると横軸も指定できます。

__各週ごとに各個人の得点集計__
```py
pd.pivot_table(data, index="week", columns="name", values="point", aggfunc=sum)
```
軸を変えてみましょう。
縦軸を個人ごとに変更し、横軸に各問題ごとの解答状況を並べてみます。
```py
pd.pivot_table(data, index='name', columns='problem', values='point', aggfunc=max)
```
少し早足でしたが、時系列データを参考にクロス集計を試してみました。
パラメータを変更しながら、どのように変わるかみて、理解を深めてください。

