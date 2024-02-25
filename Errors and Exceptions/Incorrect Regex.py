import re

n = int(input())

for _ in range(n):
    ret = True
    try:
        re.compile(input())
    except re.error:
        ret = False
        
    print(ret)
