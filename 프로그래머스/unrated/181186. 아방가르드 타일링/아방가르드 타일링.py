MOD = 1000000007

def solution(n):
    dp = [0, 1, 3, 10] + [0] * (n - 3)
    cache = [8, 0, 2]

    for i in range(4, n+1):
        remainder = i % 3
        sum_value = cache[remainder]
        plus = 4 if i % 3 == 0 else 2

        sum_value += dp[i - 1] * 1
        sum_value += dp[i - 2] * 2
        sum_value += dp[i - 3] * 5
        sum_value += plus
        sum_value %= MOD

        cache[remainder] += dp[i - 1] * 2
        cache[remainder] += dp[i - 2] * 2
        cache[remainder] += dp[i - 3] * 4
        cache[remainder] %= MOD

        dp[i] = sum_value

    return dp[n]
