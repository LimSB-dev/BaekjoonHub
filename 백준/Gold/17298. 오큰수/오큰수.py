import sys
input = sys.stdin.readline

a = int(input())
li = list(map(int,input().split()))
stack = []
anw = [-1] * a

for i in range(a):
  try:
    while (li[stack[-1]] < li[i]):
      anw[stack.pop()] = li[i]
  except:
    pass

  stack.append(i)

for i in anw:
  print(i,end=' ')
