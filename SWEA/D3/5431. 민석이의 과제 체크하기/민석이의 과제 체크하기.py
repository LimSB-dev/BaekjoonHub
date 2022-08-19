for tc in range(1, int(input()) + 1):
    answer = []
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(1, n + 1):
        if not i in arr:
            answer.append(i)

    print(f'#{tc}', *answer)
