import sys
input = sys.stdin.readline
# print = sys.stdout.write

t = int(input())
for i in range(t):
  n = int(input())
  clothes = {}
  anw = 1
  for j in range(n):
    cloth = list(map(str,input().split()))
    if cloth[1] in clothes:
      clothes[cloth[1]] += 1
    else:
      clothes[cloth[1]] = 1
  li = clothes.values()
  for i in li:
    anw *= i+1
  print(anw-1)