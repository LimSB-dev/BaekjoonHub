def solution(n):
    
    if n == 2:
        return 3
    elif n == 4:
        return 11
    else:
        MOD = 1000000007
        n = int(n / 2)
        dp = [3, 11]
        
        for num in range(3, n + 1):
            nextValue = (dp[1] * 4 - dp[0]) % MOD
            dp = [dp[1], nextValue]
        
        print(dp)
        
        return dp[1]