import numpy as np
A = np.array(input().split(), dtype='int')
B = np.array(input().split(), dtype='int')
print(np.inner(A, B), np.outer(A, B), sep='\n')
