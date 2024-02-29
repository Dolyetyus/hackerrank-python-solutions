import numpy

def arrays(arr):
    arr = numpy.flip(arr)
    return numpy.array(arr, float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
