n = int(input())
dp = []

for _ in range(n):
  r,g,b = map(int,input().split())
  dp.append([r,g,b])

table = [[0 for _ in range(3)] for _ in range(n)]

for i in range(n):
  for j in range(3):
    if i == 0:
      table[i][j] = dp[i][j]
    else:
      table[i][j] = min(table[i-1][(j+1)%3], table[i-1][(j+2)%3]) + dp[i][j]

print(min(table[-1]))
  