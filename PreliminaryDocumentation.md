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
| . | Decimal point |
| , | separates statements and elements in a row |
| ; | End of statement operator. **Do we need this?**|
| % | designates a comment and specifies formatting| 
| ' | transpose operator |
| = | Assignment operator |
| _ | Matrix accessor operator e.g. `A_12` Access matrix A element in row 1 column 2 **Just an idea**|
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |
| == | Equal to |
| ~= OR != | Not equal to |
| & | And |
| \| | Or |
| ~ OR ! | Not |

## Variables

### Variable identifier

The variable identifier cannot:
1.	Start with a number. e.g. `1var`
2.	Have a special character in it. e.g. `var'`

### **Important questions**
1.	End of statement operator ";" ?
 2.	Is it strong typed or weak typed?
 If it is strong typed then variable assignment would be like:
 
```MATLAB
int x = 4
```

And if it is weak typed then would be like:
```MATLAB
x = 4
```

> MATLAB is weak typed.

3.	Does variable declaration and assignment need to happen in the same line?
	E.g.
	```MATLAB
	x = 4
	```
If if not then would be something like:
```MATLAB
	x;
```
If this is the case then implicitly it has to assign an `undefined` value.
`x` same as `x = undefined`
	
4.	Multiple Assignments ?
```MATLAB
x = y = z = 1
```

5.	Decimal point
Many programming languages make a distinction between "short" decimal point values and "long" decimal point values.
For example MATLAB make this distinction. 
A "short" is a four decimal place value.
So, `x = 3.1.` is implicitly `3.1000`
A long is a 16 decimal place value.
So, `x = 3.31201849182649331`
In MATLAB if we want a long we have to specify it.
One easy not so elegant way we can handle this is by making `long` or `short` the default or the only decimal type.

6.	Arrays and other data types?
	I think we should limit this language to deal just with simple data types and matrices and vectors.
## Vectors
MATLAB has two types of vectors

 1. Row vectors
 **Row vectors** are created by enclosing the set of elements in square brackets, using space or comma to delimit the elements.
 ```MATLAB
 r =  [7  8  9  10  11]
 ```
 3. Column vectors
**Column vectors** are created by enclosing the set of elements in square brackets, using semicolon to delimit the elements.
```MATLAB
c =  [7;  8;  9;  10;  11]
```

### Referencing the elements of a vector

```MATLAB
v =  [  1;  2;  3;  4;  5;  6];  % creating a column vector of  6 elements
v(3) % Returns the fourth element
```

> I think it's easier a strong typed language. That way declaring a
> column vector would be something like
> ```MATLAB
> c : colv = [1 2 3 4 5]
> ```
>  or 
> ```MATLAB
> colv c = [1 2 3 4 5 6]
> ```

### Creating matrices
In MATLAB, you create a matrix by entering elements in each row as comma or space delimited numbers and using semicolons to mark the end of each row.

For example, let us create a 4-by-5 matrix *a*:
```MATLAB
a =  [  1  2  3  4  5;  2  3  4  5  6;  3  4  5  6  7;  4  5  6  7  8]
```

if our PL is strong typed then should we specify the size of the matrix in the declaration?
```MATLAB
3x3 A = [1 2 3; 4 5 6; 7 8 9]
```

### Referencing the elements of a matrix
```MATLAB
a(1, 2);
```
Maybe we could have a notation like:
`a_1_2` or `a_1-2`


## Functions
### Calling functions
functionName(A) for a 1 predicate function
functionName(A, B) for a 2 predicate function

### QUESTION
Is it necessary to allow users to declare their own functions?
I think we should limit this PL to work only on pre-defined functions.

### Predefined functions
| function | purpose |
|--|--|
| cat | Concatenates arrays |
| length | Computes number of elements |
| eye | Creates an identity matrix |
| cross | Computes matrix cross products |
| dot | Computes matrix dot products |
| det | Computes determinant of an array |
| inv | Computes inverse of a matrix |
| rank | Computes rank of a matrix |
| rref | Computes reduced row echelon form |

## Data types
| Data type | Description |
|--|--|
| int | 8-bit signed integer.|
| double | up to 4 decimal places |
| bool| logical values of 1 or 0, represent true and false respectively |
| matrix | MATLAB doesn't have this data type but we should, in my opinion |
| vector | MATLAB doesn't have this data type but we should, in my opinion |

In matlab everything is either  a matrix or an array.

> MATLAB provides 15 fundamental data types. Every data type stores data
> that is in the form of a matrix or array. The size of this matrix or
> array is a minimum of 0-by-0 and this can grow up to a matrix or array
> of any size.

E.g.
```MATLAB
Total = 42
```

> The above statement creates a 1-by-1 matrix named 'Total' and stores
> the value 42 in it.

## DECISIONS

#### 

*if* statement
```MATLAB
if <expression>
   % statement(s) will execute if the boolean expression is true 
   <statements>
end
```
*if…else*
```MATLAB
if <expression>
   % statement(s) will execute if the boolean expression is true 
   <statement(s)>
else
   <statement(s)>
   % statement(s) will execute if the boolean expression is false 
end
```

*if…elif…elif…else…*

```MATLAB
if <expression 1>
   % Executes when the expression 1 is true 
   <statement(s)>
elif <expression 2>
   % Executes when the boolean expression 2 is true
   <statement(s)>
elif <expression 3>
   % Executes when the boolean expression 3 is true 
   <statement(s)>
else 
   %  executes when the none of the above condition is true 
   <statement(s)>
end
```

## Loops
**Should we implement loops?**
- while loop
- for loop
- break statmeent
- continue statement

## Strings
```MATLAB
str = 'a simple string'
```
