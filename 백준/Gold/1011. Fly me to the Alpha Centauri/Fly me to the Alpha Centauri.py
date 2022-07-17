import sys
from math import sqrt

t = int(sys.stdin.readline().strip())

for i in range(t):

  x, y = map(int,sys.stdin.readline().split())
  l = y - x
  temp = round(sqrt(l))
  num = temp * 2 - 1

  if temp ** 2 < l:

    print(num + 1)
  
  else:

    print(num)