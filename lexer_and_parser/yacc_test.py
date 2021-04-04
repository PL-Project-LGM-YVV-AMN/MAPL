import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer_test import tokens
from vectorClass import vector
from matrixClass import matrix
import re


precedence = (
    ('left','multiplier'),
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
            | int
            | matrix
            | multiplier'''
    p[0] = p[1]

def p_factor(p):
    '''factor : lCurlyBracket expression rCurlyBracket
              | lHardBracket expression rHardBracket'''
    p[0] = p[2]


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

def p_expression_plus_matrix(p):
    'expression : expression plus matrix'
    RightMatrix = matrix(p[3])
    LeftMatrix = matrix(p[1])
    p[0] = LeftMatrix + RightMatrix

def p_expression_minus_matrix(p):
    'expression : expression minus matrix'
    RightMatrix = matrix(p[3])
    LeftMatrix = matrix(p[1])
    p[0] = LeftMatrix - RightMatrix

def p_expression_scalar_vector(p):
    'expression : multiplier vector'
    vecToBeMultiplied = vector(p[2])
    multiplier = float(p[1])
    p[0] = vecToBeMultiplied.scalar_multiplication(multiplier)

def p_expression_scalar_matrix(p):
    'expression : multiplier matrix'
    matrixToBeMultiplied = matrix(p[2])
    multiplier = float(p[1])
    p[0] = matrixToBeMultiplied.scalar_multiplication(multiplier)

def p_expression_cross_product_matrix(p):
    'expression : matrix matrix'
    leftMat = matrix(p[1])
    rightMat = matrix(p[2])
    p[0] = leftMat.cross_product(rightMat)


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

