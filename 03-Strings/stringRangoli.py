
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in indices:
start_index = i+1
original = alphabet[-start_index:]
reverse = original[::-1]
row = reverse + original[1:]
row = '-'.join(row)
width = size*4-3
row = row.center(width,'-')
print(row)     
