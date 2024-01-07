a = int(input())
b = input().split()
c = [input().split() for _ in range(a)]
print(sum(int(c[n][b.index("MARKS")])for n in range(len(c)))/len(c))

