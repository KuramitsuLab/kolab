import sys
import pegtree as pg

tpeg = pg.grammar('pyline.pegtree')
parser = pg.generate(tpeg)

def fix(tree):
    a = [tree.epos_]
    for t in tree:
        fix(t)
        a.append(t.epos_)
    for key in tree.keys():
        a.append(fix(tree.get(key)).epos_)
    tree.epos_ = max(a)
    return tree

def readfile(filename, head=None):
    with open(filename, 'r') as f:
        for i, line in enumerate(f.readlines()):
            tree = parser(line)
            if len(tree) > 0:
                for t in tree:
                    if t.tag_ != 'Name':
                        print(fix(t))
                    #print(repr(fix(t)))
            if i == head:
                break

if __name__ == '__main__':
    for filename in sys.argv[1:]:
        readfile(filename)