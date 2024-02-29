import numpy

x, y, *a = map(int, input().split())

print(numpy.zeros((x, y, *a), dtype = numpy.int))
print(numpy.ones((x, y, *a), dtype = numpy.int))
