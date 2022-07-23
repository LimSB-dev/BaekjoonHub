t = int(input())

for _ in range(t):
  a,b = map(int,input().split())
  A,B=a,b
  while b != 0:
    r = a % b
    a = b
    b = r
  print((A * B)//a)