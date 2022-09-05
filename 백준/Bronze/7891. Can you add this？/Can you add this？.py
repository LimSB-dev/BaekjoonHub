import sys
t = int(input())

for _ in range(t):
  a,b = map(float,sys.stdin.readline().split())
  print(int(a+b))