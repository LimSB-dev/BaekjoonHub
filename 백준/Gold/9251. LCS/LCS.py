import sys
input = sys.stdin.readline

words = []

for _ in range(2):
  words.append(input().strip())

a = len(words[0])
b = len(words[1])

dp = [[0]*(b+1) for _ in range(a+1)]

for i in range(1,a+1):
  for j in range(1,b+1):
    if words[0][i-1] == words[1][j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[a][b])