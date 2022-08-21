for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for y in range(n - m + 1):
        for x in range(n - m + 1):
            sum_value = 0
            for q in range(m):
                for p in range(m):
                    sum_value += matrix[x + p][y + q]

            if sum_value > answer:
                answer = sum_value
            
    print(f'#{tc} {answer}')