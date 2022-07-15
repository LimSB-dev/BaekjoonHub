t = int(input())

for i in range(t):
  x1,y1,r1,x2,y2,r2=map(int,input().split())

  X = abs(x1-x2)
  Y = abs(y1-y2)
  R1 = abs(r1+r2)
  R2 = abs(r1-r2)

  if X == 0 and Y == 0 and r1 == r2:

    print(-1)

  elif (X**2)+(Y**2) == (R1**2)or(X**2)+(Y**2) == (R2**2):

    print(1)

  elif (X**2)+(Y**2)<(R1**2)and(X**2)+(Y**2)>(R2**2):

    print(2)

  else:

    print(0)