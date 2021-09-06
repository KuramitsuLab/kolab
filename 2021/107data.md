# データの傾向をつかもう

いよいよ、データを使って統計分析する手法を学んでいきます。

今回は、Pandas と グラフ描画を組み合わせて、データの可視化による分析を学びます。

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
## データ入手

今回は、[ポルトガルの高校生の数学の成績データ](https://archive.ics.uci.edu/ml/datasets/student+performance)を使って、データ解析をします。

<img src="https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/315e0d53-5fed-3f10-db50-eda9ece4f5f9.jpeg" width="40%"/>


__データの取り寄せ__

```bash
!wget https://kuramitsulab.github.io/data/student-mat.csv
```

<div class="admonition note">

wget

URLからファイルをダウンロードするUNIXコマンドです。
Colab上にファイルをアップロードするとき、重宝します。

</div>


### データの内容確認

`student-mat.csv`をデータフレームとして読み込みます。
```py
data = pd.read_csv('./student-mat.csv')
data.head() #最初の5行を確認
```
```py
data.tail() # 最後の5行を確認
```
### データの属性を確認する

新しいデータをロードしたとき、最初に行うことは**データの属性**を確認することです。

|属性名   |説明   |
|--------|------|
|`school`|学校名 |
|`sex`   |性別 `F`: 女性, `M`: 男性  |
|`age`   |年齢   |
|`address`|居住地 `U`: 都市部, `R`: 地方 |
|`famsize`   |性別 `F`: 女性, `M`: 男性  |
|`Pstatus`   |同居 `T`: 同居, `A`: 寮  |
|`Medu`| 母親の学歴 |
|`Fedu`| 父親の学歴 |
|`Mjob`| 母親の職業 |
|`Fjob`| 父親の職業 |
|`reason`| 学校を選んだ理由 |
|`guardian`| 保護者は誰か？ |
|`traveltime`| 通学時間 |
|`studytime`| 週の勉強時間 |
|`failures`| 過去の落第数 |
|`schoolsup`| 補修 |
|`famsup`| 家族からのサポート |
|`paid`| 塾 |
|`activities`| 部活動 |
|`nursery`| 保育園 |
|`higher`| 高等教育 |
|`internet`| インターネット接続 |
|`romantic`| 恋人 |
|`famrel`| 家族関係 |
|`freetime`| 自由時間 |
|`goout`| 友人と遊ぶ頻度 |
|`Dalc`| 平日のアルコール量 |
|`Walc`| 週末のアルコール量 |
|`health`| 健康状態 |
|`absense`| 欠席数 |
|`G1`| 一学期の成績 (０〜２０) |
|`G2`| 二学期の成績 (０〜２０) |
|`G3`| 最終成績 (０〜２０) |

ポルトガルの高校なので、日本人の感覚からすると？？？なところもありますが、
上記の情報が含まれています。

<div class="admonition note">

ここからのミッション

高校生の各属性が数学の成績(G1, G2, G3)、特に最終成績(G3)に与える影響を調べていきましょう。
(ちなみに、`G3`が0.0の学生は、ドロップアウトしてしまった学生です。エラーではありません。)

</div>
### データの形式を確認する

データの属性を確認したら、次は属性がどのような形式で入っているか確認します。

データの`.info()`を呼ぶと、属性とデータ形式のリストを表示してくれます。
```py
data.info()
```
データの属性名に続いて、データの個数、さらに形式が`int64`か`object`か示されています。

* `int64`: 数値データ
* `object`: 文字列データ

重要なのは、**数値データ（量的データ）**、**カテゴリデータ（質的データ）**を区別することです。

* **数値データ**: 量が数値によって連続的に表現されるデータであり、基本的に比較可能。（例. 人数や金額など)
* **カテゴリデータ**: カテゴリやグループを表す不連続のデータ

少し注意したいのは、カテゴリデータであっても、カテゴリの種類が数値で表現されていると、`int64`形式となります。
同じく、カテゴリデータであっても、論理値などの比較可能な数値に変換できるものがあります。

`Medu`や`Fedu`は、カテゴリの種類が数値で入っていますが、数値データ(`int64`)と解釈されていますが、カテゴリデータとして処理したいなら、型を`object`に変更しておくとよいでしょう。
```py
data['Medu'] = data['Medu'].astype('object')
data['Fedu'] = data['Fedu'].astype('object')

```

<div class="admonition note">

カテゴリから数値データへの変換

次のように`.map()`を行えば、カテゴリーデータも数値データに変換できます。

```
data['school']=data['school'].map({'GP':0, 'MS':1})
data['sex']=data['sex'].map({'M':0 ,'F':1})
data['address']=data['address'].map({'R':0 ,'U':1})
data['famsize']=data['famsize'].map({'LE3':0 ,'GT3':1})
data['Pstatus']=data['Pstatus'].map({'A':0 ,'T':1})
data['Mjob']=data['Mjob'].map({'at_home':0 ,'services':1, 'teacher':2, 'health':3, 'other':4})
data['Fjob']=data['Fjob'].map({'at_home':0 ,'services':1, 'teacher':2, 'health':3, 'other':4})
data['famsup']=data['famsup'].map({'no':0, 'yes':1})
data['reason']=data['reason'].map({'course':0 ,'home':1, 'reputation':2, 'other':3})
data['guardian']=data['guardian'].map({'mother':0 ,'father':1, 'other':2})
data['schoolsup']=data['schoolsup'].map({'no':0, 'yes':1})
data['paid']=data['paid'].map({'no':0, 'yes':1})
data['activities']=data['activities'].map({'no':0, 'yes':1})
data['nursery']=data['nursery'].map({'no':0, 'yes':1})
data['higher']=data['higher'].map({'no':0, 'yes':1})
data['internet']=data['internet'].map({'no':0, 'yes':1})
data['romantic']=data['romantic'].map({'no':0, 'yes':1})
```

</div>


### カテゴリデータの確認

`data.dtypes`が`object`あるものをカテゴリデータとみなして、
カテゴリデータの属性リストを取り出しています。
```py
# カテゴリデータのリストを取り出す
print(list(data.dtypes[data.dtypes == 'object'].index))

```
各カテゴリデータがどのような値が含まれるか、調べます。
```py
# カテゴリデータの値の調べる
for cat_feat in data.dtypes[data.dtypes == 'object'].index:
    print(cat_feat)
    print(data[cat_feat].value_counts())
    print()
```
<div class="admonition warning">

Pandas 力をあげるためには？

Pandas は高機能で、Google で調べるといってもなかなか求めている機能を探すことが難しいです。
最初のうちは、よくわからないコードが出てきたら、地道にひとつずつ動きを確認するようにしましょう。

```
data.dtypes
data.dtypes == 'object'
data.dtypes[data.dtypes == 'object']
data.dtypes[data.dtypes == 'object'].index
```

こういう地道な努力がプログラミング向上に繋がります。

</div>
### 数値データの要約

`describe()`は、数値データの基礎統計量を集計するメソッドです。

__基礎統計量__

* `count`: データ数
* `mean`: 平均値
* `std`: 標準偏差
* `min`: 最小値
* `25%`: 小さい方から25%目の値（第一四分位点）
* `50%`: 中央値
* `75%`: 小さい方から75%目の値（第三四分位点）
* `max`: 最大値

ざっくりと傾向をみるとき、重宝します。
```py
data.describe()
```
## 可視化

表データは、数値や統計量だけみていても、データの傾向をつかめません。


<div class="admonition note">

Let's try

ここから例として、`G3`列を示しますが、他の属性も自分で調べてみましょう。

</div>

さて、それではMatplotlib を用いてデータの可視化していきましょう。

### 箱ひげ図

箱ひげ図は、最大値、最小値、中央値、四分位範囲を視覚化してくれるグラフです。
ヒゲの上端が最大値、ヒゲの下端が最小値を示します。データの範囲がみえてきます。

__最終成績(G3)の統計量__
```py
data['G3'].describe()
```
__最終成績(G3)の箱ヒゲ図__
```py
plt.boxplot(data['G3'])
plt.grid(True)

```
```py
## G1, G2, G3 と表示する例
plt.boxplot([data['G1'], data['G2'], data['G3']])
plt.grid(True)
```
seaborn の`boxplot()`を用いれば、もう少しこった凝ったヒストグラムを描画できます。
```py
sns.boxplot(x=data['Fjob'],y=data['G3'])
plt.title('父親の仕事が子供の成績に与える影響')
plt.xlabel('父親の仕事')
plt.ylabel('成績')
plt.show()
```
```py
## subplot を使った凝ったグラフ

plt.figure(figsize= (15,5))
plt.subplot(1,2,1)
order_by = data.groupby('Fjob')['G3'].median().sort_values(ascending = False).index
sns.boxplot(x = data['Fjob'], y = data['G3'],order = order_by)
plt.xticks(rotation = 90)
plt.title('Fjob v/s G3')

plt.subplot(1,2,2)
order_by = data.groupby('Mjob')['G3'].median().sort_values(ascending = False).index
sns.boxplot(x = data['Mjob'], y = data['G3'],order = order_by)
plt.xticks(rotation = 90)
plt.title('Mjob v/s G3')

plt.show()
```
<div class="admonition note">

可視化の達人になるためには

皆さんから、先生のようにPandasやMatplotlibを使いこなせるようになりたいと言われますが、
過去に書いたグラフを直しながら、必要に応じてGoogleで調べて、書き直しているだけです。
とにかく、色々なグラフを書いて試してみて、
後で探しやすいようにColabのノートブックでライブラリを作っておきましょう。

</div>
### ヒストグラム

おなじみのヒストグラムも描画してみましょう。

__最終成績(G3)のヒストグラム__
```py
plt.hist(data['G3'], bins=20, range=[0,21], rwidth=0.8)
plt.title('Distribution of grades average of students')
plt.xlabel('G3')
plt.ylabel('Count')
plt.show()
```
```py
sns.countplot(x=data['G3'], palette='gray_r')
sns.set_theme(style="whitegrid")
plt.xlabel('G3')
plt.ylabel('Count')
plt.show()
```
__グループ分けされたヒストグラム__

`hue`を追加すると、カテゴリーごとに色分けされたヒストグラムが得られます。
```py
sns.countplot(x='G3',hue='sex', data=data)
plt.title('Students distribution according to G3 and sex')
plt.xlabel('G3')
plt.ylabel('Count')
plt.show()
```
__カーネル密度推定法によるヒストグラム__
```py

sns.kdeplot(data.groupby('sex').get_group('M')['G3'], shade = True,label = 'male')
sns.kdeplot(data.groupby('sex').get_group('F')['G3'], shade = True, label = 'female')
plt.xlabel('G3')
plt.ylabel('% data distribution')
plt.show()
```
### 散布図と相関係数

ここまでは、基本的にひとつの属性に着目してきました。
データサイエンスや機械学習では、**２つの属性間の関係性**がより重要になります。

属性間の関係性により注目するため、散布図と相関係数を学びます。

__一学期の成績(G1)と最終成績(G3)__
```py
plt.scatter(data['G3'], data['G1'], marker='o')
plt.xlabel('G3')
plt.ylabel('G1')
plt.grid(True)
```
第一学期から成績が良い学生が最終成績の成績がよくなる傾向がグラフから読み取ることができます。

この関係性を数値化する手法が、[相関係数](https://ja.wikipedia.org/wiki/相関係数)です。

* 1に近いほど、正の相関がある
* 0無相関
* -1に近いほど、負の相関がある

Python では、SciPy に含まれている`pearsonr`を使って相関係数を算出できます。

__G3とG1の相関係数__

```py
import scipy as sp
sp.stats.pearsonr(data['G1'], data['G3'])
```
ひとつ目の値が相関係数です。（ふたつ目の値は、p値です。）

<div class="admonition note">

p値

偶然、実際に反した数値が統計量として計算される確率です。p値が低いほど、ありえないことが起きたことになります。

</div>

#### 線形近似（予習）

成績G3とG1の関係を$y = ax + b$という線形近似をしてみます。

次回以降用いる機械学習モジュール`sklearn`を予習として用いて、
[最小二乗法](https://ja.wikipedia.org/wiki/最小二乗法)によって、$a$(回帰係数)と$b$(切片)を求めます。

__線形近似__
```py
from sklearn import linear_model
reg = linear_model.LinearRegression()
X = data.loc[:, ['G3']].values
Y = data['G1'].values
reg.fit(X, Y)
print('a=', reg.coef_, ', b=', reg.intercept_)
```
```py
plt.scatter(X, Y)
plt.xlabel('G3')
plt.ylabel('G1')

plt.plot(X, reg.predict(X), color='red') # y=ax+bを描画
plt.grid(True)
```
<div class="admonition warning">

詳しくは

[第7回目 線形回帰](ds07reg.html)でもう一度勉強します。

</div>
## 可視化（プロの技）

最後に、少しデータサイエンスの可視化テクニックを紹介します。

### 相関行列とヒートマップ

相関行列は、すべての属性（数値データ間）で相関係数を計算した行列です。

__相関行列__
```py
data.corr()
```
ご多分に漏れず、可視化しておくとデータ解析が行やすいです。
```py
# Correlation matrix
corr = data.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr, annot=True)
```
### ヒストグラムと散布図をまとめて書く

seabornモジュールの`pairplot`を用いると、さまざまな属性の関係性を一度に確認できます。

* 欠席数`absences`
* アルコール摂取量`Dalc`
* 年齢`age`
* 最終成績`G3`
```py
sns.pairplot(data[['absences', 'Dalc', 'age', 'G3']])
```
```py
sns.pairplot(data[['absences', 'Dalc', 'age', 'G3', 'sex']], hue='sex')
```
### カテゴリーデータを視覚化する

カテゴリデータの分類がどのように散らばっているか一覧を作ります。
```py
plt.figure(figsize = (15,15))
for i,item in enumerate(['school', 'sex', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
       'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
       'nursery', 'higher', 'internet', 'romantic']):
    plt.subplot(4,4,i+1)
    sns.countplot(data=data, x=item)
    plt.title(item)

plt.show()   
```

## コースワーク

<div class="admonition tip">

**演習（ランチボックス）**

カフェフロアで販売されているお弁当の販売数のデータを可視化して、
販売数`y`を増やすため、特徴をつかんでみよう。

|属性|説明|
|--------|----|
|datetid|インデックスとして使用する日付|
|y|販売数|
|week|曜日（月～金）|
|soldout|完売フラグ（0:完売せず、1:完売）
|name|メインメニュー
|kcal|おかずのカロリー（kcal）|
|remarks|特記事項|
|event|社内イベント|
|payday|給料日フラグ（1:給料日）|
|weather|天気|
|precipitation|降水量|
|temperature|気温|

* 販売数`y`の影響を与える属性は？
* 販売数`y`


</div>

__データの入手方法__

[SIGNATE社のコンテスト用データ](https://signate.jp/competitions/24)を
利用させていただきます。データの入手法の詳細は授業中に紹介します。


<!--
! wget http://kuramitsulab.github.io/data/bento_train.csv
! wget http://kuramitsulab.github.io/data/bento_test.csv
-->
