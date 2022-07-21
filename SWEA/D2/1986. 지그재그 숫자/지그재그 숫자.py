t = int(input())

for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    for i in range(1, n + 1):
        if i % 2 == 0:
            i *= -1
            answer += i
        else:
            answer += i
    print(f'#{tc} {answer}')