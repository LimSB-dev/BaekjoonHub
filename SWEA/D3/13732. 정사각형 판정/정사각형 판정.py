for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(input().strip()) for _ in range(n)]
    a, b, c, d = 21, 21, -1, -1
    answer = 'yes'
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == '#':
                a, b, c, d = min(a, row), min(b, col), max(c, row), max(d, col)

    if abs(c-a) != abs(d-b):
        answer = 'no'

    for row in range(a, c+1):
        for col in range(b, d+1):
            if matrix[row][col] != '#':
                answer = 'no'
    print(f'#{tc} {answer}')
