t=int(input())
for i in range(t):

    _=int(input())
    A=set(list(map(int, input().split())))

    _=int(input())
    B=set(list(map(int, input().split())))

    if A.union(B)==B:
        print("True")
    else:
        print("False")

