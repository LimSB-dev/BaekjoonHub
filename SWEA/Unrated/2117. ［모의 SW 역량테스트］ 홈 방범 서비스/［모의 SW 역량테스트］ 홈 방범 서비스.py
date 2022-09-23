for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    people = 0
    answer = 0

    for row in matrix:
        people += sum(row)

    max_cost = people * m

    k = 0
    while True:
        k += 1
        cost = k * k + (k - 1) * (k - 1)

        if max_cost < cost:
            break

        for row in range(n):
            for col in range(n):
                secure = 0
                for r in range(n):
                    for c in range(n):
                        if k > abs(r - row) + abs(c - col):
                            secure += matrix[r][c]

                if cost <= secure * m:
                    if answer < secure:
                        answer = secure

    print(f'#{tc} {answer}')