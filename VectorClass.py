import lexer_test as lt
import re


class vector:
    elemsRule = re.compile((r'-?' + lt.t_float + r'|-?' + lt.t_int))

    def __init__(self, string):
        self.elems = vector.elemsRule.findall(string)
        self.size = len(self.elems)

    def __str__(self):
        result = re.sub(r'\'', '', str(self.elems))
        result = re.sub(",","", str(result))
        return result

    def __add__(self, RightVec):
        result = []
        for i in range(self.size):
            result.append(float(self.elems[i])+float(RightVec.elems[i]))
        vecResult = vector(matrix.FormatColumnVectors(str(result)))
        return vecResult

    def __sub__(self, RightVec):
        result = []
        for i in range(self.size):
            result.append(float(self.elems[i])-float(RightVec.elems[i]))
        vecResult = vector(matrix.FormatColumnVectors(str(result)))
        return vecResult
    
    def __len__(self):
        return self.size


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
        tempStr = "["
        i = 0
        for i in range(len(vecList)):
            if i != len(vecList) - 1:
                tempStr = tempStr + vector.__str__(vecList[i]) + ';'
            else:
                tempStr = tempStr + vector.__str__(vecList[i])
        tempStr += "]"
        return matrix(tempStr)

    def __sub__(self,RightMatrix):
        if self.numOfColumns != RightMatrix.numOfColumns and self.numOfRows != RightMatrix.numOfRows:
            return None
        vecList = []
        for vecs in range(self.numOfColumns):
            vecList.append(self.ColumnVecs[vecs] - RightMatrix.ColumnVecs[vecs])
        tempStr = "["
        i = 0
        for i in range(len(vecList)):
            if i != len(vecList) - 1:
                tempStr = tempStr + vector.__str__(vecList[i]) + ';'
            else:
                tempStr = tempStr + vector.__str__(vecList[i])
        tempStr += "]"
        return matrix(tempStr)


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
        




y = matrix("[[1.0 2.0 3];[1 2]]")

z = matrix("[[2 3 4];[5 6]]")

b = y-z

print(b)