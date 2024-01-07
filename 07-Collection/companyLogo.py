from collections import Counter
s = sorted(list(input()))
for x, y in Counter(s).most_common(3):
    print(x, y)
