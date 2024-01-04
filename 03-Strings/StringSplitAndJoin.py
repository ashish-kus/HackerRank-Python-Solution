def split_and_join(line):
    result=""
    li=line.split(" ")
    for i in li:
        result=result + i + "-"
    return result

line = input()
result = split_and_join(line)
print(result[:-1])
