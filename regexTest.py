import lexer_test as lt
import re

class vector:
    isvector = re.compile(lt.t_vector)
    elemsRule = re.compile(lt.t_float + r'|' + lt.t_int)
    def __init__(self,string):
        if vector.isvector.search(string) != None:
            self.elems = vector.elemsRule.findall(string)
            self.size = len(self.elems)


x = vector("[10.00 20 30.00 40.11 5.22]")

print(x.elems)