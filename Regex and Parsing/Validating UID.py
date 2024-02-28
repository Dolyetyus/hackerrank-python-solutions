import re

n = int(input())

for _ in range(n):
    a = input()
    if (bool(re.match(r'^(?=(?:[^A-Z]*[A-Z]){2})(?=(?:\D*\d){3})(?!.*(.).*\1)[A-Za-z0-9]{10}$', a))):
        print("Valid")
    else:
        print("Invalid")
