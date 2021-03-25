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

class matrix:
    
    VectorRule = re.compile(lt.t_vector)

    def __init__(self, string):
        ColumnVecsFromRE = matrix.VectorRule.findall(string)
        self.ColumnSize = len(ColumnVecsFromRE)
        self.ColumnVecs = []
        for i in range(self.ColumnSize):
            self.ColumnVecs.append(vector(matrix.FormatColumnVectors(ColumnVecsFromRE[i])))

    

    @staticmethod
    def FormatColumnVectors(string):
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result




x = "[[1.0 2.0 3];[1 2 3];[3 4 5]]"

y = matrix(x)

for i  in range(y.ColumnSize):
    print(y.ColumnVecs[i])

