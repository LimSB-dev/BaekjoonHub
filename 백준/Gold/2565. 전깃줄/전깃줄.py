n = int(input())

lines = [list(map(int, input().split())) for _ in range(n)]

lines.sort(key=lambda x: x[0])

b_line = [b for a, b in lines]

dp = [1] * n

for i in range(n):
    for j in range(i):
        if b_line[i] > b_line[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))