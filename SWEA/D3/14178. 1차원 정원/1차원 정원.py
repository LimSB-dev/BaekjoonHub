import math

for tc in range(1, int(input()) + 1):
    n, d = map(int, input().split())
    answer = math.ceil(n / (1 + (d * 2)))

    print(f'#{tc} {answer}')
