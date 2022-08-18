import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    a = 1
    b = 3
    n = int(input())
    n //= 10
    for _ in range(n - 1):
        a, b = b, b + (2 * a)

    print(f'#{tc} {a}')
