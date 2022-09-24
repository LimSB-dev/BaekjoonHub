for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    over = []

    for i in range(1 << n):
        sum_value = 0
        for j in range(n):
            if i & (1 << j):
                sum_value += s[j]

            if sum_value >= b:
                over.append(sum_value)
                break

    answer = min(over) - b

    print(f'#{tc} {answer}')
