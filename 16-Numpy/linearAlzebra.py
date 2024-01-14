from numpy.linalg import det
print(round(det([list(map(float, input().split())) for i in range(int(input()))]), 2))
