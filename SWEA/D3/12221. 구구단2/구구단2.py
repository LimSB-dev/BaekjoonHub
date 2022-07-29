t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        answer = a * b
    else:
        answer = -1

    print(f'#{tc} {answer}')
