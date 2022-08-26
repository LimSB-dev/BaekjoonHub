for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    bi = format(m, 'b')
    answer = 'ON'
    if len(bi) >= n:
        for i in range(1, n + 1):

            if bi[-1 * i] != '1':
                answer = 'OFF'
                break
    else:
        answer = 'OFF'
    print(f'#{tc} {answer}')
