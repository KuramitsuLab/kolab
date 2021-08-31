import tokibi
import verb

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

# @get  値 -> 値を求める
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_get(code, docs, results, options):
    for doc in docs:
        tokibi.randomize()
        results.append((code, doc+'を'+tokibi.alt('求める|習得する|得る')))

# @calc  値 -> 値を算出する
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_calc(code, docs, results, options):
    for doc in docs:
        tokibi.randomize()
        results.append((code, doc+'を'+tokibi.alt('求める|算出する|得る')))

# @check  値 -> 値を算出する
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_check(code, docs, results, options):
    for doc in docs:
        vpos, base, prefix = verb.detect_last_vpos(doc)
        if vpos == 'NA':
            tokibi.randomize()
            results.append((code, doc+'を'+tokibi.alt('表示する|確認する|調べる|見る')))
    return True

# @let

def emit_let(code, docs, results, options):
    name = 'newname' if len(options) == 0 else options[0]        
    for doc in docs:
        vpos, base, prefix = verb.detect_last_vpos(doc)
        random_factor = tokibi.randomize()
        suffix = name + tokibi.alt('とする@4|にする@2|に代入する')
        if vpos.startswith('V'): #動詞
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、' + suffix
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、' + suffix
        else:
            suffix = base+f'を'+suffix
        results.append((f'{name} = {code}', prefix+suffix))

def emit_let_self(code, docs, results, options):
    emit_let(code, docs, results, options)
    name = code.split('.')[0]
    for doc in docs:
        vpos, base, prefix = verb.detect_last_vpos(doc)
        if vpos.startswith('V'): #動詞
            random_factor = tokibi.randomize()
            suffix = tokibi.alt('置き換える|再代入する')
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、' + suffix
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、' + suffix
            results.append((f'{name} = {code}', prefix+suffix))

def emit_inplace(code, docs, results, options):
    name = 'newname'
    for doc in docs:
        vpos, base, prefix = verb.detect_last_vpos(doc)
        random_factor = tokibi.randomize()
        suffix = tokibi.alt('インプレースする|置き換える')
        if vpos.startswith('V'): #動詞
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、' + suffix
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、' + suffix
            code2 = code[:-1] + ', inplace=True)'
            results.append((code2, prefix+suffix))

def emit_dot(code, docs, results, options):
    for doc in docs:
        vpos, base, prefix = verb.detect_last_vpos(doc)
        random_factor = tokibi.randomize()
        if vpos.startswith('V'): #動詞
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、'
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、'
        else:
            suffix = base+f'の'
        results.append((f'{code}.', prefix+suffix))

def emit_it(code, docs, results, options):
    loc = code.find('.')
    if loc == -1:
        return
    code = code[loc:]
    it = 'それを' if len(options) == 0 else options[0]
    suffix = it[-1]
    d = set() # 同じdoc を繰り返し出力しないようにする
    for doc in docs:
        loc = doc.find(suffix)
        if loc > 0:
            doc = it + doc[loc+1:]
            if doc not in d:
                results.append((f'{code}', doc))
                d.add(doc)

def emit_FIXME(code, docs, results, options):
    pass