from itertools import combinations
S,k=input().split()
S=sorted(S)
li=[]
for i in range(1, int(k)+1):
    li.extend(list(combinations(S,i)))
for i in li:
    print("".join(i))
