import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = [int(input()) for _ in range(n)]
coin_list.sort(reverse=True)
dp = [0] * (k+1)
dp[0] = 1

for coin in coin_list:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

answer = dp[k]

print(answer)
