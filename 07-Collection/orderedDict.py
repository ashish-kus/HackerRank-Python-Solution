# # Regular Dictionary (Python 3.7 and later)
# regular_dict = {'apple': 3, 'banana': 1, 'orange': 2}
# print("Regular Dictionary:", regular_dict)

# # OrderedDict
# from collections import OrderedDict
# ordered_dict = OrderedDict([('apple', 3), ('banana', 1), ('orange', 2)])
# print("OrderedDict:", ordered_dict)

# # Iterating over both to demonstrate order
# print("\nIterating over Regular Dictionary:")
# for key, value in regular_dict.items():
#     print(key, value)

# print("\nIterating over OrderedDict:")
# for key, value in ordered_dict.items():
#     print(key, value)

from collections import defaultdict
n, d = int(input()), defaultdict(int)
[d.update({i: d[i]+int(j)}) for i, j in [input().rsplit(maxsplit=1) for _ in range(n)]]
[print(i, j) for i, j in d.items()]

