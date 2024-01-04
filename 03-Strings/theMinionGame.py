s=input()
vowels=[ "a", "e", "i", "o", "u" ]

stuart=0
kevin=0
i=0
for a in s:
    if a.isalpha():
        if a.lower() in vowels: 
            kevin=kevin+len(s)-i
            print(a, kevin,stuart)
        else:
            stuart=stuart+len(s)-i
            print(a, kevin,stuart)
    i=i+1
if stuart > kevin :
    print(f'Stuart {stuart}')
elif stuart == kevin:
    print("Draw")
else:
    print(f'Kevin {kevin}')


