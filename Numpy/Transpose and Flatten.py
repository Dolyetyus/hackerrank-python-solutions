import numpy

n, m = map(int, input().split())
arrs = []

for _ in range(n):
    arr = list(map(int, input().split()))
    arrs.append(arr)
    
num_arr = numpy.array(arrs)
print(numpy.transpose(num_arr))
print(num_arr.flatten())
