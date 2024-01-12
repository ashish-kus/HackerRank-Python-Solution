import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

# Input the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    pattern = input()
    print(is_valid_regex(pattern))
