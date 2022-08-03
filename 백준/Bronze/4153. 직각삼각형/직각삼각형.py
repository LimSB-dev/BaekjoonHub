import sys

while True:

  a,b,c=map(int,sys.stdin.readline().split())

  A = a**2
  B = b**2
  C = c**2

  N = [A,B,C]

  N = sorted(N)

  if a + b + c == 0:
    break
  
  elif N[0] + N[1] == N[2]:

    print('right')
  
  else:

    print('wrong')