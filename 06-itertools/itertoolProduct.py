from itertools import product
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
cartesian_product = list(product(list_a, list_b))
for item in cartesian_product:
    print(item, end=' ')
