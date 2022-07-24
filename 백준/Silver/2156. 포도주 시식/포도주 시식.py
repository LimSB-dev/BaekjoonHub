t = int(input())
li = [int(input()) for _ in range(t)]

wine = [0,0,0] + li

dp = [0] * (t+3)

for i in range(3,t+3):
  dp[i] = max(dp[i-1],dp[i-2] + wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[-1])