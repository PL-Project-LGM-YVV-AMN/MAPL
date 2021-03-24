import lexer_test as lt
import re

class vector:
    elemsRule = re.compile(r'-*'+(lt.t_float + r'|' + lt.t_int))
    def __init__(self,string):
        self.elems = vector.elemsRule.findall(string)
        self.size = len(self.elems)
    
    def __str__(self):
        return re.sub("'", '', str(self.elems))
    
