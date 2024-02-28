import re

n = int(input())

for _ in range(n):
    a = input()
    print(bool(re.match(r'^[-+]?([1-9][0-9]*\.?[0-9]*|0?\.[0-9]+)$', a)))
