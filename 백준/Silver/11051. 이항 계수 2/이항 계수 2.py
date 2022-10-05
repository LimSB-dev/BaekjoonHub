import sys
input = sys.stdin.readline
n,k = map(int,input().split())
anw = 1
if k == 0:
  print(1)
  exit(0)
for i in range(1,k+1):
  anw *= n
  n -= 1
for i in range(1,k+1):
  anw //= k
  k -= 1
print(anw%10007)