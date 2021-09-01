import random
import tokibi
import verb

def detect_vpos(s):
    return verb.detect_last_vpos(s)

def alt(s):
    tokibi.randomize()
    return tokibi.alt(s)

def check_modified_code(code, doc):
    if '#' in doc:
        return doc.split('#')
    return code, doc

def remove_whether(doc):
    if doc.endswith('かどうか') or doc.endswith('か否か'):
        return doc[:-4]
    if doc.endswith('か'):
        return doc[:-1]
    return doc

def transform_not(code):
    if '==' in code:
        return code.replace('==', '!=')
    if '!=' in code:
        return code.replace('!=', '==')
    return f'not {code}'

# @not 否定形を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に作る (docsは複数だが最低ひとつ)
# results.append(('a % 2 != 0', 'aが偶数でないかどうか'))

def emit_not(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        doc = remove_whether(doc)
        vpos, base, prefix = detect_vpos(doc)
        if vpos == 'NA':
            doc = doc + 'でない'
        else:
            doc = prefix + verb.emit_base(base, vpos, verb.否定形)
        results.append((doc + alt('か@6|かどうか@3|か否か'), transform_not(mcode)))
    return True

# @andor
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する
# results.append(('a % 2 == 0 and', 'aが偶数、かつ、'))
# results.append(('a % 2 == 0 or', 'aが偶数、または、'))

def emit_andor(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        doc = remove_whether(doc)
        vpos, base, prefix = detect_vpos(doc)
        random_factor = random.random()
        if vpos == 'NA' or random_factor < 0.5 :
            pass
        else:
            mode = verb.否定形 if doc.endswith('ない') else 0
            doc = prefix + verb.emit_base(base, vpos, verb.連用形|mode)
        results.append((doc+'、かつ、', f'{mcode} and'))
        results.append((doc+'、または、', f'{mcode} or'))
    return False

# @if if文を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する (バリエーションを作ってもいい)
# results.append(('if a % 2 == 0:', 'もしaが偶数ならば'))
# results.append(('if a % 2 == 0:', 'もしaが偶数のとき'))

def emit_if(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        doc = remove_whether(doc)
        vpos, base, prefix = detect_vpos(doc)
        mode = verb.否定形 if doc.endswith('ない') else 0
        random_factor = random.random()
        if vpos == 'NA' or random_factor < 0.5 :
            results.append((alt('もし|') + doc + alt('ならば|とき|場合'), f'if {mcode} :'))
        if vpos != 'NA' and random.random() < 0.7:
            doc = prefix + verb.emit_base(base, vpos, verb.仮定形|mode) + 'ば'
            results.append((alt('もし|') + doc, f'if {mcode} :'))
        if vpos != 'NA' and random.random() < 0.7:
            doc = prefix + verb.emit_base(base, vpos, verb.過去形|mode) + alt('ならば|なら|ら|とき|場合')
            results.append((alt('もし|') + doc, f'if {mcode} :'))
    if tokibi.OPTION['--partial']:
        emit_andor(code, docs, results, options)
    return False

# @while 文を作る
# 例
# code: a % 2 == 0  docs: ['aが偶数かどうか', 'aが奇数でないかどうか']
# 変換した結果は、results に追加する (バリエーションを作ってもいい)
# results.append(('if a % 2 == 0:', 'もしaが偶数の間'))

def emit_while(code, docs, results, options):
    for doc in docs:
        random_factor = random.random()
        if random_factor < 0.6 :
            mcode, doc = check_modified_code(code, doc)
            doc = remove_whether(doc)
            results.append((doc + '間', f'while {mcode} :'))
    return False


# @then  して〜
# 例
# print() 表示する 
# pi 円周率
# 変換した結果は、results に追加する
# results.append(('print()', '表示して、それを'))
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_then(code, docs, results, options):
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
        mcode, doc = check_modified_code(code, doc)
        vpos, _, _ = detect_vpos(doc)
        if vpos == 'NA':
            results.append((doc+'を'+alt('表示する|確認する|調べる|見る'), mcode))
    return True

# @calc  値 -> 値を算出する
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_calc(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        vpos, _, _ = detect_vpos(doc)
        if vpos == 'NA':
            results.append((doc+'を'+alt('表示する|確認する|調べる|見る'), mcode))
    return True

# @check  値 -> 値を算出する
# results.append(('pi', '円周率')) 名詞は変換しなくてよい

def emit_check(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        vpos, _, _ = detect_vpos(doc)
        if vpos == 'NA':
            results.append((doc+'を'+alt('表示する|確認する|調べる|見る'),mcode))
    return True

# @let

def emit_let(code, docs, results, options):
    name = 'newname' if len(options) == 0 else options[0]        
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
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
        results.append((prefix+suffix, f'{name} = {code}'))
    return False

def emit_let_self(code, docs, results, options):
    emit_let(code, docs, results, options)
    name = code.split('.')[0]
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        vpos, base, prefix = verb.detect_last_vpos(doc)
        if vpos.startswith('V'): #動詞
            random_factor = tokibi.randomize()
            suffix = tokibi.alt('置き換える|再代入する')
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、' + suffix
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、' + suffix
            results.append((prefix+suffix, f'{name} = {mcode}'))
    return False

def emit_inplace(code, docs, results, options):
    name = 'newname'
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        vpos, base, prefix = verb.detect_last_vpos(doc)
        random_factor = tokibi.randomize()
        suffix = tokibi.alt('インプレースする|置き換える')
        if vpos.startswith('V'): #動詞
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、' + suffix
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、' + suffix
            mcode = mcode[:-1] + ', inplace=True)'
            results.append((prefix+suffix, mcode))
    return False

def emit_dot(code, docs, results, options):
    for doc in docs:
        mcode, doc = check_modified_code(code, doc)
        vpos, base, prefix = verb.detect_last_vpos(doc)
        random_factor = tokibi.randomize()
        if vpos.startswith('V'): #動詞
            if random_factor < 0.5:
                suffix = verb.emit_base(base, vpos, verb.連用形)+'、'
            else:
                suffix = verb.emit_base(base, vpos, verb.接続形)+'、'
        else:
            suffix = base+f'の'
        results.append((prefix+suffix, f'{code}.'))
    return False

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
                results.append((doc, code))
                d.add(doc)
    return False

def emit_FIXME(code, docs, results, options):
    pass