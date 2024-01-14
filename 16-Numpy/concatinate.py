import numpy as np

N, M, P = map(int, input().split())
data_N = [input().split() for _ in range(N)]
int_data_N = [list(map(int, row)) for row in data_N]

data_M = [input().split() for _ in range(M)]
int_data_M = [list(map(int, row)) for row in data_M]

arr_N, arr_M = np.array(int_data_N), np.array(int_data_M)
result = np.concatenate((arr_N, arr_M), axis=0)
print(result)

