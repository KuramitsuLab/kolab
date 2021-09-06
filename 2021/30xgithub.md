# GitHub ソーシャルコーディング

まずは、
Github によるソーシャルコーディングを理解しましょう。

https://breezegroup.co.jp/202102/vscode-github-windows/
https://qiita.com/shiro01/items/e886aa1e4beb404f9038

## Git と Github

ソフトウェアは、複数の開発者がソースコードを編集するので、
「**いつ誰がどこを編集したのか？** 」などを管理する必要があります。

<div class="admonition note">

（用語）レポジトリ

バージョン管理ツールによるソースコードの保管場所

</div>

### Git

Gitは、**ソースコードのバージョンを管理するツールのひとつ** です。
開発者ごとにレポジトリを持ち、変更を分散管理しやすい点が特徴です。

\begin{center}
\includegraphics[width=0.40\paperwidth]{./fig/gitcmd}
\end{center}

### GitHub

GitHubは、**Gitを利用した開発者を支援するWebサービス** のことです。

* クラウド上でリモートレポジトリを開設し、簡単に共有できる
* Gitにはない、開発者に便利な機能を追加している
* 例. Pull Request: ソースコードの変更点について他のメンバーにレビュー依頼ができる機能

Githubを使うメリットには次のようなものがあります。

__グループ開発__

* 定番
* 複数バージョン（ブランチ）をシェアできる
* 複数の開発者による開発成果をマージできる
* プロジェクト管理のサポートがある

__個人開発__

* いつでも昔の状態に戻すことができる
* 複数のバージョンの管理
* 開発ソフトウェアを公開しやすい

<div class="admonition note">

広がるGithub

現在は、ソースコード以外にも、デザインデータや文書などのバージョン管理にも活用されています。
例. ホワイトハウスや国土地理院など、行政機関の文書管理など

</div>

## Github の簡単な使い方


## Github による開発

__既にあるプロジェクトに参加する場合__

1. **リポジトリ**を作成する
2. ソースコードの作成、編集を行う
3. 新規作成、変更、削除をGitのステージに追加する
4. ステージに追加された内容をローカルリポジトリに**コミットする**
5. ローカルリポジトリの内容を**リモートリポジトリ**にプッシュする
6. もしくは**レポジトリ**をフォークする

\subsection{レポジトリを作る}

\HBold{1.} Github の個人ページを開いて、\textbf{New Repository}する

\begin{center}
\HUnder{授業用レポジトリ名} {\Large \tt chibi}
\end{center}

レポジトリ名は、自由につけることができるが、授業中は統一した名前を用いる。
（練習で chibi という名前のスモール言語を作る。）

\begin{center}
\includegraphics[width=0.60\paperwidth]{./fig/newrepo}\\
\url{https://github.com/kkuramitsu}\\
\HUnder{注意} kkuramitsu の部分は、自分のアカウント名を用いる
\end{center}

%\begin{cbox}{konohaとは}
%倉光が、昔開発していたプログラミング言語の名前
%\begin{center}
%\includegraphics[width=0.40\paperwidth]{./fig/tykonoha}\\
%(TinyKonoha)
%\end{center}
%\end{cbox}

\HBold{2. (git clone)} Github上のリモートレポジトリから\textbf{ローカルレポジトリ}のクローンを作る

\begin{quote}
\begin{Py}

$ git clone https://github.com/kkuramitsu/mykonoha.git
Cloning into 'mykonoha'...
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.

$ cd mykonoha
$ ls
LICENSE		README.md
\end{Py}

無事にクローンされると、
\texttt{mykonoha} というフォルダ（ディレクトリ）が生成される。
\textbf{このフォルダがローカルレポジトリとなる。}\\

\end{quote}

\HBold{3. (git status)} レポジトリの状態を確認する

\begin{quote}
現在のリポジトリの状態を確認するコマンドは次のとおり

\begin{Py}

$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
\end{Py}

Git は、頻繁にうまくいかなくなる。
このコマンドで状態を確認する癖をつけるとよい。
\end{quote}

\vspace{1cm}
\begin{cbox}{Git は複雑}
Git は、使いやすくする方法が研究論文になるなど、少々複雑。\\
変な風になったら、ローカルレポジトリをclone して作り直す。

\end{cbox}

\subsection{ソースコードを編集する}

\newcommand{\VSC}[0]{{Visutal Studio Code}}

\begin{center}
\includegraphics[width=0.75\paperwidth]{./fig/vsc}\\
（統合開発環境: \VSC)
\end{center}

\HBold{4.} {\VSC} で mykonoha フォルダを開き、フォルダ内にhello.py ファイルを作成する
\begin{quote}
\begin{lbox}{hello.py の内容}

\begin{Py}
print('hello world')

\end{Py}
\end{lbox}

\HUnder{注意}: \VSC に慣れるために、実行してみるとよい。\\
\end{quote}

\HBold{5. (git add)} {\VSC}で編集＆保存し、ステージ環境にあげる

\begin{quote}

\begin{Py}
$ git add hello.py 

$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   hello.py

\end{Py}

\begin{cbox}{ステージ環境とは}
\begin{itemize}
\item 「ローカルリポジトリに上げる準備が整ったファイルの集合」である
\item ステージ環境にあるファイルをコミットすると、ローカルリポジトリにあがる
\end{itemize}
\end{cbox}
\end{quote}

\HBold{6. (git commit)} \textbf{ログ用コメント}を付けてローカルレポジトリにコミットする

\begin{quote}
\begin{Py}

$ git commit -m 'new hello.py' 

[master b3dfabb] new hello.py
 1 file changed, 2 insertions(+)
 create mode 100644 hello.py

$ git log
commit b3dfabbdb44ee1f732616dd445481502202f0c88 (HEAD -> master)
Author: Kimio Kuramitsu 
Date:   Tue Sep 17 15:03:04 2019 +0900

    new hello.py

commit 244ef1417d989d31143f131a6e1201b283b1d029 (origin/master, origin/HEAD)
Author: Kimio Kuramitsu 
Date:   Mon Sep 16 02:47:09 2019 +0900

    Initial commit

\end{Py}

\end{quote}

\begin{cbox}{\Large Git による開発}
{\Large ４〜６を繰り返し。\\（動作確認など作業の一区切りで）コミットする}
\end{cbox}

\HBold{4〜6を繰り返す}　 {\VSC} 再度、hello.py ファイルを編集してみる

\begin{quote}
\begin{lbox}{hello.py の内容}

\begin{Py}
for n in range(10):
	print('hello world')

\end{Py}

\end{lbox}

ここで、編集を保存して \textbf{git diff} を用いると、\textbf{前回コミットからの更新箇所}が確認できる。

\begin{Py}

$ git diff
diff --git a/hello.py b/hello.py
index a169752..c4acb0b 100644
--- a/hello.py
+++ b/hello.py
@@ -1,2 +1,3 @@
-print('hello, world')
+for n in range(10):
+       print('hello, world')
\end{Py}

\vspace{1cm}
\begin{cbox}{練習}
編集した hello.py を再度コミットしてみよう。
\end{cbox}
 
 正しく、コミットできると、\textbf{git log} で次のようになるはず
 
\begin{Py}

$ $ git log
commit 937e98c40680101f92c75503a0c386364e6f9831 (HEAD -> master)
Author: Kimio Kuramitsu <kkuramitsu@gmail.com>
Date:   Tue Sep 17 15:10:46 2019 +0900

    10times

commit b3dfabbdb44ee1f732616dd445481502202f0c88
Author: Kimio Kuramitsu <kkuramitsu@gmail.com>
Date:   Tue Sep 17 15:03:04 2019 +0900

    new hello.py

commit 244ef1417d989d31143f131a6e1201b283b1d029 (origin/master, origin/HEAD)
Author: Kimio Kuramitsu <kkuramitsu@gmail.com>
Date:   Mon Sep 16 02:47:09 2019 +0900

    Initial commit
\end{Py}
\end{quote}

\begin{cbox}{変なコメントを残すと}
ログをみたとき、作業内容がわからなくなる。
\end{cbox}
 
 \newpage
\subsection{ローカルとリモートの同期}

\begin{flushright}
\includegraphics[width=0.20\paperwidth]{./fig/gitcmd}
\end{flushright}

\vspace{-3cm}
\HBold{7. (git push)} ローカルレポジトリからリモートレポジトリに同期する

\begin{quote}

\begin{Py}

$ git push
Username for 'https://github.com': kkuramitsu
Password for 'https://kkuramitsu@github.com': 
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 540 bytes | 135.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
To https://github.com/kkuramitsu/mykonoha.git
   244ef14..937e98c  master -> master

\end{Py}

\vspace{1cm}
\begin{cbox}{アカウント名とパスワード}
毎回、パスワードを入力したくないときは、\Google{SSH公開鍵}を登録しておくとよい
\end{cbox}
\end{quote}

\HBold{8. (git pull)} リモートレポジトリからローカルレポジトリに同期する

\begin{quote}

\begin{Py}

$ git pull
Already up to date.
\end{Py}

リモートレポジトリを複数人で開発していると、
ローカルレポジトリの内容とコンフリクト（衝突）することがある。
その場合は、コンフリクトした\textbf{ファイルを編集して、手作業で解決する}。
\end{quote}

\begin{cbox}{Github とグループ開発}
Github は本来グループ開発で威力を発揮するが、本講義では\Google{ pull request }などは扱わない。
\end{cbox}

\vspace{1cm}
\subsection{家でGithubを使うためには？}

\begin{center}
\includegraphics[width=0.40\paperwidth]{./fig/githome}
\end{center}

\begin{multicols}{2}
\emph{Macの場合}
\begin{itemize}
\item \texttt{xcode --select} で gcc を入れる
\item \Google{brew, brew cask} を入れる
\item \texttt{brew install python3}
\item \texttt{brew cask install visual-studio-code}
\end{itemize}

\columnbreak
\emph{Windows の場合}
\begin{itemize}
\item \Google{Python3} を入れる
\item \Google{Git for Windows } を入れる
\item \Google{Visual Studio Code }を入れる
\end{itemize}
 
\end{multicols}

\HBold{注意}四角枠「 \Google{ キーワード } はGoogle でキーワードを調べてね（あとは頑張ってね）」という意味


