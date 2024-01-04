eng=int(input())
eng_roll=set(list(map(int,input().split())))

fre=int(input())
fre_roll=set(list(map(int,input().split())))

print(len(eng_roll.union(fre_roll)))



