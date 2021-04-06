import lexer_test as lt
from vectorClass import vector
import re
import math
class matrix:
    
    VectorRule = re.compile(lt.t_vector)

    def __init__(self, string):
        ColumnVecsFromRE = matrix.VectorRule.findall(string)
        self.numOfColumns = len(ColumnVecsFromRE)
        self.ColumnVecs = []
        sizeOfVecs = []
        for i in range(self.numOfColumns):
            self.ColumnVecs.append(vector(matrix.FormatColumnVectors(ColumnVecsFromRE[i])))
            sizeOfVecs.append(len(self.ColumnVecs[i]))
        maxColumnSize = max(sizeOfVecs)
        for j in range(self.numOfColumns):
            self.ColumnVecs[j] =  matrix.appendZeroes(self.ColumnVecs[j],self.ColumnVecs[j].size,maxColumnSize)
        RowVecs = []
        temp_list = []
        for k in range(maxColumnSize):
            if k != 0:
                RowVecs.append(temp_list)
                del temp_list
                temp_list = []
            for z in range(self.numOfColumns):
                temp_list.append(self.ColumnVecs[z].elems[k])
        RowVecs.append(temp_list)
        del temp_list
        self.size = maxColumnSize*self.numOfColumns
        self.numOfRows = len(RowVecs)
        self.RowVecs = []
        for i in range(self.numOfRows):
            self.RowVecs.append(vector(matrix.FormatColumnVectors(RowVecs[i])))
        self.isSquare = False
        if math.sqrt(self.size) == math.floor(math.sqrt(self.size)):
            self.isSquare = True

    def __str__(self):
        ans = ""
        for i in range(self.numOfRows):
           ans = ans + vector.__str__(self.RowVecs[i]) + '\n'
        return ans

    def __add__(self,RightMatrix):
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfColumns):
            vecList.append(self.ColumnVecs[vecs] + RightMatrix.ColumnVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def __sub__(self,RightMatrix):
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfColumns):
            vecList.append(self.ColumnVecs[vecs] - RightMatrix.ColumnVecs[vecs])
        return matrix(matrix.formatList(vecList))

    def scalar_multiplication(self, multiplier):
        vecList = []
        for i in range(self.numOfColumns):
            vecList.append(self.ColumnVecs[i].scalar_multiplication(multiplier))
        return matrix(matrix.formatList(vecList))
    
    def cross_product(self, rightMat):
        if self.numOfColumns != rightMat.numOfRows:
            print("Left matrix's number of columns not equal to right matrix's number of rows")
            return None
        new_column_vecs = []
        temp_list = []
        for i in range(rightMat.numOfColumns):
            if i != 0:
                new_column_vecs.append(temp_list)
                del temp_list
                temp_list = []
            for j in range(self.numOfRows):
                temp_list.append(self.RowVecs[j].dot_product(rightMat.ColumnVecs[i]))
        new_column_vecs.append(temp_list)
        del temp_list
        new_mat_str_list = []
        for k in range(len(new_column_vecs)):
            new_mat_str_list.append(vector(vector.FormatColumnVectors(new_column_vecs[k])))
        return matrix(matrix.formatList(new_mat_str_list))
    
    def transpose(self):
        new_column_vecs = []
        for i in range(self.numOfRows):
            new_column_vecs.append(vector(matrix.FormatColumnVectors(self.RowVecs[i])))
        return matrix(matrix.formatList(new_column_vecs))

    def det(self):
        if self.isSquare == False:
            print("Matrix is not square")
            return None
        row_matrix = []
        for i in range(self.numOfRows):
            temp_vec = [int(x) for x in self.RowVecs[i].elems]
            row_matrix.append(temp_vec.copy())
            temp_vec.clear()
        return matrix.rec_det(row_matrix)

    @staticmethod
    def rec_det(mat):
        mat_cpy = mat.copy()
        if len(mat) <= 1:
            return float(re.sub(r'\[|\]',"",str(mat_cpy)))
        else:
            sum = 0
            for row in range(len(mat)):
                sum += pow(-1,row)*mat[row][0]*matrix.rec_det(matrix.not_in_row_or_column(mat_cpy,len(mat_cpy),row,0))
            return sum

    @staticmethod
    def not_in_row_or_column(mat,size,target_row,target_column):
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
    def FormatColumnVectors(string):
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result
    
    @staticmethod
    def appendZeroes(vec,initialSize ,maxColumnSize):
        while initialSize < maxColumnSize:
            vec.elems.append(0.0)
            vec.size = vec.size + 1
            initialSize = initialSize + 1
        return vec

    @staticmethod
    def formatList(vecList):
        tempStr = "["
        for i in range(len(vecList)):
            if i != len(vecList) - 1:
                tempStr = tempStr + vector.__str__(vecList[i]) + ';'
            else:
                tempStr = tempStr + vector.__str__(vecList[i])
        tempStr += "]"
        return tempStr


