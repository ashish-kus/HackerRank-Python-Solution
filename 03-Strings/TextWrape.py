strint=input()
result=""
for i in range(len(strint)):
    if(i==0):
        result=result  + strint[i]
    elif((i) % 4 == 0):
        result=result + '\n' + strint[i]
    else:
        result=result  + strint[i]
print(result)

