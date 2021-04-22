import lexer
import grammar
import re

with open("test_file.txt", 'r') as f:
    for line in f:
        temp = re.sub(r'\n',"", line)
        result = grammar.parser.parse(temp)
        print(result)