# Initialize an empty list
n = []

# Get the number of commands to be executed
for i in range(int(input())):
    
    # Get a command as space-separated input and split it into a list
    command = list(input().split())
    
    # Extract the action and arguments from the command
    action = command[0]
    arguments = command[1:]   

    # Check if the action is "print"
    if action == "print":
        # If the action is "print", display the current state of the list
        print(n)
    else:
        # If the action is not "print", dynamically call the method on the list using getattr
        # Convert arguments to integers using map and unpack them using *args
        getattr(n, action)(*map(int, arguments))
    # print(arguments)



# n=[]
# for i in range(int(input())):
#     command=list(input().split())
#     action=command[0]
#     arguments=command[1:]   
#     if action=="print":
#         print(n)
#     else:
#         getattr(n, action)(*map(int,arguments))
