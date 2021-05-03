import ply.yacc as yacc
from lexer import tokens, t_vector, t_matrix
from vectorClass import vector
from matrixClass import matrix
import re


precedence = (
    ('right', 'EQUALS'),
    ('left', 'PRINT'),
    ('left','multiplier'),
    ('left', 'crossProduct'),
    ('left', 'transpose'),
    ('left', 'determinant'),
    ('left', 'inverse'),
    ('left', 'adjugate'),
    ('left', 'plus', 'minus'),
    ('left', 'dotProduct'),
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
    left_thing_str = str(p[1])
    right_thing_str = str(p[3])
    if re.match(t_vector, left_thing_str) and re.match(t_vector, right_thing_str):
        LeftThing = vector(left_thing_str)
        RightThing = vector(right_thing_str)
    elif re.match(t_matrix, left_thing_str) and re.match(t_matrix, right_thing_str):
        LeftThing = matrix(left_thing_str)
        RightThing = matrix(right_thing_str)
    else:
        return None
    p[0] = LeftThing+RightThing

def p_expression_minus(p):
    'expression : expression minus expression'
    left_thing_str = str(p[1])
    right_thing_str = str(p[3])
    if re.match(t_vector, left_thing_str) and re.match(t_vector, right_thing_str):
        LeftThing = vector(left_thing_str)
        RightThing = vector(right_thing_str)
    elif re.match(t_matrix, left_thing_str) and re.match(t_matrix, right_thing_str):
        LeftThing = matrix(left_thing_str)
        RightThing = matrix(right_thing_str)
    else:
        return None
    p[0] = LeftThing-RightThing

def p_expression_dot_product_vector(p):
    'expression : expression dotProduct expression'
    left_vec_str = str(p[1])
    right_vec_str = str(p[3])
    if not(re.match(t_vector, p[1]) and re.match(t_vector, p[3])):
        return None
    p[0] = vector(left_vec_str).dot_product(vector(right_vec_str))

def p_expression_scalar(p):
    'expression : multiplier expression'
    thing_str = str(p[2])
    if re.match(t_vector, thing_str):
        thingToBeMultiplied = vector(thing_str)
    elif re.match(t_matrix, thing_str):
        thingToBeMultiplied = matrix(thing_str)
    else:
        return None
    p[0] = thingToBeMultiplied.scalar_multiplication(float(p[1]))

def p_expression_cross_product_matrix(p):
    'expression : expression crossProduct expression'
    left_mat_str = str(p[1])
    right_mat_str = str(p[3])
    if not (re.match(t_matrix, left_mat_str) and re.match(t_matrix, right_mat_str)):
        return None
    leftMat = matrix(left_mat_str)
    rightMat = matrix(right_mat_str)
    p[0] = leftMat.cross_product(rightMat)

#Needs to change symbol so it doesn't confuse transpose with an identifier 
def p_expression_transpose_matrix(p):
    'expression : transpose expression'
    mat_str = str(p[2])
    if not(re.match(t_matrix, mat_str)):
        return None
    p[0] = matrix(mat_str).transpose()

def p_expression_det_matrix(p):
    'expression : determinant expression determinant'
    mat_str = str(p[2])
    if not(re.match(t_matrix, mat_str)):
        return None
    p[0] = matrix(mat_str).det()


#Needs to change symbol so it doesn't confuse inv with an identifier 
def p_expression_inverse_matrix(p):
    'expression : inverse expression'
    thing_str = str(p[2])
    if not(re.match(t_matrix, thing_str)):
        return None
    p[0] = matrix(thing_str).inv()

#Needs to change symbol so it doesn't confuse adjugate with an identifier 
def p_expression_adjugate_matrix(p):
    'expression : adjugate expression'
    thing_str = str(p[2])
    if not(re.match(t_matrix, thing_str)):
        return None
    p[0] = matrix(thing_str).adjugate()

def p_term_name(p):
    'term : identifier'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print('Unknown name ', p[1])
        p[0] = 0

def p_expression_print(p):
    'expression : PRINT expression'
    print(p[2])
    p[0] = None

parser = yacc.yacc()
if __name__ == "__main__":
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print(result)