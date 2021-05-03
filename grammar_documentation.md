## Grammar Documentation

In this module, each grammar rule is defined by a Python function.

The module starts defining the precedence of the operations.
- ```python
    precedence = (
        ('right', 'EQUALS'),
        ('left', 'PRINT'),
        ('left','multiplier'),
        . . .
        )
Each function accepts a single argument `p` that is a sequence containing the values of each grammar symbol in the corresponding rule.

- ```python
    def p_expression_plus(p):
        'expression : expression PLUS term'
        #   ^            ^        ^    ^
        #  p[0]         p[1]     p[2] p[3]
        p[0] = p[1] + p[3]

## Rules
 defines what an expression is.
- ```python
    p_expression_term(p)
 defines assignment with the format `identifier = expression`
- ```python
    p_assignment(p)

 outputs an error in case there is an syntax error in the input string.
- ```python
    p_error(p)

 defines the addition operation for each subcase, including matrix and vector addition.
- ```python
    p_expression_plus(p)

 defines the subtraction operation for each subcase, including matrix and vector subtraction.
- ```python
    p_expression_minus(p)

defines the dot product operation of two vectors.
- ```python
    p_expression_dot_product_vector(p)

 defines scalar multiplication for vectors and matrices.
- ```python
    p_expression_scalar(p)

 defines the cross product operation of two matrices.
- ```python
    p_expression_cross_product_matrix(p)

defines the transpose of a matrix
- ```python
    p_expression_transpose_matrix(p)

defines the determinant of a matrix
- ```python
    p_expression_det_matrix(p)

defines the inverse of a matrix
- ```python
    p_expression_inverse_matrix(p)

defines the adjugate of a matrix
- ```python
    p_expression_adjugate_matrix(p)

defines the identifier and outputs an error if this identifier was not defined.
- ```python
    p_term_name(p)

prints an expression, e.g. `PRINT identifier`
- ```python
    p_expression_print(p)
