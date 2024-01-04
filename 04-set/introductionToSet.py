def avg(numbers):
    return round(sum(set(numbers))/len(set(numbers)), 3)

numbers=int(input())
numbers=list(map(int,input().split()))
result=avg(numbers)
print(result)
