for tc in range(1, int(input()) + 1):
    n, a, b = map(int, input().split())
    max_value = min(a, b)
    min_value = n - (a + b)

    if min_value > 0:
        min_value = 0
    else:
        min_value *= -1

    answer = [max_value, min_value]

    print(f'#{tc}', *answer)
