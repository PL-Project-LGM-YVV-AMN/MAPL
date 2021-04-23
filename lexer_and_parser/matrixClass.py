import lexer as lt
from vectorClass import vector
import re
import math
class matrix:
    """
    **A class used to represnt a matrix**

    Attributes
    ----------
    numOfRows : int
        the number of vectors found in the string 
    RowVecs : list
        a list of vector objects created from the string
    size : int
        the amount of elements in the matrix 
    numOfColumns : int
        the number of columns in the matrix
    ColumnVecs : list
        a list of vector objects created from RowVecs
    isSqaure : bool
        is true if the matrix has a sqaure number of elements, else false

    Methods
    -------
    scalar_multiplication(multiplier)
        Returns a matrix object containing the the elements 
        of self scalar multiplied\n
    cross_product(rightMat)
        Returns a matrix object containing the the elements 
        of self cross multiplied with the elements of rightMat\n
    tanspose()
        Returns a matrix object containing the the elements 
        of self transposed\n
    det()
        Returns the determinant of self\n
    inv()
        Returns a matrix object containing the inverse of self\n
    adjugate()
        Returns a matrix object containing the adjugate of self\n
    """
    
    VectorRule = re.compile(lt.t_vector)

    def __init__(self, string: str):
        """
        Parameters
        ----------
        string : str
            needs to be compliant with matrix regex
        """
        RowVecsFromRE = matrix.VectorRule.findall(string)
        self.numOfRows = len(RowVecsFromRE)
        self.RowVecs = []
        sizeOfVecs = []
        for i in range(self.numOfRows):
            self.RowVecs.append(vector(matrix.FormatColumnVectors(RowVecsFromRE[i])))
            sizeOfVecs.append(len(self.RowVecs[i]))
        maxRowSize = max(sizeOfVecs)
        for j in range(self.numOfRows):
            self.RowVecs[j] =  matrix.appendZeroes(self.RowVecs[j],self.RowVecs[j].size,maxRowSize)
        ColumnVecs = []
        temp_list = []
        for k in range(maxRowSize):
            if k != 0:
                ColumnVecs.append(temp_list[:])
                temp_list.clear()
            for z in range(self.numOfRows):
                temp_list.append(self.RowVecs[z].elems[k])
        ColumnVecs.append(temp_list[:])
        self.size = maxRowSize*self.numOfRows
        self.numOfColumns = len(ColumnVecs)
        self.ColumnVecs = []
        for i in range(self.numOfColumns):
            self.ColumnVecs.append(vector(matrix.FormatColumnVectors(ColumnVecs[i])))
        self.isSquare = False
        if math.sqrt(self.size) == math.floor(math.sqrt(self.size)):
            self.isSquare = True

    def __str__(self) -> str:
        """
        returns the row vectors formatted to be compliant with matrix regex
        """
        ans = ""
        for i in range(self.numOfRows-1):
           ans += "[" + vector.__str__(self.RowVecs[i]) + ';'
        ans +=  vector.__str__(self.RowVecs[self.numOfRows-1]) + "]"
        return ans

    def __add__(self,RightMatrix):
        """
        returns a matrix object containing the sum of self and RightMatrix
        Parameters
        ----------
        RightMatrix : matrix
            must be of the same size as self
        """
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfRows):
            vecList.append(self.RowVecs[vecs] + RightMatrix.RowVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def __sub__(self,RightMatrix):
        """
        returns a matrix object containing the difference of self and RightMatrix
        Parameters
        ----------
        RightMatrix : matrix
            must be of the same size as self
        """
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfRows):
            vecList.append(self.RowVecs[vecs] - RightMatrix.RowVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def scalar_multiplication(self, multiplier: float):
        """
        returns a matrix object containing the elements of self
        scalar multiplied by a factor by multiplier
        Parameters
        ----------
        multiplier : float
            the value by which the matrix will be multiplied by
        """
        vecList = []
        for i in range(self.numOfColumns):
            vecList.append(self.RowVecs[i].scalar_multiplication(multiplier))
        return matrix(matrix.formatList(vecList))

    def cross_product(self, rightMat):
        """
        **returns a matrix object containing the cross product with rightMat.**\n
        rightMat.numOfRows must equal to self.numOfColumns for the operation to be performed
        otherwise None will be returned
        Parameters
        ----------
        rightMat : matrix
            numOfRows must equal to self.numOfColumns for the operation to be performed
        """
        if self.numOfColumns != rightMat.numOfRows:
            print("Left matrix's number of columns not equal to right matrix's number of rows")
            return None
        new_row_vecs = []
        temp_list = []
        for row in range(self.numOfRows):
            new_row_vecs.append(temp_list[:])
            temp_list.clear()
            for column in range(rightMat.numOfColumns):
                temp_list.append(self.RowVecs[row].dot_product(rightMat.ColumnVecs[column]))
        new_row_vecs.append(temp_list[:])
        new_row_vecs = [x for x in new_row_vecs if x]
        new_mat_str_list = []
        for i in range(len(new_row_vecs)):
            new_mat_str_list.append(vector(vector.FormatColumnVectors(new_row_vecs[i])))
        return matrix(matrix.formatList(new_mat_str_list))


    
    def transpose(self):
        """
        returns a matrix object that contains the elements of self transposed
        i.e the rows become columns and columns become rows
        """
        new_row_vecs = []
        for i in range(self.numOfColumns):
            new_row_vecs.append(vector(matrix.FormatColumnVectors(self.ColumnVecs[i])))
        return matrix(matrix.formatList(new_row_vecs))

    def det(self) -> float:
        """
        returns the determinant of self as a float value
        """
        if self.isSquare == False:
            print("Matrix is not square")
            return None
        row_matrix = []
        for i in range(self.numOfRows):
            temp_vec = [float(x) for x in self.RowVecs[i].elems]
            row_matrix.append(temp_vec.copy())
            temp_vec.clear()
        return matrix.rec_det(row_matrix)

    def inv(self): 
        """
        returns a matrix object containing the inv of self
        """
        mat_det = self.det()
        if self.isSquare == False or mat_det == 0:
            print("Matrix is not square or matrix determinant is zero")
            return None
        return self.__inv_and_adjugate__(mat_det)

    def adjugate(self):
        """
        returns a matrix object that is the adjugate of self
        """
        if self.isSquare == False:
            print("Matrix is not square")
            return None
        return self.__inv_and_adjugate__(1.0)

    def __inv_and_adjugate__(self,det: float):
        """
        returns a matrix object that can produce the star matrix
        divided by det
        Parameters
        ----------
        det : float
            what the star matrix is divided by by
        """
        column_matrix = []
        for i in range(self.numOfColumns):
            temp_vec = [float(x) for x in self.ColumnVecs[i].elems]
            column_matrix.append(temp_vec.copy())
            temp_vec.clear()
        star_mat = matrix.star(column_matrix.copy())
        adjugate_mat = []
        temp_vec.clear()
        for row in range(self.numOfColumns):
            adjugate_mat.append(temp_vec[:])
            temp_vec.clear()
            for column in range(self.numOfColumns):
                temp_vec.append(star_mat[row][column]/det)
        adjugate_mat.append(temp_vec[:])
        adjugate_mat = [x for x in adjugate_mat.copy() if x]
        vec_list = []
        for i in range(len(adjugate_mat)):
            vec_list.append(vector(matrix.FormatColumnVectors(adjugate_mat[i])))
        return matrix(matrix.formatList(vec_list))


    @staticmethod
    def rec_det(mat) -> float:
        """
        returns the determinant of a list of lists containing float values
        """
        mat_cpy = mat.copy()
        if len(mat) <= 1:
            return float(re.sub(r'\[|\]',"",str(mat_cpy)))
        else:
            sum = 0
            for row in range(len(mat)):
                sum += pow(-1,row)*mat[row][0]*matrix.rec_det(matrix.not_in_row_or_column(mat_cpy,len(mat_cpy),row,0))
            return sum

    @staticmethod
    def not_in_row_or_column(mat: list,size: int,target_row: int,target_column: int) -> list:
        """
        returns a list of lists containing float values of all the
        values that are not in the position target row and target column
        also called the co-factors of a position
        Parameters
        ----------
        mat : list
            is a list of lists containing float values
        size : int
            is the length of mat
        target_row : int
            the row that element you want to find the co-factors of
        target_column : int
            the column that element you want to find the co-factors of
        """
        temp_vec = []
        new_mat = []
        for row in range(size):
            if row != 0:
                new_mat.append(temp_vec.copy())
                temp_vec.clear()
            for column in range(size):
                if row != target_row and column != target_column:
                    temp_vec.append(mat[row][column])
        new_mat.append(temp_vec)
        new_mat = list([x for x in new_mat.copy() if x])
        return new_mat

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
    
    @staticmethod
    def appendZeroes(vec: list, initialSize: int, maxColumnSize: int) -> list:
        """
        add the difference of maxColumnSize and initialSize of zeroes to vec
        Parameters
        ----------
        vec : list
            the list you wish to add zeroes to
        initialSize : int
            the initial length of vec
        maxColumnSize : int
            the size you wish to compare with initialSize
        """
        while initialSize < maxColumnSize:
            vec.elems.append(0.0)
            vec.size = vec.size + 1
            initialSize = initialSize + 1
        return vec

    @staticmethod
    def formatList(vecList: list) -> list:
        tempStr = "["
        for i in range(len(vecList)):
            if i != len(vecList) - 1:
                tempStr = tempStr + vector.__str__(vecList[i]) + ';'
            else:
                tempStr = tempStr + vector.__str__(vecList[i])
        tempStr += "]"
        return tempStr
    
    @staticmethod
    def star(mat: list) -> list:
        """
        returns a list of lists of floats containing
        the star transformation of mat\n
        **is a helper function**
        Parameters
        ----------
        mat : list
            returns a list of lists of floats containing the row vectors 
            of a square matrix
        """
        temp_vec = []
        adjugate_mat = []
        for row in range(len(mat)):
            adjugate_mat.append(temp_vec[:])
            temp_vec.clear()
            for column in range(len(mat)):
                val = pow(-1,column+row)*matrix.rec_det(matrix.not_in_row_or_column(mat,len(mat),row,column))
                temp_vec.append(val)
        adjugate_mat.append(temp_vec[:])
        temp_vec.clear()
        adjugate_mat = [x for x in adjugate_mat.copy() if x]
        return adjugate_mat

