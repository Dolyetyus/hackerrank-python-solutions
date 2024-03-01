import numpy

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
a = numpy.min(arr, axis=1)
print(numpy.max(a))
