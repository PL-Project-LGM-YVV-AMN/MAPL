import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer_test import tokens
from VectorClass import vector
import re


precedence = (
    ('left', 'plus', 'minus'),
)

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

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
    if LeftVector.size != RightVector.size:
        print("Vectors are not of equal size")
        return
    p[0] = RightVector+LeftVector

def p_expression_minus_vector(p):
    'expression : expression minus vector'
    RightVector = vector(p[1])
    LeftVector = vector(p[3])
    if LeftVector.size != RightVector.size:
        print("Vectors are not of equal size")
        return
    p[0] = RightVector-LeftVector
        
    



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

