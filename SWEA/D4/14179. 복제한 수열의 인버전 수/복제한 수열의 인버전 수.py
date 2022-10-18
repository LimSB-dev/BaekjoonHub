for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    a = 0
    for i in range(n - 1):
        for j in range(i, n):
            if numbers[i] > numbers[j]:
                a += 1

    d = 0
    for i in range(n):
        for j in range(n):
            if numbers[i] > numbers[j]:
                d += 1

    m = 10 ** 9 + 7

    answer = k * ((2 * a) + (k - 1) * d) // 2 % m

    print(f'#{tc} {int(answer)}')