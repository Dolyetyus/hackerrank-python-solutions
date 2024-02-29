import numpy

arr = list(map(int, input().split()))

num_arr = numpy.array(arr)

print(numpy.reshape(num_arr, (3, 3)))
