\documentclass[uplatex]{jsarticle}

\usepackage{amsmath}
\usepackage{latexsym}
\usepackage{url}

\usepackage{amssymb}
\setcounter{tocdepth}{3}
\usepackage[dvipdfmx]{graphicx}

\usepackage{amsmath}
%\usepackage{bcprules}
\usepackage{comment}
\usepackage{multicol}
\usepackage{ascmac}
\usepackage{amsthm}
\usepackage{ulem}

\usepackage{listings}

\newtheoremstyle{problemstyle}  % <name>
{3pt}                                               % <space above>
{3pt}                                               % <space below>
{\normalfont}                               % <body font>
{}                                                  % <indent amount}
{\bfseries\itshape}                 % <theorem head font>
{\normalfont\bfseries:}         % <punctuation after theorem head>
{.5em}                          % <space after theorem head>
{}          % <theorem head spec (can be left empty, meaning `normal')>
\theoremstyle{problemstyle}

\newtheorem{problem}{問題}[section] % Comment out [section] to remove section number dependence

\newenvironment{hint}{\begin{quote}}{\end{quote}}
%\newenvironment{hint}{\begin{comment}}{\end{comment}}

\newenvironment{answer}{\begin{quote}}{\end{quote}}

\lstset{%
language={C},
%backgroundcolor={\color[gray]{.85}},%
basicstyle={\small},%
identifierstyle={\small},%
commentstyle={\small\itshape},%
keywordstyle={\small\bfseries},%
ndkeywordstyle={\small},%
stringstyle={\small\ttfamily},
frame={tb},
breaklines=true,
columns=[l]{fullflexible},%
numbers=left,%
xrightmargin=0zw,%
xleftmargin=3zw,%
numberstyle={\scriptsize},%
stepnumber=1,
numbersep=1zw,%
lineskip=-0.5ex%
}

\usepackage{color}
\definecolor{darkblue}{rgb}{0.0,0,0.5} % R(赤),G(緑),B(青)
\definecolor{byzantium}{rgb}{0.44, 0.16, 0.39}
\newcommand{\Name}[1]{{\small \texttt{\color{darkblue} #1}}}
%\newcommand{\nt}[1]{{\tt {\small {\color{byzantium} #1}}}}
\newcommand{\nt}[1]{{\tt #1}}

\newcommand{\TODO}[1]{{\color{blue} [TODO: #1]}}
\newcommand{\FIXME}[1]{{\color{red} {\bf FIXME}: #1}}


\newcommand{\User}{ユーザ}
\newcommand{\Review}{レビュー}
\newcommand{\Suffix}{サフィックス}
\newcommand{\True}{true}
\newcommand{\False}{false}

\title{C演習問題}
\author{倉光君郎}

\begin{document}

%\maketitle


\end{document}

