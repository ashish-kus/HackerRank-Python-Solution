import numpy

def arrays(arr):  
    narray=numpy.array(arr, float)
    return numpy.flip(narray)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
