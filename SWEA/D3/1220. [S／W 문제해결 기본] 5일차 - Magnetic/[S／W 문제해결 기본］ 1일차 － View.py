for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    answer = [0] * n

    for col in range(n):
        now = ''
        for row in range(n):
            if matrix[row][col] == 1:
                now = 'n'
            elif matrix[row][col] == 2:
                if now == 'n':
                    answer[col] += 1
                now = 's'

    print(f'#{tc}', end=' ')
    print(sum(answer))
