# 計算はPythonにさせてしまおう

Pythonを用いて計算問題をときながら、「Python 勘」を取り戻していきましょう。

今回は、数学や物理を学ぶときにも「Pythonは便利だな」と思わず感じてしまう 
SymPy と代数計算を紹介します。

## SymPyとは

[SymPy](https://www.sympy.org/en/index.html) は、Mathematica や Maple の代替を目指して開発が進められている Python の代数計算ライブラリです。

初歩的な数学の問題を解くときに重宝します。

### 準備

最初に、SymPy のモジュールをインポートします。
```py
from sympy import *
```
Colab上では、数式をmathjax で表示できるように設定しておくとよいでしょう。
```python
def custom_latex_printer(exp,**options):
    from google.colab.output._publish import javascript
    url = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js"
    javascript(url=url)
    return printing.latex(exp,**options)
init_printing(use_latex="mathjax",latex_printer=custom_latex_printer)
```
## 代数計算とは

代数操作とは、数式を数値として計算することなく、シンボル(代数)の操作として計算することです。

__数値計算(従来)__
```py
x = 1
y = 2
x + y + y + x + x
```
代数計算では、変数はシンボルであると宣言します。
すると、変数に数値を代入することなく、シンボルのまま計算されます。

__代数計算(SymPy)__
```py
x = Symbol('x')
y = Symbol('y')

x + y + y + x + x
```
`x`も`y`も代数式なので、代入された`z`も代数式となります。
```py
z = x + y + y + x + x
z
```
また、代数式に対するPythonの演算は、**代数操作**となります。
```py
z ** 2
```
### 関数や定数

三角関数、 𝜋  などは、SymPyからインポートされたものを用います。



```py
sin(pi/3)
```
### 数値解の求め方

数値解を求めたいときは、`float()`を用います。

```py
float(sin(pi/3))
```
<div class="admonition tip">

**例題（代数式）**

次の式を書いてみよう

1.   $\sin{x}+\cos{y}$
2.   $e^{x}$
3.   $\frac{x+xy}{x}$

</div>
```py
sin(x)+cos(y)
```
```py
E**x
```
```py
(x+x*y)/x
```
## 基本的な代数操作

数学でおなじみの代数操作（式の変形）を使ってみましょう。

1.   展開 (expand)
2.   因数分解(factor)
3.   簡易化 (symplify)
4.   代入 (substitution)

<div class="admonition warning">

Pythonは英語

Pythonの関数名やメソッド名は、英語か英語の省略した名称になっています。
英語に強いと意味はすぐにわかりますが、英語だと認識しないとアルファベット列です。
関数を覚えるときは、（辞書で意味を調べて）**英単語**も同時に覚えるようにしましょう。

</div>

__準備__

x, y, z をシンボルとします。
```py
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
```
### 式の展開

式を展開するときは、`expand()`を用います。

__例.__ $(x+y)^3$の展開

```py
(x+y)**3
```
```py
expand((x+y)**3)
```
三角関数が含まれるときは、`trig=True`を追加します。

__例__. $cos(x+y)$
```py
expand(cos(x + y), trig=True)
```
部分分数への展開は`apart()`を用います。

__例.__ $\frac{1}{x(x+1)}$
```py
1/(x*(x+1))
```
```py
apart(1/(x*(x+1)))
```
### 因数分解

式を因数分解するときは、`factor()`を用います。

__例.__ (受験でお馴染みの)$x^3+y^3+z^3 - 3xyz$の因数分解
```py
x**3 + y**3 + z**3 - 3*x*y*z
```
```py
factor(x**3+y**3+z**3-3*x*y*z)
```
### 式の簡略化

式を簡易化するときは`simplify()`を用います。

__例.__ $\frac{x+xy}{x}$ の簡略化
```py
simplify((x + x*y)/x)
```
三角関数を含む式を簡略化したいときは、`trigsimp()` を用います。

例. $\cos^2{x}-\sin^2{x}$
```py
trigsimp(cos(x)**2 - sin(x)**2)
```
### 式の代入

式への代入は、subs()メソッドを用います。

__例.__ $x^3+y^3+z^3-3xyz$ の$z$に1を代入する
```py
(x**3+y**3+z**3-3*x*y*z).subs(z, 1)
```
## 方程式の解法

`solve()`を用いると、方程式の解を求めることができる。

__例.__ $x^4=1$のxの解
```py
solve(x**4-1, x)
```
連立方程式は、リストで与えます。

__例.__ 連立方程式  𝑥+5𝑦=2,−3𝑥+6𝑦=15 の解
```py
solve([x+5*y-2, -3*x+6*y-15], [x,y])
```
## 初等解析

### 極限

極限は、`limit()`を用いて求めることができます。

__例.__ $\lim_{x \to 0} x^x$

```py
limit(x**x, x, 0)
```
無限大は、`oo`と書きます。

__例.__ $\lim_{x \to \infty} \frac{1}{x}$
```py
limit(1/x, x, oo)
```
### 微分

微分は、`diff()`を用います。

__例. $\frac{x}{dx}\sin{x}$__
```py
diff(sin(x), x)
```
### 積分

積分は、`integrate(関数, 変数)`によって、初等関数, 特殊関数の積分が可能です。
 
__例__ $\int \log x ~dx$
```py
integrate(log(x), x)
```
__例__ $\int_{-\infty}^\infty  e^{-x^2} dx$
```py
integrate(exp(-x**2), (x, -oo, oo))
```
## コースワーク

Pythonの習得で重要なのは、習ったことを覚えてプログラミングすることではありません。
「こういうことはできるかな？」と調べて、ソースコードを参考にプログラミングすることです。
ぜひ、解いてみましょう。
<div class="admonition tip">

**演習（数式）**

1.   $\int_{-\infty}^\infty \sin{x^2} dx$ を求めよ
2.   $\int_{0}^\infty  (\sqrt{x^2+1}-1)^2 dx$ を求めよ
3.   $f(x)=\frac{4x^2+2x+1}{x^2+1}$の極値を求めよ
4.   大学入試の過去問からSymPyで解ける問題を探して解いてみよう

</div>

__ヒント__

色々な解き方があります。

1. SymPyを使っても解いてみましょう。
2. どうしても解けなければ、手で解いても構いません


