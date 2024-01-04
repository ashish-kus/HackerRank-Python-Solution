A=set(list(map(int, input().split())))
result=True
for i in range(int(input())):
    arr=set(list(map(int, input().split())))
    if not A.issuperset(arr) or A == arr:
        result=False
    print(result)

