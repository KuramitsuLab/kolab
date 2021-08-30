import tokibi

# @not 否定形を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に作る (docsは複数だが最低ひとつ)
# results.append(('a % 2 != 0', 'aが偶数でないかどうか'))

def emit_not(code, docs, results, options):
    pass


# @if if文を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する (バリエーションを作ってもいい)
# results.append(('if a % 2 == 0:', 'もしaが偶数ならば'))
# results.append(('if a % 2 == 0:', 'もしaが偶数のとき'))

def emit_if(code, docs, results, options):
    pass

# @while 文を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する (バリエーションを作ってもいい)
# results.append(('if a % 2 == 0:', 'もしaが偶数の間'))

def emit_andor(code, docs, results, options):
    pass

# @andor
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する
# results.append(('a % 2 == 0 and', 'aが偶数、かつ、'))
# results.append(('a % 2 == 0 or', 'aが偶数、または、'))

def emit_andor(code, docs, results, options):
    pass

# @it  して〜、それを
# 例
# print() 表示する 
# pi 円周率
# 変換した結果は、results に追加する
# results.append(('print()', '表示して、それを'))
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_it(code, docs, results, options):
    pass

# @result  する -> した結果にする
# 例
# print() 表示する 
# pi 円周率
# 変換した結果は、results に追加する
# results.append(('print()', '表示した結果'))
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_result(code, docs, results, options):
    pass

