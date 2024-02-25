from itertools import combinations

string, num = input().rsplit(maxsplit=1)
num = int(num)
string = sorted(string)

for i in range(num):
    a = list(combinations(string, i+1))
    a.sort()
    for char in a:
        print(''.join(char))
