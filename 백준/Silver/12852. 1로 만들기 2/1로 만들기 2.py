import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1) # 횟수의 최솟값
path = [0] * (n + 1) # 최소 경로
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    path[i] = i - 1
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        path[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        path[i] = i // 3
print(dp[n])

answer = [n]
while True:
    if n == 1:
        break
    answer.append(path[n])
    n = path[n]

print(*answer)
