 # n odd == weird
 # n even  { 2 - 5 } == not wierd
 # n even { 6 - 20 } == weird 
 # n even > 20 == Weird

n=int(input()) 
if (n% 2==0):
    if (n>=2 and n<=4):
        print("Not Weird")
    elif (n>=6 and n<=20):
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("Weird")
