# 条件分岐と繰り返し

プログラムは、原則、上から順番に[A]→[B]のように評価してゆきます。

![code_seq-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/7b643ba4-a47c-8d36-6639-d85e1e1d5a78.png)

しかし、**条件によっては、評価するプログラムを[X]か[Y]のように切り替えたい**ことがあります。
そのようなときは、**if文と呼ばれる制御構造**を用います。

![code_if-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/555f7c9d-15b4-1d0b-e593-aa581b4ae16a.png)

**if文**や条件分岐の考え方は難しいものではありません。少し例題をときながら書いていきましょう。

<div class="admonition note" style="background: #eeffee">

**例題: 食べ過ぎに注意**

ユーザから身長(cm)と体重(kg)を入力し、BMI25以上なら、「食べ過ぎに注意」と警告するプログラムを書きましょう。

</div>

`if`は、分岐されるプログラムの部分をインデントすることで区別します。

```py
h = input("身長(cm)は?")
w = input("体重(kg)は?")

h = h / 100 # cm から mに変換
BMI = w / h**2

if BMI >= 25.0:
    print("食べ過ぎに注意")
```

## 数当てゲーム

数当てゲームとは、コンピュータが生成した０〜１００の整数をユーザが当てるまでの回数を競うゲームです。コンピュータは、ユーザが正解を当てるまで、「大き過ぎる」「小さ過ぎる」とヒント、ユーザが入力した数値のヒントを返します。

### 乱数

```py
import random
x = random.randint(0, 10)
```

```
print('@x', x)
```

### ユーザの入力

まず、ユーザに整数`y`を入力させ、`x`と等しければ`"正解"`、もし小さければ`"小さ過ぎる"`、そうでなければ`"大き過ぎる"`と表示するようにします。

```py
import random
x = random.randint(0, 10)

y = int(input('数字を当ててみて'))
if x == y:
    print('正解')
elif y < x:
    print('小さ過ぎる')
else y > x:
    print('大き過ぎる')

```

### 繰り返しの構文

もちろん、一回で当てられるのはまれです。繰り返して、ユーザに数当てしてもらうようにします。ここで、繰り返しの構文`while`文か`for`文を使います。

while文は、特殊な条件分岐の構文になります。
if文の代わりに、while文を用いると、
**条件PがTrueの間はブロック`[X]`を繰り返し**ます。

![code_while-fs8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/57754/975ed466-4bfa-9560-230a-faa0a09f97e1.png)


### while文 

次は、while文に


```py
import random
x = random.randint(0, 10)

y = int(input('数字を当ててみて'))
c = 1

while x != y : # 等しくない間、繰り返す
    if y < x:
        print('小さ過ぎる')
    else y > x:
        print('大き過ぎる')
    y = int(input('数字を当ててみて'))
    c += 1  # c = c + 1

print('正解')
print(c, '回で当てました！')
```

<div class="alert warning-info" style="background: #ffeeee">

**無限ループ**



</div>


### for文

`for文`は、指定された回数繰り返す構文です。
プログラム中で繰り返す部分を`for`文のブロックに入れます。

`break`文は、`while`文や`for`文による繰り返しを強制的に中断する制御構造です。`break`文を使うと、xとyが等しいとき、繰り返しを中断するようにします。


```py
import random
x = random.randint(0, 10)

for c in range(10):
    y = int(input('数字を当ててみて'))
    if x == y:
        print('正解')
        print(c, '回で当てました！')
        break
    elif y < x:
        print('小さ過ぎる')
    else y > x:
        print('大き過ぎる')

```

<div class="admonition note" style="background: #eeeeff">

### Let's try

ユーザが3回以内で正解を当てられないときは、コンピュータの勝ちになるように直してみよう。(ユーザに、あと何回と答えられる回数を教えてあげましょう。)

</div>

## 丹治郎の模様



## ソウルナンバー占い

BMIは、

<div class="admonition note" style="background: #eeffee">

あなたと相手の誕生日を聞いて、相性を占ってあげましょう。

</div>

# グラフを書いてみよう