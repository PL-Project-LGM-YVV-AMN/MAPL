import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer_test import tokens
from regexTest import vector
import re



'''def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]'''


'''def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]'''


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


'''def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]'''


'''def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]'''


'''def p_term_factor(p):
    'term : factor'
    p[0] = p[1]'''


'''def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]'''


'''def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]'''

# Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")

def p_term_vector(p):
    '''term : factor
            | vector
            | comma
            | float
            | int'''
    p[0] = p[1]

def p_factor(p):
    '''factor : lCurlyBracket expression rCurlyBracket
              | lHardBracket expression rHardBracket'''
    p[0] = p[2]

'def p_expression_minus(p):'


def p_expression_plus_vector(p):
    'expression : expression plus vector'
    RightVector = vector(p[1])
    LeftVector = vector(p[3])
    max_size = max(RightVector.size,LeftVector.size)
    temp = []
    for i in range(max_size):
        temp.append(float(RightVector.elems[i]) + float(LeftVector.elems[i]))
    temp = vector(re.sub("'", "", str(temp)))
    p[0] = temp
        
    



# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
