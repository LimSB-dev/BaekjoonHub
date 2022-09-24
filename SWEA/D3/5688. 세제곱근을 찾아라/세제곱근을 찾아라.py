for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = 0

    while True:
        answer += 1
        if n == answer**3:
            break

        if answer**3 >= 10**18:
            answer = -1
            break

    print(f'#{tc} {answer}')
