# s,k=input().split()
# print(s)
s=input()
k=int(input())
for i in range(0, len(s), k):
    subStringList=list(dict.fromkeys(list(s[i:i+k])))
    print("".join(subStringList))
#     
# for i in range(0,len(s)//k,3):
#     subString=s[i:i+k]
#     print(subString)
# #     
# for i in range(0, len(s), 3):
#     print(s[i])
