import re
n = int(input())

for _ in range(n):
    name, mail = map(str, input().split())
    
    res = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', mail)
    if res:
        print(name, mail)
