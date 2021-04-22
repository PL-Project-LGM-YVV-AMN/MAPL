import lexer as lt
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
        if self.size != RightVec.size:
            print("Vectors are not of equal size")
            return None
        for i in range(self.size):
            result.append(float(self.elems[i])+float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult

    def __sub__(self, RightVec):
        result = []
        if self.size != RightVec.size:
            print("Vectors are not of equal size")
            return None
        for i in range(self.size):
            result.append(float(self.elems[i])-float(RightVec.elems[i]))
        vecResult = vector(vector.FormatColumnVectors(str(result)))
        return vecResult
    
    def __len__(self):
        return self.size

    def scalar_multiplication(self, multiplier):
        multiplied_vec = []
        for i in range(self.size):
            multiplied_vec.append(float(self.elems[i])*multiplier)
        return vector(vector.FormatColumnVectors(str(multiplied_vec)))

    @staticmethod
    def FormatColumnVectors(string):
        result = re.sub(r'\'', '', str(string))
        result = re.sub(",","", str(result))
        return result

    def dot_product(self, rightVec):
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


