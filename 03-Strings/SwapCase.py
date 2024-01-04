  
string=str(input())
final=""
for i in string:
        if (i.isupper()):
            final = final + i.lower()
        else: 
            final = final + i.upper()
print(final)

        


    
