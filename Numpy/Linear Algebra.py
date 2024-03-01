import numpy

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(float, input().split())))
    
print(round(numpy.linalg.det(a), 2))
