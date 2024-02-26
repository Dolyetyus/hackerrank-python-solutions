from itertools import combinations_with_replacement

string, num = input().rsplit(maxsplit=1)
num = int(num)
string = sorted(string)

a = list(combinations_with_replacement(string, num))
a.sort()

for char in a:
    print(''.join(char))
