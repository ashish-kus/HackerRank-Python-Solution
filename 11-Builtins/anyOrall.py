# _, arr = int(input()), all(int(x) > 0 and str(x) == str(x)[::-1] for x in input().split())
# _, arr = int(input()), all(int(x) > 0 for x in input().split()) and any(str(x) == str(x)[::-1] for x in input().split())
# two failed attempts but lot to learn /
_, arr = input(), input().split()
print(all(int(x) > 0 for x in arr) and any(x == x[::-1] for x in arr))


