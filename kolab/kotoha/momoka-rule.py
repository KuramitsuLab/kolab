
x,y,z = '' 
list, list2 = 'リスト'

_アペンドする = '追加する|アペンドする'
_エクステンドする = '追加する|エクステンドする'

# 動詞で終わります
list.append(x) # listにxをアペンドする
list.extend(list2) # listの最後尾にlist2をエクステンドする

list.myfind(x) # listからx(要素)を探す -> int(位置)