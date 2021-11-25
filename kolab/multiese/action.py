import random

Functions = globals()

def remove_whether(sentence):
    if sentence.endswith('かどうか'):
        return sentence[:-4], 'かどうか'
    if sentence.endswith('か否か'):
        return sentence[:-4], 'か否か'
    if sentence.endswith('か'):
        return sentence[:-1], 'か'
    return sentence, ''

def transform_not(code):
    if '==' in code:
        return code.replace('==', '!=')
    if '!=' in code:
        return code.replace('!=', '==')
    if ' is ' in code and not 'is not' in code:
        return code.replace(' is ', ' is not ')
    if ' in ' in code and not 'not in' in code:
        return code.replace(' in ', ' not in ')
    if 'True' in code:
        return code.replace('True', 'False')
    if 'False' in code:
        return code.replace('False', 'True')
    return f'not {code}'

def perform_not(pairs, option):
    pairs_not = []
    for sentence, code in pairs:
        code_not = transform_not(code)
        sentence, whether = remove_whether(sentence)
        if 'でない' in sentence:
            sentence_not = sentence.replace('でない', '') + whether
        else:
            sentence_not = sentence + 'でない' + whether
        pairs_not.append((sentence_not, code_not))
    return pairs_not

def optional_choice(option, s, seed=0):
    choice = s.split('|') if isinstance(s, str) else s
    r = option.get('random', random.random())
    max = len(choice)
    return choice[int(max * r + seed) % max]

def perform_if(pairs, option):
    ## pairs.extends(perform_not(pairs, option)) # @@not を加える
    pairs_if = []
    for sentence, code in pairs:
        code_if = f'if {code} :'
        sentence, _ = remove_whether(sentence)
        sentence_if = optional_choice(option, 'もし|もし|') + sentence
        sentence_if += optional_choice(option, 'ならば|なら|の場合|のとき')
        pairs_if.append((sentence_if, code_if))
    return pairs_if

def perform_while(pairs, option):
    pairs_while = []
    for sentence, code in pairs:
        code_while = f'while {code} :'
        sentence, _ = remove_whether(sentence)
        sentence_while = sentence + 'の間'
        pairs_while.append((sentence_while, code_while))
    return pairs_while

def perform_check(pairs, option):
    pairs_check = []
    for pair in pairs:
        code = pair[1]
        r = option.get('random', random.random())
        if r < 0.3:
            sentence_check = pair[0] + 'を表示する'
        elif r < 0.5:
            sentence_check = pair[0] + 'を確認する'
        elif r < 0.7:
            sentence_check = pair[0] + 'を調べる'
        else:
            sentence_check = pair[0] + 'を見る'
        pairs_check.append((sentence_check, code))
    return pairs_check

def perform_get(pairs, option):
    pairs_get = []
    for pair in pairs:
        code = pair[1]
        r = option.get('random', random.random())
        if r < 0.3:
            sentence_get = pair[0] + 'を取得する'
        elif r < 0.7:
            sentence_get = pair[0] + 'を得る'
        else:
            sentence_get = pair[0] + 'を抽出する'
        pairs_get.append((sentence_get, code))
    return pairs_get

def perform_calc(pairs, option):
    pairs_calc = []
    for pair in pairs:
        code = pair[1]
        r = option.get('random', random.random())
        if r < 0.3:
            sentence_calc = pair[0] + 'を計算する'
        elif r < 0.7:
            sentence_calc = pair[0] + 'を求める'
        else:
            sentence_calc = pair[0] + 'を算出する'
        pairs_calc.append((sentence_calc, code))
    return pairs_calc

def perform_filter(actions, pairs, option):
    actions = actions.split('.')   # e.g.: @@if.not
    for action in actions:
        f = f'perform_{action}'
        if f in Functions:
            pairs = Functions[f](pairs, option)
    return pairs


if __name__ == '__main__':
    print(Functions)
    perform_filter('not.if', [], {})
