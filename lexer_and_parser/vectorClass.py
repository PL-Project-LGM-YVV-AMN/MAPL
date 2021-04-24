import lexer as lt
import re


class vector:
    """
    A class used to represent a mathematical vector
    Attributes
    ----------
    elems : list
        a list of float or integers
    size : int
        the amount of float or integers in elems
    Methods
    scalar_multiplication(multiplier)
        multiplies the elements of self and returns a new vector 
        object
    """
    elemsRule = re.compile((r'-?' + lt.t_float + r'|-?' + lt.t_int))

    def __init__(self, string: str) -> "vector":
        """
        Parameters
        ----------
        string : str
            needs to be compliant with vector regex from in lexer.py as t_vector
        """
        self.elems = vector.elemsRule.findall(string)
        self.size = len(self.elems)

    def __str__(self) -> str:
        """
        returns the vector elements formatted to be compliant with vector regex
        """
        result = re.sub(r'\'', '', str(self.elems))
        result = re.sub(",","", str(result))
        return result

    def __add__(self, RightVec: "vector") -> "vector":
        """
        returns a vector object containing the sum of self and Rightvector
        Parameters
        ----------
        RightVec : vector
            must be of the same size as self
        """
        result = []
        if self.size != RightVec.size:
            print("Vectors are not of equal size")
            return None
        for i in range(self.size):
            result.append(float(self.elems[i])+float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult

    def __sub__(self, RightVec: "vector") -> "vector":
        """
        returns a vector object containing the difference of self and RightVec
        Parameters
        ----------
        RightMatrix : matrix
            must be of the same size as self
        """
        result = []
        if self.size != RightVec.size:
            print("Vectors are not of equal size")
            return None
        for i in range(self.size):
            result.append(float(self.elems[i])-float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult
    
    def __len__(self) -> int:
        """
        returns the amount of elements in the vector object
        """
        return self.size

    def scalar_multiplication(self, multiplier: float) -> "vector":
        """
        returns a vector object containing the elements of self
        scalar multiplied by a factor by multiplier
        Parameters
        ----------
        multiplier : float
            the value by which the vector will be multiplied by
        """
        multiplied_vec = []
        for i in range(self.size):
            multiplied_vec.append(float(self.elems[i])*multiplier)
        return vector(vector.FormatColumnVectors(str(multiplied_vec)))

    @staticmethod
    def FormatColumnVectors(string: str) -> str:
        """
        removes commas and single quotes from string
        Parameters
        ----------
        string : str
            must be a the string of a list containing strings
        """
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result

    def dot_product(self, rightVec: "vector") -> float:
        """
        returns the dot product of rightVec and self.
        If rightVec is not the same size as self, will return none
        Parameters
        ----------
        rightVec : vector
            must be of the same size for the operation to be executed
        """
        product_nums = []
        if self.size != rightVec.size:
            print("Vectors are not of equal size")
            return None
        for i in range(self.size):
            product_nums.append(float(self.elems[i])*float(rightVec.elems[i]))
        return sum(product_nums)



# x = vector("[1 2 3]")
# y = vector("[4 5 6]")
#
# temp = x.__str__()
# print()


