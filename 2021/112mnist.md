
# 手書き文字の認識

画像データ（手書きの文字）を用いて、画像認識に挑戦してみます。
原理を理解すれば、より複雑な画像認識にも応用することができるようになります。

![imagenet-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/1296178f-4bfd-e03b-2120-4b5278bf5df1.png)

[ImageNet](https://devopedia.org/imagenet)より引用

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

## MNIST

MNIST は、「0」~「9」の手書き数字の画像データセットです。Yann LeCun らによって、手書き文字データセットの NIST データベースから抽出＆加工して、機械学習のチュートリアル用に作成されて公開されています。

ここは、画像データ(手書きの文字)を説明変数 (X)、ラベルを目的変数 (y) として学習モデルを作成してみます。

![mnist-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/d7283850-3cdd-3701-4f56-f7b4ae8090e3.png)

__MNISTデータのロード__

```py
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784')

```

画像データは、`mnist.data`に70000万件、要素数768(28x28)のNumPy配列で登録されています。
画像データのラベルは、`mnist.target`に70000件登録されています。

__画像データとラベルデータの大きさ__

```py
print('画像データ', mnist.data.shape)
print('ラベル', mnist.target.shape)
```

最初の画像データをみてみましょう。
784要素の配列はみにくいので、28x28で表示してみます。
0~255 階調のグレースケールになっています。

```py
print(mnist.data.values[0])
```

<div class="admonition warning">

データ形式の不一致

sklearnのバージョンによっては、mnist.dataの形式が異なるようです。
アクティブに開発が進んでいるプロジェクトでは、こういうことはよくあります。

__落ち着いてデータの形式を調べて対処してください__

```
print(mnist.data)
```

エラーが発生した場合は、`data.values[0]`の代わりに、
次のように`data[0]`のように`.values`を取り除いてください。
</div>

Matplotlibで表示することもできます。0が黒で白が255なので、文字が白くなります。

```py
plt.imshow(mnist.data.values[0].reshape(28,28), cmap=plt.cm.gray)
```

```py
W = 16 # 横に並べる個数
H = 8 # 縦に並べる個数
fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1.0, hspace=0.05, wspace=0.05)
for i in range(W*H):
    ax = fig.add_subplot(H, W, i + 1, xticks=[], yticks=[])
    ax.imshow(mnist.data.values[i].reshape((28, 28)), cmap=plt.cm.gray)
plt.show()
```

機械学習では、28x28 Grayscale の画像データを**784次元の多次元ベクトル** として扱います。

まず、0〜255のグレースケールの値を0.0〜1.0の範囲に正規化しておきます。
その後、ホールドアウト法を用いて学習するので、訓練データとテストデータに分割しておきます。

```py
X = mnist.data.values.reshape(70000, 784) / 255  # [0,1]で正規化
y = mnist.target.values.astype(int)

# 訓練データとテストデータ
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=10000, random_state=0)

print('訓練データ数:', len(X_train))
print('テストデータ数:', len(X_test))

```

### 画像データの分布 (寄り道)

画像データ(多次元ベクトル)を２次元に次元圧縮して、
手書き文字がどのように分布しているかみてみましょう。

__1000枚だけ選んでPCAで次元圧縮__

```py
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca.fit(X[:1000])  # 1000枚選ぶ
pc12 = pca.transform(X[:1000])
```

__表データに変換__

```py
data = pd.concat([pd.DataFrame(pc12, columns=['pc1', 'pc2']), pd.DataFrame(y[:1000], columns=['label'])], axis=1)
data.head()
```

__散布図を描画する__

```py
colors =  ["r", "g", "b", "c", "m", "y", "k", "orange", "pink", 'violet']
plt.figure(figsize=(15,15))
ax = None
for i, df in enumerate(data.head(3000).groupby('label')):
  ax = df[1].plot(kind='scatter', x='pc1', y='pc2', alpha=0.3, c=colors[int(i)], label=df[0], ax=ax)
plt.legend()
plt.show()
```

結構、ごちゃごちゃに重なっているところがあります。綺麗に分類できるのでしょうか？

## 多層パーセプトロン

ニューラルネットワークで紹介した多層パーセプトロン(MLPClassifier)を使ってみます。

MLPClassifier は、パーセプトロンで説明したとおり、豊富なオプションがあります。

__hidden_layer_sizes__: 中間層のサイズを設定します。

中間層が 3 つ (各中間層のニューロン数が 100 個、200 個、100 個) の 5 層ニューラル ネットワークを設定したいときは、次のように設定します。

```
hidden_layer_sizes=(100, 200, 100)
```

__activation__: 中間層の活性化関数

* identity:恒等関数
* logistic:シグモイド関数
* tanh:双曲線正接関数
* relu:ランプ関数

__solver__: 重みの最適化手法

* lbfgs:準ニュートン法に属す BFGS の一種
* sgd:確率的勾配降下法
* adam:確率的勾配降下法にモーメントをつける

__max_iter__: エポック数

今回は、３層パーセプトロンで、前回ならったとおり、活性化関数はシグモイド関数、最適化は確率的勾配降下法を用いてみます。

```py
from sklearn.neural_network import MLPClassifier

model = MLPClassifier(hidden_layer_sizes=(128,), activation='logistic', solver='sgd', max_iter=20, verbose=10, random_state=0)
```

訓練データを学習させます。

```py
history = model.fit(X_train, y_train)
```

<div class="admonition warning">

**ConvergenceWarning：収束が不十分**

Epoch数が足りないので、収束が不十分だと言われます。

</div>

`history`は学習の様子を記録したログデータです。
Matplotlibで表示してみると、学習の進捗をみることができます。

```py
plt.plot(history.loss_curve_)
plt.xlabel('Iteration') 
plt.ylabel('loss') 
plt.grid(True)
```

損失 (loss) が減少しているときは、順調に学習が進んでいます。

```py
y_pred = model.predict(X_test)
```

```py
#fig.subplots_adjust(left=0, right=1, bottom=0, top=1.0, hspace=0.05, wspace=0.05)

def plot_mnist(X, y):
    fig = plt.figure()
    for i in range(10):
        ax = fig.add_subplot(1, 10, i + 1, xticks=[], yticks=[])
        ax.imshow(X[i].reshape((28, 28)), cmap=plt.cm.gray_r) #白黒反転
    print(y[:10])
    plt.show()

plot_mnist(X_test, y_pred)
```

### 正解率

```py
print('正解率(train)', model.score(X_train, y_train))
print('正解率(test)', model.score(X_test, y_test))

```

ひと昔前は、ハガキの郵便番号を読み取って、自動的に仕分けする装置であっても、
70%の正確さも出ませんでした。それに比べると、素晴らしい正解率です。

<div class="admonition danger">

Let's try

MLPClassfierのパラメータを変更して、正解率がどう変わるか調べてみよう。

__最近のニューラルネットワークの定番パラメータ__

- 隠れ層を増やす
- 活性化関数: `relu`
- 最適化: `adam`

</div>

<div class="admonition note">

PyTorch, TensorFlow, Kelas

深層学習技術は、近年、高度化してきています。
より細かくネットワークの構成やパラメータを設定できる
PyTorch, Tensorflow, Kelas,  などのニューラルネットワーク・ライブラリが登場しています。

__PyTorchによるモデル構築の例__

```python
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
```

興味のある人は、
PytorchやTensorflowなどニューラルネットワークを構築してみてください。
より高い正解度のモデルを構築することができます。
（なお、研究レベルの予測モデルを使るときは、
このようなニューラルネットワークフレームワークを活用することになります。）

</div>

## 自分の手書き文字を認識する

最後に、自分自身で書いた手書き文字を認識してみましょう。

紙を用意して数字を書いて、スマホで撮影します。
１文字だけ適当に切り出して、ファイルに保存してみてください。

### Pillow/PIL ライブラリ

画像は、Pillow/PIL ライブラリを用いて操作します。
まずColab上で自分のファイル（例.`2.png`）を読み込めるか、表示して確認しておきます。

```py
from PIL import Image
im = Image.open("2.png")
print('サイズ', im.size)
im
```

MNIST用のモデルの画像ファイルは、
グレースケールの28x28なので、Pillow/PIL ライブラリを用いて変換します。

```py
im = Image.open("2.png").convert('L').resize((28,28))
print('サイズ', im.size)
im
```

このPillow画像データをNumPy配列に変換し、784次元のデータにします。

```py
myimage = np.array(im).reshape(1,-1)
myimage.shape
```

MNISTのモデルは、白黒が反転している画像で学習しているため、白黒を反転させて、0.0〜1.0に正規化します。これで入力データはできました。

```py
myimage = (255 - myimage)/255
```

それでは、学習済みのモデルを使って予測してみましょう。(正しく予想できるかな？)

```py
model.predict(myimage)
```

### アプリケーションへの組み込み

人工知能アプリケーションに学習済みモデルを組み込むときは、毎回学習しなくて済むように学習済みモデルだけ、pickle形式のファイルに保存しておきます。

<div class="admonition note">

pickle

Pythonでのオブジェクトをシリアライズする一般的な方法です。**シリアライズ（直列化）**とは、プログラミング言語においてオブジェクトをバイト列のデータに表現に変換することです。逆に、**デシリアライズ（非直列化）**とは、シリアライズしたバイト列から元のオブジェクトに復元することです。

</div>

__モデルの保存__

```py
import pickle
with open('mnist-model.pickle', mode='wb') as fp:
    pickle.dump(model, fp)
```

保存されたファイルの大きさは1.6Mバイト程度になります。
（もちろん、学習したデータやパラメータにもよります。）

```py
!ls -l mnist-model.pickle
```

__モデルのロード__

```py
import pickle
with open('mnist-model.pickle', mode='rb') as fp:
    model = pickle.load(fp)
model.predict(myimage)
```

## コースワーク

<div class="admonition danger">

**演習（画像処理）**

[Fashin-MNIST](https://github.com/zalandoresearch/fashion-mnist)の画像データを使って、
ファッションアイテムの分類をしてみよう。

![fashionmnist-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/6de529e7-2652-4429-8b34-a662b61236b8.png)

</div>

__データの入手方法__

```
from sklearn.datasets import fetch_openml
fashion_mnist = fetch_openml('Fashion-MNIST')
```
