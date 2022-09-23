for tc in range(1, int(input()) + 1):
    n = int(input())
    words = list(input())

    # 부분 집합
    sub = set()

    # 비트 연산자
    for i in range(len(words)):
        for j in range(i, len(words)):
            sub.add(''.join([words[k] for k in range(i, j + 1)]))

    sub = sorted(list(sub))

    if len(sub) > n:
        answer = sub[n - 1]
        print(f'#{tc}', answer)
    else:
        answer = 'none'
        print(f'#{tc}', answer)