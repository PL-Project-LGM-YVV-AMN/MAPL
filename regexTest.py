import lexer_test as lt
import re

class vector:
    elemsRule = re.compile(lt.t_float + r'|' + lt.t_int)
    def __init__(self,string):
        self.elems = vector.elemsRule.findall(string)
        self.size = len(self.elems)
    
    def __str__(self):
        return re.sub("'", '', str(self.elems))

"""
x = vector("[10.00 20 30.00 40.11 5.22]")
y = vector("[10.00 20 30.00 40.11 5.22]")
z = []

for i in range(x.size):
    z.append(float(x.elems[i]) + float(y.elems[i]))

new_vec = vector(re.sub("'", " ", str(z)))

print(new_vec.elems)
"""

