# import math
# import os
# import random
# import re
# import sys



if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input()) 
    arr=sorted(arr, key=lambda x: x[k])
    [print(*x) for x in arr]

