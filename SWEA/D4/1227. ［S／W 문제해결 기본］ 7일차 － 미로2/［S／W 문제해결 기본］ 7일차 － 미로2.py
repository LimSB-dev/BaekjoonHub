from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col):
    global answer

    queue = deque([[row, col]])

    while queue:

        r, c = queue.popleft()

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if matrix[nr][nc] == 0:

                matrix[nr][nc] = 1

                queue.append([nr, nc])

            if matrix[nr][nc] == 3:
                answer = 1


for _ in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(100)]
    answer = 0

    for row in range(100):
        for col in range(100):
            value = matrix[row][col]

            if value == 2:
                s_r, s_c = row, col
            elif value == 3:
                e_r, e_c = row, col

    bfs(s_r, s_c)

    print(f'#{tc} {answer}')