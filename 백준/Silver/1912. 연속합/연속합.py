n = int(input())
li = list(map(int,input().split()))
dp = li
for i in range(1,n):
    dp[i] = max(dp[i], dp[i-1] + li[i])

print(max(dp))