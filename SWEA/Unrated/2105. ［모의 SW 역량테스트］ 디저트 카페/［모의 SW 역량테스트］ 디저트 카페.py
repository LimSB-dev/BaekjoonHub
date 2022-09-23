dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dfs(r, c, path, direction):
    global answer

    if direction == 3 and r == row and c == col and len(path) > 2:
        answer = max(answer, len(path))
        return

    if 0 <= r < n and 0 <= c < n and cafe[r][c] not in path:
        new_path = path + [cafe[r][c]]

        # 직진
        nr = r + dr[direction]
        nc = c + dc[direction]

        dfs(nr, nc, new_path, direction)

        # 꺾는 경우
        if direction < 3:
            nr = r + dr[direction + 1]
            nc = c + dc[direction + 1]
            dfs(nr, nc, new_path, direction + 1)


for tc in range(1, int(input()) + 1):
    n = int(input())
    cafe = [list(map(int, input().split())) for _ in range(n)]

    answer = -1
    for row in range(n):
        for col in range(n):
            dfs(row, col, [], 0)

    print(f'#{tc} {answer}')