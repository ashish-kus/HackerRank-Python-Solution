import numpy as np
n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], dtype='int')
print(np.mean(A, axis=1), np.var(A, axis=0), round(np.std(A, axis=None), 11), sep='\n')
