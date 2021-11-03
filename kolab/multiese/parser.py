import pegtree as pg
from pegtree import ParseTree
from pegtree.visitor import ParseTreeVisitor

peg = pg.grammar('multiese')
parser = pg.generate(peg)


def fix(tree):
    a = [tree.epos_]
    for t in tree:
        fix(t)
        a.append(t.epos_)
    for key in tree.keys():
        a.append(fix(tree.get(key)).epos_)
    tree.epos_ = max(a)
    return tree


class MultieseParser(ParseTreeVisitor):
    def __init__(self):
        ParseTreeVisitor.__init__(self)

    # [#Expression e]

    def acceptExpression(self, tree: ParseTree):
        return self.visit(tree[0])
