from itertools import permutations
a, b = input().split()
b = int(b)
for result in sorted(permutations(a, b)):
    print("".join(result))
