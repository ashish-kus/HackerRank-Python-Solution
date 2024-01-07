from collections import Counter
x=int(input())
xs = Counter(list(map(int, input().split())))
n=int(input())
xk=list(xs.keys())
sell=0
for i in range(n):
    k,v=map(int,input().split())
    if xs[k]>=1:
        sell=sell+v
        xs[k]=xs[k]-1
print(sell)

