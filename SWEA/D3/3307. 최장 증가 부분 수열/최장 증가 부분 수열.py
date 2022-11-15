for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = 1
    dp = [0] * n
    
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                if max_value < dp[i]:
                    max_value = dp[i]

    print(f'#{tc} {max_value}')