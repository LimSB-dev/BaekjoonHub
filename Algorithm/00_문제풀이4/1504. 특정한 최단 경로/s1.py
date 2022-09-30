dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, words):
    words += matrix[y][x]

    if len(words) == 7:
        answer.append(words)
        return

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, words)


for tc in range(1, int(input()) + 1):
    matrix = [list(input().split()) for _ in range(4)]
    answer = []

    for row in range(4):
        for col in range(4):
            dfs(col, row, '')

    answer = set(answer)

    print(f'#{tc} {len(answer)}')