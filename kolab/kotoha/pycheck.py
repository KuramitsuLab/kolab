import sys
import pegtree as pg

tpeg = pg.grammar('pynmt.pegtree')
parser = pg.generate(tpeg, start = 'Checker')
parser2 = pg.generate(tpeg, start = 'Statement')

def check_syntax(s: str):
    """
    Python の構文的に正しいかどうか
    """
    tree = parser(s.strip())
    # print(repr(tree))
    # return not tree.isSyntaxError()
    return tree.isSyntaxError()

def fix(tree):
    a = [tree.epos_]
    for t in tree:
        fix(t)
        a.append(t.epos_)
    for key in tree.keys():
        a.append(fix(tree.get(key)).epos_)
    tree.epos_ = max(a)
    return tree

def filter_syntax(s: str):
    """
    Pythonの構文的に正しいところまで取り出す。
    """
    tree = parser2(s.strip())
    return str(fix(tree))


def main(argv):
    err_sum = 0
    line_sum = 0

    if len(argv) == 0:
        pass
    else:
        filename = argv[0]
        with open(filename) as f:
            for line in f:
                line_sum += 1
                err_sum += check_syntax(line)

    print(f'Error rate : {err_sum}/{line_sum} ({err_sum / line_sum})')


if __name__ == '__main__':
    main(sys.argv[1:])
    # print(check_syntax(" df . head ( ) "))
    # print(check_syntax(" df . groupby ( [ 'month' , 'period' ] ) [ 'sales' ] . sum ( "))
    # print(filter_syntax(" df . groupby ( [ 'month' , 'period' ] ) [ 'sales'  . sum (  "))

