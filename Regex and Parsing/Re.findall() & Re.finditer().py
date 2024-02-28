import re

a = input()

a = re.findall('[aeiouAEIOU]{2,}[^aeiouAEIOU]{1}', a)
if a:
    print(*[i[:-1] for i in a], sep = "\n")
else:
    print("-1")
