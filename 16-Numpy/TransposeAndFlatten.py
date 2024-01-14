# import numpy
# N,M = map(int,input().split())
# lst=[]
# for _ in range(N):
#     lst.append([int(x) for x in input().split()])
# arr = numpy.array(lst)
# print(numpy.transpose(arr))
# print(arr.flatten())
import numpy as np

N, M = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.transpose(arr))
print(arr.flatten())

