# Matrix Documentation

A matrix class object admits as its sole argument a string whose regex expression looks like this:
```regex
\[((\[(?:\s*(?:-?'\d+\.\d+|-?\d)\s*)+\])\s*;?)\]
```
For example, a vector would look something like this:
> [[1 2 3]; [4 5 6]; [3 2 1]]

or some thing like this
> [[1.0 2.0 3.0]; [7.0 1 2.3]; [4 8 0.0]]
---
**NOTE**: The matrix class is comprised of vector objects.
## Class Functions Documentation

- ```python
    def __init__(self, string)
    ```
    - **Purpose**: Constructor
    - **Precondition**: Create a matrix object
    - **Post-condition**: Matrix object is created

- ```python
    def __str__(self)
    ```
    - **Purpose**: Overload the \_\_str\_\_ operator
    - **Precondition**: Matrix object must exist and the inserted string must conform the regex for the matrix class
    - **Post-condition**: The row vectors of the matrix will be printed thus printing the matrix in the correct orientation

- ```python
    def __add__(self, RightMatrix)
    ```
    - **Purpose**: Adds two matrix objects
    - **Precondition**: The thing in _RightMatrix_ must be a matrix object
    - **Post-condition**: A matrix object containing the sum of the elements of both matrix is returned

- ```python
    def __sub__(self,RightMatrix)
    ```
    - **Purpose**: Subtracts two matrix objects
    - **Precondition**: The thing in _RightMatrix_ must be a matrix object
    - **Post-condition**: A matrix object containing the difference of the elements of both matrix is returned

- ```python
    def scalar_multiplication(self, multiplier)
    ```
    - **Purpose**: Do the scalar multiplication of the matrix object
    - **Precondition**: Matrix object must exist
    - **Post-condition**: Returns a vector object containing the _self.elems_ of the row vectors scalar multiplied

- ```python
    def cross_product(self, rightMat)
    ```
    - **Purpose**: Do the cross product of _self_ object with another vector. For example, self.cross_product(B) means _**AB**_
    - **Precondition**: Matrix object must exist and _rightMat_ must also be a matrix object
    - **Post-condition**: A matrix object containing the cross product of two matrices is returned. If _self.numOfRows_ does not equal _rightMat.numOfRows_  

- ```python
    def transpose(self)
    ```
    - **Purpose**: Get the transpose of _self_
    - **Precondition**: Matrix object must exist
    - **Post-condition**:  A matrix object containing the transpose, meaning the rows become columns and columns become rows, of _self_ is returned

- ```python
    def det(self)
    ```
    - **Purpose**: Returns the determinant of _self_
    - **Precondition**: Matrix object must exist
    - **Post-condition**: The determinant of _self_ is returned as a float, If _self.isSqaure_ is set to false, the function will return _None_   