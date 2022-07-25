import sys
A,B,C=map(int,sys.stdin.readline().split())
D=int(input())
C=C+D
while C>59:
  B+=1
  C-=60
  while B>59:
    A+=1
    B-=60
    if A>23:
      A-=24
print(A,B,C)