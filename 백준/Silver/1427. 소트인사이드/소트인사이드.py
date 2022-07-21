import sys
input = sys.stdin.readline
c = 1
N = int(input())
n = N
while True:
  if 10 <= n:
    n = n // 10
    c += 1
  else:
    break
li =[]
for _ in range(c):
  li.append(N % 10)
  N = N//10
LI = sorted(li,reverse=True)
for i in range(len(LI)):
  print(LI[i],end='')