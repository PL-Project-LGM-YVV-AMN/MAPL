import ply.lex as lex

tokens = (
    'rHardBracket',
    'lHardBracket',
    'int',
    'float',
    'plus',
    'minus',
    'dotProduct',
    'crossProduct',
    'comma',
    'rCurlyBracket',
    'lCurlyBracket',
    'vector'
)

t_lHardBracket = r'\['
t_rHardBracket = r'\]'
t_int = r'\d+'
t_float = r'\d+\.\d+'
t_plus = r'\+'
t_minus = r'\-'
t_dotProduct = r'\.'
t_crossProduct = 'X'
t_comma = r'\,'
t_lCurlyBracket = r'\{'
t_rCurlyBracket = r'\}'
t_vector = t_lHardBracket + r'((' + t_float + r'|' + t_int + r')\s*)+' + t_rHardBracket
t_ignore = ' \t'

print

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
"""
if __name__ == "__main__":
    data = input("Input data: ")
    lexer.input(data)
    for tok in lexer:
        print(tok)
"""
