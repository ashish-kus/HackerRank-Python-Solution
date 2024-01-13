import re

def fun(s):
    # Define the regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'
    
    # Return True if the string matches the pattern, else return False
    return re.match(pattern, s) is not None

def filter_mail(emails):
    # Use the provided function 'fun' with the 'filter' function
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input("Enter the number of email addresses: "))
    emails = []
    for _ in range(n):
        emails.append(input())

    # Call the filter_mail function to get a list of valid email addresses
    filtered_emails = filter_mail(emails)

    # Sort the valid email addresses in lexicographical order
    filtered_emails.sort()

    # Print the list of valid email addresses
    print(filtered_emails)
