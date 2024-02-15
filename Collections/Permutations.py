from itertools import permutations

string, chars = map(str, input().split())
chars = int(chars)

list = permutations(string, chars)

for i in sorted(list):
    print("".join(i))
