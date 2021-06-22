from janome.tokenizer import Tokenizer

t = Tokenizer()

token = t.tokenize('走れ').__next__()

print(token)
print(token.infl_type)


def pj(s):
    for tok in t.tokenize(s):
        print(tok, tok.infltype)


pj('赤くない')
pj('赤い#not')
pj('書ける')
pj('書ければ')
pj('書かせる')
pj('書かせてみる')
pj('置換する')
pj('置き換える')


janome = Tokenizer()


def pj(s):
    for tok in janome.tokenize(s):
        print(list(tok), tok.infltype)


pj('赤くない')
pj('赤い#not')
pj('書ける')
pj('書ければ')
pj('書かせる')
pj('書かせてみる')
pj('置換する')
pj('置き換える')
