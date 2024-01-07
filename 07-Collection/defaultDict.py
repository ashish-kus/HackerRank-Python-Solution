from collections import defaultdict

N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

d = defaultdict(list)

for index, item in enumerate(A, start=1):
    d[item].append(index)

for item in B:
    print(*d.get(item, [-1]))
