import sys
input = sys.stdin.readline

n = int(input())
MOD = 1000000000
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        dp[i] = (dp[i - 1] + dp[i // 2]) % MOD
    else:
        dp[i] = dp[i - 1]
print(dp[n])
