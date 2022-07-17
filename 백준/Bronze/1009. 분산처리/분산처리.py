import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
  a, b = map(int,sys.stdin.readline().split())
  a = a % 10
  b = b % 4
  if b == 0:
    b = 4
  anw = (a**b) % 10
  if anw == 0:
      print(10)
  else:
  	print(anw)