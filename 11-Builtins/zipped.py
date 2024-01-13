n,x=list(map(int, input().split()))
[print(sum(i)/len(i)) for i in list(zip(*[list(map(float, input().split())) for _ in range(x)]))]
 
