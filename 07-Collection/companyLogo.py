from collections import Counter
[print(*x) for x in Counter(sorted(list(input()))).most_common(3)]
