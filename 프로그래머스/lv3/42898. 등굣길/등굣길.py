MOD = 1000000007

def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for r, c in puddles:
        dp[c-1][r-1] = MOD

    for i in range(n):
        for j in range(m):
            if dp[i][j] != MOD:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD

    return dp[n-1][m-1] % MOD
