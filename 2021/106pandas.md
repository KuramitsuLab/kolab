# 表データとPandasを使いこなそう

今回は、データ分析と言えば、避けては通れないPandas の使い方を学び、表データの操作を練習します。

## Pandas とは

Pandas とは、表データを扱うPython モジュールで、表計算ソフト (Excel)やリレーショナルデータベースの操作を Python から手軽に行えるようにしてくれます。 

次のように`pandas`モジュールをインポートして使います。

```py
import pandas as pd
```

Pandas は、とても高機能です。

本講義では、Pandas でデータ分析をする必須の機能だけ紹介し、ハンズオン演習で体験します。

* 暗記するものではありません。
* どういうデータ処理や操作ができるか、覚えましょう。
* 使うときは、Google 等で調べながら使ってください。

### データの用意

Pandas の使い方に慣れるために、小さな練習用のデータを作成して、そちらを使って演習していきます。

ファイル書き込み機能(`%%file`)を使って、Colab上でCSVファイル `arashi.csv`を作ります。

```py
%%file arashi.csv
名前,出身,生年,身長,血液型
相葉雅紀,千葉,1982,175,AB
松本潤,東京都,1983,172,A
二宮和也,東京都,1983,168,A
大野智,東京都,1980,166,A
櫻井翔,東京都,1982,171,A
```

<div class="admonition warning">

データが間違っている？

一部間違っていると指摘をよく受けます。
どうぞ、各自でご自由に、ご修正して練習にお使いください。

</div>

CSV ファイルは、表計算ソフト(Excel)のファイルをデータ処理しやすく、カンマ区切り形式のテキストで出力したものです。当然、Excel 等の表計算ソフトで開いてみることができます。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/0dd26ba4-bbfb-a468-6547-56968d575ce0.png" width="60%"/>

もうひとつ、あとから表データの結合をする練習で用いる `junk.csv` (わざと少し壊れたファイル）も作っておきましょう。

```py
%%file junk.csv
name,height,weight
大野智,166,52.0
相葉雅紀,176,58.0
二宮和也,168,52.0
松本潤,173,62.0
カビゴン,210,460.0
```

<div class="admonition note">

Let's try

ちゃんと`arashi.csv`が作成されているか、表計算ソフトで確認してみよう。

</div>

## 基本操作

Pandas は、表データを効率よく操作できます。

Pandas 用語では、表データのことをデータフレーム(DataFrame)と呼びますが、本資料では表データと呼びます。

![dataframe-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/b9d6f05e-df40-4680-a8ad-a1b3f9ee3665.png)

<div class="admonition note">

__覚えておこう：Pandas用語__

* カラム: 列方向のデータ
* インデックス: 行方向のデータ

</div>

### CSVファイルの読み込み

Pandas では、`pd.read_csv()`を用いると、CSVファイルから表データを読み込めます。

```py
data = pd.read_csv('arashi.csv')
data.head()  # 最初の5行のみ表示
```

読み込んで表データは、`data`という名前にしてあります。

表データへの操作は、`data.head()`のようにメソッドで操作します。

### 属性名からカラム(列)を取り出す

Pandas では、属性ごとのデータ処理が多くなります。まず、属性名`'名前'`のデータを取り出してみましょう。

```py
data['名前']
```

取り出した属性データは、Pythonの列(シーケンス）として、`for`文などで処理できます。

```py
for name in data['名前']:
  print(name)
```

### 属性(列データ）の追加

新しい属性、つまり列データを追加してみましょう。

表データ中には、５人分のデータがあるため、リストとして５人分のデータを代入すると、新しい属性を追加することができます。

__例. 性別を追加する__

```py
data['性別'] = ['男性'] * 5 
data #表示
```

<div class="admonition note">

上級者向け: 列に数式を適用する

`apply`を使えば、各列データに関数やラムダ式を適用した列がえられます。

```py
data['年齢'] = data['生年'].apply(lambda x: 2021 - x)
```

</div>

### n行目のデータを取り出す

表データの列ごとへのアクセスは、`.iloc`プロパティを通して行ます。

```py
data.iloc[0]
```

```py
for values in data.iloc[0]:
  print(values)
```

### セルの値

インデックスと属性の組み合わせで、表データをセルの値を指定して取り出すことができます。

```py
data['出身'][0]
```

もしくは

```py
data.iloc[0]['出身']
```

### 表データの出力

Pandas で操作した表データは、`.to_csv()`でCSVファイルに保存できます。

```py
data.to_csv('arashi2.csv', index=False,encoding='utf_8_sig')  #インデックスなしで、文字化けしないようにする
```

<div class="admonition warning">

文字化けを防ぐには？

CSVファイルの文字化けを防ぐには、`encoding='utf_8_sig'`オプションをつけて、先頭にBOMと呼ばれる文字コードを識別する記号をいれます。

</div>


__ちゃんと保存できたか確認してみましょう__

```py
!cat arashi2.csv
```

## データベースの操作

Pandas の[リレーショナル代数](https://ja.wikipedia.org/wiki/%E9%96%A2%E4%BF%82%E4%BB%A3%E6%95%B0_(%E9%96%A2%E4%BF%82%E3%83%A2%E3%83%87%E3%83%AB))の操作をみていきましょう。

データベース実習を履修している人は、SQLを思い出しながら試していきましょう。

<div class="admonition warning">

リレーショナル代数って何？

SQLの元になったデータ操作を集合論をベースに定義した代数系です。
Pandas の操作を覚えるときは、Excel や SQL などの操作と対応付けながら、
マスターしていきましょう。

</div>

### 選択(selection)

選択は、指定した条件に合う行を取り出します。データを抽出するフィルターの役割になります。

__SQL例__

```sql
SELECT * FROM data WHERE '身長 >= 170'
```

```py
data[data['身長'] >= 170]
```

複雑な条件は、`.query()`メソッドを用いて与えることもできます。

```py
data.query('身長 >= 170 and 血液型 == "A"')
```

### 射影(projection)

射影（projection）は、表データから属性を限定した表データを返します。Pandasでは、抽出したい属性名をリストにして渡します。

__SQL例__

```sql
SELECT 名前,生年,血液型 FROM data
```

```py
data[['名前', '生年', '血液型']]
```

### 表の連結

複数のファイルに入っている表データをまとめてひとつにしたいことがあります。
今度は、最初に作ったもう一つのCSVファイル junk.csvを読み込んで、連結してみます。

```py
data2 = pd.read_csv('junk.csv')
data2
```

単純に縦方向に連結したいときは、`pd.concat()`を使って連結します。
（属性名が異なるので、綺麗につながりません）

```py
pd.concat([data, data2]) 
```

横方向に連結したいときは、`axis=1`のオプションをつけます。

```py
pd.concat([data, data2], axis=1)  #横方向に連結
```

### 表データの結合(join)

表データの結合は、ふたつの表データのある属性をキーにして、キーが同じ値であれば一つの行にまとめる操作です。

Pandasでは、`pd.merge()`で結合します。

__`名前`と`name`をキーにする__

```py
pd.merge(data, data2, left_on='名前', right_on='name')

```

ふたつの表データは結合されましたが、データが一部消えてしまいました。
これは、Pandas では何も指定しなければ、一番条件の厳しい内部結合が用いられるためです。

__結合の方法__
* 内部結合 `inner`: 両方にキーが存在するとき結合
* 外部結合 `outer`: どちらか一方にキーが存在するとき結合
* 左外部結合 `left`: 左側にキーが存在するとき 
* 右外部結合 `right`: 右側にキーが存在するとき

`left`が良さそうですが、`outer`で結合してみます。

```py
pd.merge(data, data2, left_on='名前', right_on='name', how='outer')
```

また、属性名が英語だったり、日本だったり不統一です。少し整頓しておきましょう。

```py
# data, data2を外部結合した表データを新しく data とする
data = pd.merge(data, data2, left_on='名前', right_on='name', how='outer')

data.drop('name', axis=1, inplace=True)
data.drop('height', axis=1, inplace=True)
data.drop(5, axis=0, inplace=True)  #index=5を消す
data.rename(columns={'weight': '体重'}, inplace=True)

data
```

<div class="admonition warning">

pandas の表操作は書き換えない

pandas の表操作は、新しい表データを返すようになっています。だから、別の変数名で別の表データとして操作することもできます。

```python
# 新しい表を data2 として操作する 
data2 = data.drop('name', axis=1)
```

だから、同じ変数名で置き換えることもできます。

```python
data = data.drop('name', axis=1)
```

データを直接、書き換えたいときは、`inplace=True`をつけます。

```
data.drop('name', axis=1, inplace=True)
```

</div>

<div class="admonition note">

Let's try

Google で調べて、`data`のカラムの順番を`名前	性別	出身	生年	身長	体重    血液型`に変更してみよう。

（Google で調べて、操作できるようになれば、OKです。）
</div>

## データ分析の準備

次回からPandas を用いて、より本格的なデータ分析を始めます。

### 欠損値のチェック

世の中のデータは、データ値が欠けていることがあります。
今回の練習データでは、`NaN`と表示されている値が、欠損値になります。
データ件数が少ない場合は、目視でみつかる場合がありますが、
データ件数が多くなると、手作業で探すのは無理です。

欠損値をチェックすることが必要になります。

```py
data.isnull().sum()
```

欠損値が見つかったときは、
欠損値を処理するアプローチとしては：

* `dropna()`：データが欠損している行や列を削除する
* `fillna()`：データが欠損している要素を別の値で穴埋めする

どのように処理するかは、データ分析の目的によって異なります。
今回は、メンバーを消してしまったら、大変なことになりますので、
__欠損値の値を平均値で補完する__ことで対応してみます。

```py
data.fillna(data.mean(), inplace=True)
data
```

<div class="admonition note">

欠損値の補完

データ分析では、欠損値は何かの嫌がらせかと思うほど、頻繁に生じます。
色々な補完方法がありますので、適切な方法を選んでください。

```
data['体重'].fillna(50.0)                 # 体重の欠損値を50.0で穴埋め
data['体重'].fillna(data['体重'].mean())   # 体重の欠損値を体重の平均値で穴埋め
data['体重'].fillna(data['体重'].median()) # 体重の欠損値を体重の中央値で穴埋め
data['体重'].fillna(data['体重'].mode())   # 体重の欠損値を体重の最頻値で穴埋め
```

</div>

### グループごとの集計

`groupby()` は、同じ値を持つデータをまとめて、統計処理を行いときに使います。

__例. 血液型ごとに平均(mean)をとる__

```py
data.groupby('血液型').mean()
```

__`describe()`: 基礎統計量を全てみたいとき__

```py
data.groupby('血液型').describe()
```

`groupby()`は、グループごとに集計して操作するときに、重宝します。ただし、返されるのはGroupByオブジェクトで表データとして使えません。

ピボットテーブルを用いると、集計結果を表データに変換して取り出せるようになります。

```py
pd.pivot_table(data, index="血液型")
```

<div class="admonition note">

ピボットテーブルとクロス集計

ピボットテーブルは、クロス集計に使われる便利ツールです。

* `index`: 縦軸に展開するカラムを指定
* `columns`: 横軸に展開するカラムを指定
* `values`: 集約する値カラムを指定
* `aggfunc`: 集約方法を指定

</div>

ぜひ使えるようになりたいところですが、今回のサンプルはデータ件数が少なすぎます。
余力がある人は、次の時系列データで練習してみてください。

## コースワーク

コースワークは、pandasを使ったデータ操作の練習です。

<div class="admonition tip">

**演習（BMI.CSV）**

野球選手(B)、サッカー選手(F)、相撲(W)に関するCSVファイルをまとめ、
次の属性からなるCSVファイルにしよう。

```
名前    身長    体重    職業    BMI
```

1. `職業`は、野球選手`B`、サッカー`F`、相撲`W`とする
2. `BMI` は`身長`と`体重`から計算する
3. 身長の高い順にソートして、`bmi.csv`として保存する
4. 各職業ごとに、`身長`と`体重`の分布図を描画する
5. 各職業ごとにグループ集約し、身長と体重の統計量を求める

</div>

__データの入手先__

鈴木 雅也、渡辺 将人、井上 史斗.
「[数式をプログラムするってつまりこういうこと](https://github.com/massongit/math-program-book)」より、公開データを使わせてもらいます。

データをダウンロードするコマンド
```
!wget https://raw.githubusercontent.com/massongit/math-program-book/master/9_data/サッカー/Jリーグ選手身長体重.csv
!wget https://raw.githubusercontent.com/massongit/math-program-book/master/9_data/プロ野球/プロ野球選手身長体重.csv
!wget https://raw.githubusercontent.com/massongit/math-program-book/master/9_data/相撲/力士身長体重.csv
```


