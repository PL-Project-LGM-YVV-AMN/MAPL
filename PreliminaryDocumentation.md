# Preliminary Documentation
## Operators and Special Characters
| Operator | Character |
|--|--|
| + | Addition operator |
| - | Subtraction operator |
| * | Scalar and matrix multiplication operator |
| ^ | Scalar and matrix exponentiation operator|
| / | Right-division operator |
| () |  Encloses function arguments; overrides precedence |
| . | Decimal point; dot product |
| , | separates statements and elements in a row |
| ; | End of statement operator |
| % | designates a comment and specifies formatting| 
| ' | transpose operator |
| = | Assignment operator |

## Variables
MOPL is a strong typed language

### Variable identifier

The variable identifier cannot:
1.	Start with a number. e.g. `1var`
2.	Have a special character in it. e.g. `var'`

## Vectors
MATLAB has two types of vectors

 1. Row vectors
 **Row vectors** are created by enclosing the set of elements in square brackets, using space or comma to delimit the elements.
 ```MATLAB
 rvec v =  [7  8  9  10  11]
 ```
 2. Column vectors
**Column vectors** are created by enclosing the set of elements in square brackets, using semicolon to delimit the elements.
```MATLAB
cvec =  [7;  8;  9;  10;  11]
```

### Referencing the elements of a vector

```MATLAB
cvec v =  [  1;  2;  3;  4;  5;  6];  % creating a column vector of  6 elements
v(3) % Returns the fourth element
```

### Creating matrices
In MATLAB, you create a matrix by entering elements in each row as comma or space delimited numbers and using semicolons to mark the end of each row.

For example, let us create a 4-by-5 matrix *a*:
```MATLAB
matrix a =  [  1  2  3  4  5;  2  3  4  5  6;  3  4  5  6  7;  4  5  6  7  8]
```

### Referencing the elements of a matrix
```MATLAB
a[1, 2];
```

## Functions
### Calling functions
functionName(A) for a 1 predicate function
functionName(A, B) for a 2 predicate function

*MOPL is limited to predefined functions, for the time being.*

### Predefined functions
| function | purpose |
|--|--|
| length | Computes number of elements |
| eye | Creates an identity matrix |
| cross | Computes matrix cross products |
| dot | Computes matrix dot products |
| det | Computes determinant of a matrix|
| inv | Computes inverse of a matrix |
| rank | Computes rank of a matrix |
| rref | Computes reduced row echelon form |
| log | outputs to the console |

## Data types
| Data type | Description |
|--|--|
| int | 8-bit signed integer.|
| double | up to 4 decimal places |
| matrix | MATLAB doesn't have this data type but we should, in my opinion |
| vector | MATLAB doesn't have this data type but we should, in my opinion |

## Control Statements

*For the moment, MOPL won't implement control statements. Since we have only a semester to develop this PL, we're limiting our scope to the basic features and operation we think are fundamental*


## Loops
*For the moment, MOPL won't implement Loops. Since we have only a semester to develop this PL, we're limiting our scope to the basic features and operation we think are fundamental*
