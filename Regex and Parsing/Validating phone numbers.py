import re

n = int(input())

for _ in range(n):
    a = input()
    if(bool(re.match(r'^[789][0-9]{9}$', a))):
        print("YES")
    else:
        print("NO")
