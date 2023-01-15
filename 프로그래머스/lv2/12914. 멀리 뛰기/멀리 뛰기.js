function solution(n) {
    let dp = [1n, 1n, 2n]
    
    for (let i = 3; i <= n; i++) {
        dp.push(dp[i - 1] + dp[i - 2])
    }
    
    return dp[n] % 1234567n
}