import numpy

n, m, p = map(int, input().split())
arrs = []

for _ in range(n+m):
    temp = list(map(int, input().split()))
    arrs.append(temp)
    
print(numpy.array(arrs))
