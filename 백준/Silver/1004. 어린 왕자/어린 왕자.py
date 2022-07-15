import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  x1,y1,x2,y2=map(int,input().split())
  n = int(input())
  c = 0

  for _ in range(n):
    x3,y3,r=map(int,input().split())
    X1 = (x1 - x3)**2
    Y1 = (y1 - y3)**2
    X2 = (x2 - x3)**2
    Y2 = (y2 - y3)**2
    R = r**2

    if X1 + Y1 < R:
      c += 1
      if X2 + Y2 < R:
        c -= 1

    elif X2 + Y2 < R:
      c += 1
      if X1 + Y1 < R:
        c -= 1

  print(c)