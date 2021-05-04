import ply.lex as lex

tokens = (
    'identifier',
    'EQUALS',
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
    'vector',
    'matrix',
    'multiplier',
    'transpose',
    'determinant',
    'inverse',
    'adjugate',
    'PRINT'
)

t_EQUALS = r"="
t_lHardBracket = r'\['
t_rHardBracket = r'\]'
t_int = r'\d+'
t_float = r'\d+\.\d+'
t_plus = r'\+'
t_minus = r'\-'
t_dotProduct = r'\.'
t_crossProduct = r'\*'
t_determinant = r'\|'
t_comma = r'\,'
t_lCurlyBracket = r'\{'
t_rCurlyBracket = r'\}'
t_vector = t_lHardBracket + \
    r'(?:\s*(?:-?' + t_float + r'|-?' + t_int + r')\s*)+' + t_rHardBracket
t_matrix = t_lHardBracket + r'((' + t_vector + r')\s*;?)+' + t_rHardBracket
t_multiplier = r'\s*(?:-?' + t_float + r'|-?' + t_int + r')\s*'
t_transpose = r"T"
t_inverse = r'INV'
t_adjugate = r'ADJUGATE'
t_PRINT = r'PRINT'
t_ignore = ' \t'

def t_identifier(t):
    r'[a-z_]+'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    data = input("Input data: ")
    lexer.input(data)
    for tok in lexer:
        print(tok)

