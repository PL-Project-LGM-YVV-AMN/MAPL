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
        return result

    def __sub__(self, RightVec):
        result = []
        for i in range(self.size):
            result.append(float(self.elems[i])-float(RightVec.elems[i]))
        return result
    
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
            self.ColumnVecs[i] =  matrix.appendZeroes(self.ColumnVecs[j],self.ColumnVecs[j].size,maxColumnSize)
        self.RowVecs = []
        temp_list = []
        for k in range(self.numOfColumns):
            if k != 0:
                self.RowVecs.append(temp_list)
                temp_list.clear()
            for z in range(maxColumnSize):
                temp_list.append(self.ColumnVecs[z].elems[k])


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
        




x = "[[1.0 2.0 3];[1 2];[3 4]]"

y = matrix(x)

print(y.RowVecs)

