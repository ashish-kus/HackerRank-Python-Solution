from itertools import groupby
data = list(input())
grouped_data = [(key, list(group)) for key, group in groupby(data)]
grouped = [(len(group), int(key)) for key, group in grouped_data]
# print(grouped_data)
print(*grouped)
