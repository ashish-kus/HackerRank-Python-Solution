# Link: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# note: leap year is divisible by 4 and 100 as well or it is divisible by 400.

year= int(input())

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return leap



print(is_leap(year))

