import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexer_test import tokens, t_vector, t_matrix
from vectorClass import vector
from matrixClass import matrix
import re


precedence = (
    #('left', 'KEYWORDS')
    ('right', 'EQUALS'),
    ('left','multiplier'),
    ('left', 'plus', 'minus'),
)

names = {}

def p_assignment(p):
    'expression : identifier EQUALS expression'
    names[p[1]] = p[3]

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


def p_expression_plus(p):
    'expression : expression plus expression'
    if re.match(t_vector, p[1]) and re.match(t_vector, p[3]):
        RightThing = vector(p[1])
        LeftThing = vector(p[3])
    elif re.match(t_matrix, p[1]) and re.match(t_matrix, p[3]):
        RightThing = matrix(p[1])
        LeftThing = matrix(p[3])
    else:
        return None
    p[0] = RightThing+LeftThing


def p_expression_minus(p):
    'expression : expression minus expression'
    if re.match(t_vector, p[1]) and re.match(t_vector, p[3]):
        RightThing = vector(p[1])
        LeftThing = vector(p[3])
    elif re.match(t_matrix, p[1]) and re.match(t_matrix, p[3]):
        RightThing = matrix(p[1])
        LeftThing = matrix(p[3])
    p[0] = RightThing-LeftThing

def p_expression_scalar(p):
    'expression : multiplier expression'
    if re.match(t_vector, p[2]):
        thingToBeMultiplied = vector(p[2])
    elif re.match(t_matrix,p[2]):
        thingToBeMultiplied = matrix(p[2])
    else:
        return None
    p[0] = thingToBeMultiplied.scalar_multiplication(float(p[1]))

def p_expression_cross_product_matrix(p):
    'expression : expression crossProduct expression'
    if not (re.match(t_matrix, p[1]) and re.match(t_matrix, p[3])):
        return None
    leftMat = matrix(p[1])
    rightMat = matrix(p[3])
    p[0] = leftMat.cross_product(rightMat)

#Needs to change symbol so it doesn't confuse transpose with an identifier 
def p_expression_transpose_matrix(p):
    'expression : transpose expression'
    if not(re.match(t_matrix, p[2])):
        return None
    p[0] = matrix(p[2]).transpose()

def p_expression_det_matrix(p):
    'expression : determinant expression determinant'
    if not(re.match(t_matrix, p[2])):
        return None
    p[0] = matrix(p[2]).det()

def p_expression_dot_product_vector(p):
    'expression : expression dotProduct expression'
    if not(re.match(t_vector, p[1] and re.match(t_vector, p[3]))):
        return None
    p[0] = vector(p[1]).dot_product(vector(p[3]))

#Needs to change symbol so it doesn't confuse inv with an identifier 
def p_expression_inverse_matrix(p):
    'expression : inverse expression'
    if not(re.match(t_matrix, p[2])):
        return None
    p[0] = matrix(p[2]).inv()

#Needs to change symbol so it doesn't confuse adjugate with an identifier 
def p_expression_adjugate_matrix(p):
    'expression : adjugate expression'
    if not(re.match(t_matrix, p[2])):
        return None
    p[0] = matrix(p[2]).adjugate()

def p_term_name(p):
    'term : identifier'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print('Unknown name ', p[1])
        p[0] = 0

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

