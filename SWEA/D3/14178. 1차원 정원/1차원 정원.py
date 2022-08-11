for tc in range(1, int(input()) + 1):
    n, d = map(int, input().split())

    answer = n // (1 + (d * 2))
    answer_clone = n / (1 + (d * 2))
    if answer != answer_clone:
        answer += 1

    print(f'#{tc} {answer}')
