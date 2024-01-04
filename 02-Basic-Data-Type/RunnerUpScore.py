# LINK: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

n = int(input())
arr = map(int, input().split())

max_first=0
max_runner=0
score=list(set(arr))
score.remove(max(score))
print(max(score))


