# 考える計算機

命題論理の復習をかねて考える計算機を考えてみましょう。


## 命題と論理

スモール言語の例として、命題論理をみながら、
コンピュータを用いて、証明問題を解く方法を考えてみましょう。

### 命題と推論

**命題(proposition)**は，**正しいか、それとも正しくないか**を判定できる文です。

次の２つの文は，正しいかどうか判定できるため，命題となります。

- 雨が降っている
- もし雨が降っているなら、空には雲がある

この２つの命題が正しいと仮定するならば，
私たちは推論し，「空には雲がある」という結論が正しいと考えます。

- **(前提1)**: もし雨が降っているなら、空には雲がある
- **(前提2)**: 雨が降っている
- **(結論)**: 空には雲がある

### 命題変数

命題論理学では、自然言語で記述された命題を**命題変数(variable)**に置き換えることで、推論の仕組みを形式的に考えます。

-　「雨が降っている」を$P$を，「空に雲がある」を$Q$とします。
-　「もし$P$ならば$Q$である」という関係は，**含意(implication, ($\to$)**という演算子で書きます。

すると，先ほどの自然言語の命題と推論は，次のように書き換えることができます。

- **(前提1)**: $P\to Q$
- **(前提2)**: $P$
- **(結論)**: $Q$

このように変数におきかえると、命題と推論の背後にあるパターンに注目し、コンピュータなどで形式的に処理しやすくなります。

\begin{lbox}{モダスポネンス}
実は，どのような命題$P$, $Q$であっても成り立つ，
\EN{モダスポネンス}{modus ponens}という推論規則を適用し，結論を導いていたことになります。
\end{lbox}

\subsection{ルールの記法}

{\CS}や形式論理学では、推論規則のことをルールとも呼びます。
非常によく登場するので、記法が決まっています。

\begin{multicols}{2}

\[
\mbox{前提} ... \vdash \mbox{結論}
\]

\columnbreak

\infrule
{\mbox{前提 } ...}
{\mbox{結論}}

\end{multicols}

先ほどのモダス・ポネンスも、ルールの記法を用いると次のように書き直すことができます。

\begin{multicols}{2}

\[
P\to Q,P\vdash Q
\]

\columnbreak

\infrule[Modus Ponens]
{P \to Q  \andalso P}
{Q}

\end{multicols}

{\CS}の論文では、何の断りもなく用いられるので覚えておきましょう。

### 命題論理

論理式 $\phi$
$\phi$


### 命題計算

命題と推論を計算処理できるプログラムをPython で作りましょう。

さて、命題論理を計算として処理できるインタプリタを作っていきましょう。

\subsection{構文論}

まず、命題論理の論理式$\Xp$の構文を定義しておきましょう。

\begin{lbox}{論理式$\Xp$の構文}
論理式$\Xp$は、命題変数、真理値($\TT$, $\FF$)、論理記号を用いて帰納的に構成される

\begin{center}
\begin{tabular}{lcllr}
　$\Xp$ & ::= & $\TT$ & \\
& $|$ & $\FF$  & \\
& $|$ & $\lnot \Xp$ &  $\Xp$でない  & $Not(\Xp)$ \\
& $|$ & $\Xp \land \Xp$ & $\Xp$かつ$\Xp'$  & $And(\Xp,\Xp')$ \\
& $|$ & $\Xp \lor \Xp$  &  $\Xp$または$\Xp'$  & $Or(\Xp,\Xp')$ \\
& $|$ & $\Xp \Then \Xp$ &  $\Xp$ならば$\Xp'$  &  $Then(\Xp,\Xp')$ \\
%& $|$ & $\Xp \ThenEq \Xp$ &  $\Xp$と$\Xp'$は同値  &  $Eq(\Xp,\Xp')$ \\
\end{tabular}
\end{center}

\end{lbox}

なお、論理演算子の結合順序は以下の通りとします。
\begin{tabular}{ccc}
 $\lnot P \land Q$ & $\ThenEq$ & $(\lnot P) \land Q$  \\
 $P \Then P \land Q$ & $\ThenEq$ & $P \Then (P \land Q)$  \\
 $P \Then P \Then Q$ & $\ThenEq$ & $P \Then (P \Then Q)$  \\
\end{tabular}


\begin{cbox}{Let's try!!}

論理式$\Xp$の構文を{\TPEGG}で定義してみよう。

\end{cbox}

\subsection{意味論}

論理演算子の意味論は、真理値表で与えられます。

\begin{multicols}{2}

\begin{center}
\begin{tabular}{c|c}
$P$ & $\lnot P$ \\ \hline
T & F \\
F & T \\
\end{tabular}
\end{center}

\columnbreak

\begin{tabular}{cc|ccc}
$P$ & $Q$ & $P \land Q$ & $P \lor Q$ & $P \Then Q$  \\ \hline
T & T &         T & T & T  \\
T & F &         F & T & F  \\
F & T &         F & T & T  \\
F & F &         F & F & T  \\
\end{tabular}
\end{multicols}

\begin{cbox}{Let's try!!}

論理式$\Xp$を解釈するインタプリタを作ってみよう。

\end{cbox}

\if0
\subsection{命題論理の法則}

命題論理は次の法則が成り立つ

\begin{tabular}{ccr}
　$P \land P \Then P $ &　$P \lor P \Then P$ & (べき等律) \\
　$P \land \lnot P \Then \FF $ &　 & (矛盾律) \\
           &　$P \lor\lnot P \Then \TT $ & (排中律) \\
　$P \land Q \ThenEq Q \land P $ &　$P \land Q \ThenEq Q \land P $ & (交換則) \\
　$P \land (Q \lor R) \ThenEq (P \land Q) \lor R $ &　$P \lor (Q \land R) \ThenEq (P \lor Q) \land R $ & (結合則) \\
　$P \land (Q \lor R) \ThenEq (P \land Q) \lor (P \land R) $ &　$P \lor (Q \land R) \ThenEq (P \lor Q) \land (P \lor R) $ & (分配則) \\
  & & \\
 $P \Then P \ThenEq \TT$ & & \\
 $P \Then Q \ThenEq \lnot P \lor Q$  & & (含意律)　\\
 $P \Then Q \ThenEq \lnot Q \Then \lnot P$  & & (待遇律)　\\
\end{tabular}
\fi

\section{モデル意味論}

命題計算では、(簡単な)証明もコンピュータによる計算によって示せるようになります。

次の定理を考えてみましょう。

\begin{cbox}{例}
$P \Then Q$は、$\lnot P \lor Q$ と等価である
\end{cbox}

\EN{モデル意味論}{model @@}とは、
論理式の全ての命題変数に$\{\TT/\FF\}$の解釈(意味)を与え、
全ての組み合わせにおいて真になることで証明する方法です。

これを示すためには、命題変数 $P,Q$ に$\{\TT/\FF\}$の組み合わせを調べます。

\begin{center}
\begin{tabular}{cccc}
P & Q & $(P \Then Q) ~~ \Then ~~ \lnot P \lor Q$ &  $ \lnot P  \lor Q ~~ \Then ~~ (P \Then Q)$ \\ \hline
T & T &         T & T  \\
T & F &         T & T  \\
F & T &         T & T  \\
F & F &         T & T  \\
\end{tabular}
\end{center}

以上により、$P \Then Q$は、$\lnot P \lor Q$ と等価といえます。

\subsection{恒真式と充足可能★}

論理式は、命題変数の値によっては真になったり、偽になります。

\begin{itemize}
\item \EN{恒真式}{トートロジー, tautology} - 命題変数がどのような真理値をとっても常に真となる
\begin{itemize}
\item 例. $P \Then P$  $P$ が真であっても偽であっても真
\end{itemize}
\item \EN{充足可能}{satisfiable} - 命題変数の真理値の取り方によっては真になる
\begin{itemize}
\item 例. $P \land Q$  $P$ と $Q$が共に真のとき真だから充足可能
\end{itemize}
\item \EN{充足不可能}{unsatisfiable} - 命題変数がどのような真理値をとっても常に偽となる
\begin{itemize}
\item 例. $P \land \lnot P$  $P$ が真であっても偽であっても偽
\end{itemize}
\end{itemize}

\begin{lbox}{トートロジーの記法: $\models$}

\begin{multicols}{2}
$P$ はトートロジー
\[
\models P
\]

\columnbreak

$P\Then Q$ はトートロジー
\[
P \models Q
\]
\end{multicols}

\end{lbox}

命題論理は、形式論理学やコンピュータ上の論理学の基礎となります。
{\This}では軽く触れただけなので、興味のあるみなさんは、是非、参考図書を参考に勉強してみましょう。

\section{コンピュータによる証明（おまけ）}

みなさんは、大学に入る前から証明問題を解いてきました。

\textbf{定理}{theorem}は、証明された真なる命題のことです。
ちなみに，まだ証明されていないものを\EN{仮説}{hypothesis}と呼びます。

%文脈によっては公理も定理に含む。また、数学においては論説における役割等から、補題（ほだい、英: lemma）あるいは補助定理（ほじょていり、英: helping theorem）、系（けい、英: corollary）、命題（めいだい、英: proposition）などとも呼ばれることがある。ここでの「命題」と冒頭文に言う命題とは意味が異なることに注意。

一般的に，定理は、まずいくつかの前提条件を列挙($A_1, A_2, ..., A_i)$し、次にその下で成り立つ結論($B$)を述べるという形をしています。

\[
A_1, A_2, ..., A_i, ... \to B
\]

有名な\EN{ピタゴラスの定理}{Pythagorean theorem}は，次のとおり，前提条件と結論に分けて述べることができます。

\begin{quote}
\begin{description}
\item [前提]: 直角三角形の斜辺の長さを $c$、他の2辺の長さを $a$, $b$ とする
\item [結論]: $c^2 = a^2 + b^2$
\end{description}
\end{quote}

ここでは，簡単のため，ひとつの前提条件($A$)から結論$B$が成り立つという形式の定理を考えます。

\[
Theorem: A \to B
\]

証明とは何をするのかといえば，先ほどの推論規則の記法をつかえば，
$A \to B$を結論として導く\fbox{?}を埋めることになります。

\infrule
{\fbox{?}}
{A \to B}

もちろん，\fbox{?}を埋めるのは，そんなに簡単ではありません。
推論規則を何ステップも重ねて，正しさを検証しながら証明を作ってゆくわけです。

%\begin{prooftree}
%\AxiomC{$[A]$}
%\AxiomC{$C$}
%\AxiomC{$\cdots$}
%\BinaryInfC{$B$}
%\RightLabel{$\to I$}
%\BinaryInfC{$A \to B$}
%%%\UnaryInfC{$A \to B$}
%\end{prooftree}

G. Frege (1848-1925) は,1879 年『概念記法』を発表し,現代論理学の基礎となる体系を立ち上げました。
第一階述語論理などです。
このとき,「証明」についても数学的に研究しようと,発想の転換が行われました。

現代論理学は，このような証明を構成する推論規則はパターンが存在し，
しかもパターンは高々有限個のパターンしかないことを明らかにしています。

\newpage

\section*{練習問題}

命題論理ソルバーを作ってみよう。

A -> True
