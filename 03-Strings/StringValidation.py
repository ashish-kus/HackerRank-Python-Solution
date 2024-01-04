# LINK: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# alphanumaric, alphabatical, digits, lowercase and uppercase

s=input()

alphanumaric=False
alphabatical=False
digits=False
lowercase=False
uppercase=False

for i in s:
    if (i.isalnum()): alphanumaric=True
    if (i.isalpha()): alphabatical=True
    if (i.isdigit()): digits=True
    if (i.islower()): lowercase=True
    if (i.islower()): uppercase=True

print(alphanumaric, alphabatical, digits, lowercase, uppercase, sep="\n")
