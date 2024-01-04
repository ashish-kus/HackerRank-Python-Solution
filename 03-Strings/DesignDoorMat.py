n,m=map(int, input().split())
fill="---"
design=".|."
for i in range(n//2):
    print("---"*(n//2 - i)+ '.|.'*(i*2+1) + "---"*(n//2 - i))
print("-"*((m-7)//2)+"WELCOME"+"-"*((m-7)//2))
for i in range((n//2) -1, -1, -1):
    print("---"*(n//2 - i)+ '.|.'*(i*2+1) + "---"*(n//2 - i))

