import sys

a,b=map(int,sys.stdin.readline().split())
A = max(a,b)
B = min(a,b)
if B < A:
  print(A-B-1)

else:

 print(0)

while True:
  if B + 1 < A:
    B += 1
    print(B,end=' ')
  else:
    break