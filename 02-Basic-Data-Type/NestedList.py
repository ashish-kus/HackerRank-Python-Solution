# LINK: https://www.hackerrank.com/challenges/nested-list/problem
import sys
n=int(input())
student=[]
finalStudent=[]
for i in range(n):
    temp=[]
    name=input()
    score=float(input())
    temp.append(name)
    temp.append(score)
    student.append(temp)
student.sort()
minFirst=sys.maxsize - 1
minSecond=sys.maxsize 

for i in student:
    if (i[1] < minFirst):
        minSecond=minFirst
        minFirst=i[1]
for i in student:
    if (i[1] == minSecond):
        finalStudent.append(i)
finalStudent.sort()
for i in finalStudent:
    print(i[0])

