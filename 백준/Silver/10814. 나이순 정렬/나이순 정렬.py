import sys

input = sys.stdin.readline

n = int(input())
li =[]

for i in range(n):
  age,name = input().split()
  li.append([int(age),name])

li.sort(key = lambda x: x[0])

for i in range(n):
  print(li[i][0],li[i][1])