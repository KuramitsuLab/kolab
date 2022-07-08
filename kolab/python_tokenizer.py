from io import BytesIO
import tokenize
import keyword
import re
import click


def tokenize_code(text: str) -> list:
    """
    （Python に限らず）ソースコードを字句分割する

    Args:
        text (str): ソースコード

    Returns:
        list 字句リスト
    """

    text = re.sub(r'([^A-Za-z0-9_])', r' \1 ', text)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('"', '`')
    text = text.replace('\'', '`')
    tokens = [t for t in text.split(' ') if t]
    return tokens


VALUE = set(['True', 'False', 'None'])
SPACE = set(['return', ''])


def iskeyword(s):
    if s in VALUE:
        return False
    return keyword.iskeyword(s)


def tokenize_python_code(src: str) -> list:
    """
    Python ソースコードを字句分割する

    Args:
        src (str): ソースコード

    Returns:
        list 字句リスト
    """
    try:
        ss = []
        # tokenize the string
        g = tokenize.tokenize(BytesIO(src.encode('utf-8')).readline)
        for toknum, tokval, _, _, _ in g:
            #print(toknum, tokval)
            if toknum in (tokenize.COMMENT, tokenize.ENCODING):
                continue
            if len(tokval) > 0:
                ss.append(tokval)
        return ss
    except tokenize.TokenError:
        return tokenize_code(src)


@click.command()
@click.argument('filename')
def read_and_show(filename, fn=tokenize_python_code):
    with open(filename) as f:
        print(fn(f.read()))


if __name__ == '__main__':
    read_and_show()
