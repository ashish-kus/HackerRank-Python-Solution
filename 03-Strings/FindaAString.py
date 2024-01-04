def count_substring(string, sub_string):
    c = 0
    for i in range(len(string)):
        subs = string[i:]
        if sub_string in subs:
            idx = subs.index(sub_string)
            if idx == 0:
                c += 1
    return c

# Sample Input
string_input = str(input())
substring_input = str(input())

# Call the function with the sample input
result = count_substring(string_input, substring_input)

# Print the result
print(result)
 
