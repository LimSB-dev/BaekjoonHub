import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = dx[::-1]


def dfs(x, y):
    if maze[y][x] == 3:
        global answer
        answer = 1
        return

    visited[y][x] = True
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] != 1:
            dfs(nx, ny)


for tc in range(1, int(input()) + 1):
    answer = 0
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if maze[row][col] == 2:
                dfs(col, row)

    print(f'#{tc} {answer}')
