import numpy

n = int(input())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
    
for _ in range(n):
    b.append(list(map(int, input().split())))
    
print(numpy.dot(a, b))
