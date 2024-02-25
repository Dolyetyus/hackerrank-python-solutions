from collections import defaultdict

sizeA, sizeB = map(int, input().split())

d = defaultdict(list)

for _ in range(sizeA):
    d['A'].append(input())

for _ in range(sizeB):
    d['B'].append(input())
    
for char in d['B']:
    idx=[i+1 for i, x in enumerate(d['A']) if x == char]
    if idx:
        print(*idx)
    else:
        print(-1)
