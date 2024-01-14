import numpy as np
n, m = map(int, input().split())
A = np.array([input().split() for _ in range(n)], dtype='int')
print(np.max(np.min(A, axis=1), axis=None))
