input_string = input()
temp = [[], [], [], []]
[ temp[0].append(c) if 'a' <= c <= 'z' else temp[1].append(c) if 'A' <= c <= 'Z' else temp[2 + int(int(c) % 2 == 0)].append(c) for c in input_string ]
result = "".join(["".join(sorted(row)) for row in temp])
print(result)

