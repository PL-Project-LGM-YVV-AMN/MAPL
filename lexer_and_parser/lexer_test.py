import ply.lex as lex
# Poner los tokens en mayúscula
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
    # 'KEYWORDS',
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
t_multiplier = r'\s*(?:-?' + t_float + r'|-?' + t_int + r')'
t_transpose = r"\s*\s*T"
t_inverse = r'inv'
t_adjugate = r'adjugate'
t_ignore = ' \t'
# t_KEYWORDS = (
#     'inv',
#     'adjugate',
#     'transpose',
# )

def t_identifier(t):
    r'[a-zA-Z_]([a-zA-Z_0-9])*'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass
    # No return value. Token discarded

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    data = input("Input data: ")
    lexer.input(data)
    for tok in lexer:
        print(tok)
