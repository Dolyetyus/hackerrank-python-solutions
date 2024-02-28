import re

a = input()

res = re.search(r"([a-zA-Z0-9])\1", a)

if res:
    print(res.group(1))
else:
    print("-1")
