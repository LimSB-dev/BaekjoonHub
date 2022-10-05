import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    n = int(input())
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + (2 * dp[i - 2]) + dp[i - 3]

    answer = dp[n]

    print(f'#{tc} {answer}')
