t = int(input())

for _ in range(t):

  n = int(input())
  dp = [1 for _ in range(101)]
  for i in range(4,n+1):
   dp[i] = dp[i-2] + dp[i-3]

  print(dp[n])