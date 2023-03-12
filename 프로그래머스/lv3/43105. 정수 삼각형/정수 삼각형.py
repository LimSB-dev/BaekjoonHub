def solution(triangle):
    dp = [[j for j in i] for i in triangle]
    
    for i in range(len(triangle)):
        for j in range(i):
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + triangle[i][j])
            dp[i][j + 1] = dp[i - 1][j] + triangle[i][j + 1]
            
    return max(dp[-1])