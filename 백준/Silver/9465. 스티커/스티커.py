import sys
input = sys.stdin.readline

t = int(input())
anw = []

for i in range(t):
  n = int(input())
  li = []

  for _ in range(2):
    li.append(list(map(int,input().split())))

  for j in range(1,n):
    if j == 1:
      li[0][j] += li[1][j-1]
      li[1][j] += li[0][j-1]
    else:
      li[0][j] += max(li[1][j-1],li[1][j-2])
      li[1][j] += max(li[0][j-1],li[0][j-2])

  anw.append(max(li[0][n-1],li[1][n-1]))

for i in range(t):
  print(anw[i])