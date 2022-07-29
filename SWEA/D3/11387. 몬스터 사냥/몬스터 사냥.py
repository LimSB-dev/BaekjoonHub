t = int(input())

for tc in range(1, t + 1):
    d, l, n = map(int, input().split())
    answer = 0
    for i in range(n):
        answer += d * (1 + l * i * (1 / 100))

    print(f'#{tc} {int(answer)}')
