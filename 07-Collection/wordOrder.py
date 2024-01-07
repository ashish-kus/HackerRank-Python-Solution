from collections import Counter
n = int(input())
lst = [input() for _ in range(n)]
c = Counter(lst)

print(len(c.values()))
print(*c.values())

# print(*c.values()): This line prints all the values of the dictionary c
# separated by spaces. The * symbol is used for unpacking the values of the 
# dictionary and passing them as individual arguments to the print function.
