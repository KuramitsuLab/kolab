# 実用的なプログラミングへ

３年後期では、Python を用いて、より実用的なプログラミング技法を学んでいきます。

## システム・プログラミング

システム・プログラミングとは、オペレーティング・システムが提供する機能を活用するプログラミングです。本講義では、**UNIX系オペレーティング・システム** を前提に説明を進めます。

<div class="alert alert-info">

UNIX オペレーティングシステム

世の中で使われているコンピュータは、
スーパーコンピュータ、クラウド(Linux)からMac, スマートフォン(Andoroid, iPhone OS)まで、ほぼUNIX系OSが使われています。Windows だけが、身近にある唯一のUNIXでないOSと言えます。
</div>

オペレーティング・システムの授業で習ったと思いますが、簡単に用語をまとめておきます。

* __カーネル__: オペレーティングシステムの中核となるプログラム。
CPU、メモリ、ストレージなどのハードウェアをユーザプログラム（アプリのこと）にリソースとして提供する。
* __システム・コール__: カーネルに対し、リソースなどを要求する関数（ライブラリ）
* __コマンド__: システムコールをプログラムしなくても、システムを操作できるように開発されたテキストベースのアプリ
* __シェル__: コマンドを実行する(対話的な）環境

### ターミナル(端末)

ターミナル（端末）からUNIXシステムにログインすると、**シェル** が起動されて、新しいセッションができます。シェルを用いることで、手元のローカルなマシンも、リモートのサーバも、同じように操作するができます。

macOSは、UNIXなので、macOSでシェルを操作する様子をデモします。

__MacOS上のUNIXコマンド__

```
uname -a
Darwin MacBook.local 19.6.0 Darwin Kernel Version 19.6.0: Tue Jun 22 19:49:55 PDT 2021; root:xnu-6153.141.35~1/RELEASE_X86_64 x86_64
```

### クラウド: Colabの場合

Google Colaboratory は、Google 社のクラウドのUNIXでサービスを提供しています。ターミナルの代わりに、Webブラウザから操作できるように jupyter notebook (Google版)から、コマンド操作することはできます。

ターミナルとは、操作性は異なりますが、基本的にコマンド操作ができます。

__ColabのUNIXコマンド__

```
!uname -a
```

<div class="admonition warning">

Colab(Jupyter)上のUNIXコマンド

Python コードと区別するため、`!`マークをつけます。
シェルのセッションが一回ごとに切られるため、
`! cd`のようなコマンドは、うまく機能しません。
`cd`は、代わりに`%cd`を使います。 

</div>

### UNIXコマンド

UNIXコマンドの操作は、コンピュータ・エンジニアの基礎です。
自由自在に操作できないと、システム管理者としても、
データサイエンティストとしても困ります。
**最低限覚えておきたいUNIXコマンド** をまとめておきます。

| TH 左寄せ | TH 中央寄せ | TH 右寄せ |
| :--- | :---: | ---: |
| TD | TD | TD |
| TD | TD | TD |


#### ディレクトリ操作


| コマンド　　        | 操作　　　　　　　|
|-------------------|-------------------|
| pwd                 | 現在のディレクトリを表示 |
| cd                  | ホームディレクトリへ移動 |
| cd (dir名)          | 指定ディレクトリへ移動 |
| mkdir (dir名)       | 新規ディレクトリを作成 |
| rmdir (dir名)       | 空のディレクトリを削除 |
| rm -r (dir名)       | 指定ディレクトリを中のファイルごと削除 |
| cp -r (dirA) (dirB) | ディレクトリAをディレクトリBにコピー |
| mv (file名) (dir名) | ファイルをディレクトリへ移動 |
| ls (dir名)          | ファイル一覧表示 |




## ファイル操作

Python は、システムコールをPython風に使いやすいように、
モジュール化して提供しています。

### ファイルを読む

Python をファイルを読み込むときは、
`open(filename)`を用いて、ファイル（ストリーム）をオープンします。
（この奇妙な`open`という関数名は、システムコールに由来しています。）
ファイルを一旦、オープンしたら、
あとは f.readlines()で1行ずつ読んで、イテレータで処理します。

```py
def readfile(filename):
    f = open(filename)
    for line in f.readlines():
        print(line)
    f.close()

readfile('dog.txt')
```

> 空行が入るのは自分で直してみてください。

<div class="admonition warning">

`f.close()`は重要

`open(filename)`は、システムコールを呼び出して、ファイルリソースを要求しています。
ファイルリソースは有限です。（あまりにファイルを開きすぎると、開けなくなります。）
使い終わったら、`f.close()`を呼び出して、リソースを解放しておきます。

</div>

人間は、どうしても`f.close()`を忘れがちです。
Python では、プログラム言語の構文として、with 文を導入して、
with文のブロックを抜ける時に、自動的に`close()`されるようになっています。

```py
def readfile(filename):
    with open(filename) as f:
        for line in f.readlines():  #インデントする
            line = line.strip() # 行末の改行を取り除く
            print(line)

readfile('dog.txt')
```

### エラー処理（例外処理）

システム・プログラミングでは、プログラムを開発した時点では回避できないエラーが発生します。

例えは：

* 指定したファイル名が存在しない
* ファイルを読んでいる途中に、デバイスが破壊した

オペレーティング・システムは、このようなエラーをできる限り（全てではない）検出し、
プログラム側に通知してくれます。Pythonは、例外(Exception)として、送出します。

try/except文は、このような例外を補足し、プログラムの処理を続ける文法です。

まず、存在しないファイル名を指定してみて、例外を送出してみましょう。

```py
def readfile(filename):
    with open(filename) as f:
        for line in f.readlines():  #インデントする
            line = line.strip() # 行末の改行を取り除く
            print(line)

readfile('inu.txt')
```

例外処理は、例外を補足したいところを`try`ブロックで囲みます。

```py
def readfile(filename):
    try:
        with open(filename) as f:
            for line in f.readlines():  #インデントする
                line = line.strip() # 行末の改行を取り除く
                print(line)
    except FileNotFoundException :
        pass # 何もしない
readfile('inu.txt')
```

例外処理では、エラーが起きても何もなかったように処理を続けることができます。
このようなエラー処理は、「エラーを塗りつぶしてしまう」と言いますが、
結局、エラーの発生が気づかなくなり、**より深刻なシステム障害の原因** になります。

最低限、次のようにエラーの発生した記録だけはログに残す習慣をつけましょう。

```py
import logging

def readfile(filename):
    try:
        with open(filename) as f:
            for line in f.readlines():  #インデントする
                line = line.strip() # 行末の改行を取り除く
                print(line)
    except FileNotFoundException :
        logging.error('ファイルが見つかりません', filename)
readfile('inu.txt')
```

### ファイルに書き込む

ファイルの読み込みに続いて、ファイルの書き込みの方法も見ておきましょう。

ファイルの書き込みは、`open(filename, 'w')`のように、
書き込みモード(w)でファイルを開きます。
そして、print文の出力先を`file=f`のように開いたファイルに変更します。

```py
import logging

def writefile(filename, lines):
    try:
        with open(filename, 'w') as f:
            for line in lines:
                print(line, file=f)
    except FileNotFoundException :
        logging.error('ファイルが見つかりません', filename)

writefile('abc.txt', ['a', 'b', 'c'])
```

### コマンド

次は、cpコマンドのように、ファイルコピーをするコマンドを作ってみましょう。

```
!cp abc.txt abc_copied.txt
```

ここでは、Python のスクリプト名を `cp.py`として保存することにします。
すると、Pythonコマンドから、次のようにファイル名を引数で渡し、
呼び出せるようにしていきます。

```
!python3 cp.py abc.txt abc_copied.txt
```

コマンド引数で渡されたファイル名を受け取るのは、sysモジュールを用います。

```py
import sys

print(sys.argv)  # コマンド引数がリストでなっている
```

> `sys.argv[0]`には、スクリプト名が入っています。

Python でコマンドを作るときは、
プログラムをスクリプトファイルとして保存します。

```
%%file argv.py

import sys

def main(argv):
    print(argv)

if __name__ == '__main__':  # Python がコマンドとして呼ばれたときのみ実行
    main(sys.argv[1:])    
```

すると、Python コマンドから実行できます。

```
!python3 argv.py abc.txt abc_copied.txt
```

<div class="alert alert-info">

Let's try:

`cp.py`を完成させて、第一引数で渡されたファイルを第２引数で
指定されたファイルにコピーされるようにしよう。

</div>





## コースワーク

### `cat`コマンド

cat は、ファイルの内容を続けて、標準出力(stdout)に出力するコマンドです。

<div class="admonition tip">

**課題(catコマンド)**

Pythonで、`cat`コマンドをシミュレーションした `cat.py` を作ってみましょう。

__catコマンド__
```
!cat neko.txt neko.txt
```

__Python版 cat コマンド__
```
!python3 cat.py neko.txt neko.txt
```

</div>


### `wc`コマンド

wc は、wordカウントのコマンドです。

<div class="admonition tip">

**課題(catコマンド)**

Pythonで、`cat`コマンドをシミュレーションした `cat.py` を作ってみましょう。

__catコマンド__
```
!cat neko.txt neko.txt
```

__Python版 cat コマンド__
```
!python3 cat.py neko.txt neko.txt
```

</div>


<div class="alert alert-info">

Let's try:

UNIXには、シェバング(shebang)と呼ばれる機能があり、
`python3`を省略してコマンドとして呼び出せます。
調べて、試してみましょう。

</div>
