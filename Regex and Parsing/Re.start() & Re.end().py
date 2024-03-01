import re

string = input()
s = input()

match = list(re.finditer(r'(?={})'.format(s), string))

if match:
    res = [(val.start(), val.start()+len(s)-1) for val in match]
    print(*res, sep="\n")
else:
    print('(-1, -1)')
