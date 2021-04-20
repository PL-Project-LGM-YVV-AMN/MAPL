# Vector Class Documentation

A vector class object admits as its sole argument a string whose regex expression looks like this:
```regex
\[(?:\s*(?:-?'\d+\.\d+|-?\d)\s*)+\]
```

For example, a vector would look something like this:
> [1 2 3]

or some thing like this
> [1.0 2.0 3.0 4]
___

## Class Functions Documentation

- ```python
    def __init__(self,string)
    ```
    - **Purpose**: Constructor
    - **Precondition**: Create a vector object
    - **Post-condition**: Vector object is created

- ```python
    def __str__(self):
    ```
    - **Purpose**: Overload the \_\_str\_\_ operator
    - **Precondition**: Vector object must exist and the inserted string must conform the regex for the vector class
    - **Post-condition**: The _self.elems_ list is converted into a string after being modified to conform to the vector regex

- ```python
    def __add__(self, RightVec)
    ```
    - **Purpose**: Adds two vector objects
    - **Precondition**: The thing in _RightVec_ must be a vector object
    - **Post-condition**: A vector object containing the sum of the elements of both vectors is returned. 
    
- ```python
    def __sub__(self, RightVec)
    ```
    - **Purpose**: Subtracts two vector objects
    - **Precondition**: The thing in _RightVec_ must be a vector object
    - **Post-condition**: A vector object containing the difference of the elements of both vectors is returned
    
- ```python
    def __len__(self)
    ```
    - **Purpose**: Returns the amount of elements in the vector
    - **Precondition**: Vector object must exist
    - **Post-condition**: Returns the size of the vector

- ```python
    def scalar_multiplication(self, multiplier)
    ```
    - **Purpose**: Do the scalar multiplication of the vector object
    - **Precondition**: Vector object must exist
    - **Post-condition**: Returns a vector object containing the _self.elems_ scalar multiplied

- ```python
    def dot_product(self, rightVec)
    ```
    - **Purpose**: Get the dot product of _self_ and _RightVec_
    - **Precondition**: _self_ object must exist and _RightVec_ must be a vector object
    - **Post-condition**: A float value containing the dot product of both vectors is returned

- ```python
    @staticmethod
    def FormatColumnVectors(string)
    ```
    - **Purpose**: Helper function to format the string of _self.elems_. Not intended for use outside of function
    - **Precondition**: A non empty string must be provided
    - **Post-condition**: A string with __'__ and __,__ removed is returned