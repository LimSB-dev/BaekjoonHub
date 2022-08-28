for tc in range(1, int(input()) + 1):
    p, q = map(float, input().split())
    answer = 'NO'

    s1 = (1 - p) * q

    s2 = p * (1 - q) * q

    if s1 < s2:
        answer = 'YES'

    print(f'#{tc} {answer}')
