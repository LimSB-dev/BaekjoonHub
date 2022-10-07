import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    n = int(input())
    dp = [[0] * n for _ in range(n)]

    dp[n - 1][0] = 1
    dp[0][n - 1] = 1

    answer = 0

    print(f'#{tc} {answer}')
