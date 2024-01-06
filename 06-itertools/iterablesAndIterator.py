from itertools import combinations
# _, n,k=int(input()), input().split(), int(input())
# an=[ a for a in tuple(combinations(n,k)) if 'a' in a]
# print(len(an)/len(n))
n, lst, k = int(input()), input().split(), int(input())
probability = sum('a' in tu for tu in combinations(lst, k)) / len(tuple(combinations(lst, k)))
print("{:.3f}".format(probability))

