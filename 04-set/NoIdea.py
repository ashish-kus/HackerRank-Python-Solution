# n integer
# A , B  =  m

n , m = input().split()
arr=list(map(int, input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))

value =0 
for i in arr:
    if i in a:
        value= value+1
    elif i in b:
        value = value-1
    else:
        pass

print(value)

