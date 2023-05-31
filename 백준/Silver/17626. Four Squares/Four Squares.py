import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = i
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j*j]+1)

print(dp[n])
