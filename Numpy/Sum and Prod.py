import numpy

n, m = map(int, input().split())
num_arr = []

for _ in range(n):
    temp = list(map(int, input().split()))
    num_arr.append(temp)
    
print(numpy.prod(numpy.sum(num_arr, axis=0)))
