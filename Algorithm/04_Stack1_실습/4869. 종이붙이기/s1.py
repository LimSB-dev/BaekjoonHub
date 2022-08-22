import sys
sys.stdin = open('input.txt')


def dp(num):
    if num == 1:
        return 1
    elif num == 2:
        return 3
    else:
        return dp(num - 1) + 2 * dp(num - 2)


for tc in range(1, int(input()) + 1):
    n = int(input())
    n //= 10
    answer = dp(n)

    print(f'#{tc} {answer}')
