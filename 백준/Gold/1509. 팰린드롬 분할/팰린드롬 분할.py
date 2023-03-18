import sys
# sys.stdin = open('input.txt')

s = sys.stdin.readline().strip()
n = len(s)

dp = [[False] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = True

for i in range(n - 1):
    if s[i] == s[i + 1]:
        dp[i][i + 1] = True

for k in range(3, n + 1):
    for i in range(n - k + 1):
        j = i + k - 1
        if s[i] == s[j] and dp[i + 1][j - 1]:
            dp[i][j] = True

dp2 = [0] * n
for i in range(n):
    min_cut = i
    for j in range(i + 1):
        if dp[j][i]:
            if j == 0:
                min_cut = 0
                break
            else:
                min_cut = min(min_cut, dp2[j - 1] + 1)
    dp2[i] = min_cut

print(dp2[n - 1] + 1)