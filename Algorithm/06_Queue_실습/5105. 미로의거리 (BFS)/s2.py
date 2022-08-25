import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, depth):
    global answer

    queue = [(r, c, depth)]

    while queue:
        r, c, depth = queue.pop(0)

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] != 1:

                if answer <= depth:
                    return

                if matrix[nr][nc] == 3:
                    if answer > depth:
                        answer = depth
                    return

                visited[nr][nc] = True

                queue.append((nr, nc, depth + 1))


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    # 최단 거리
    answer = INF

    # 현재 거리
    dist = 0

    breaker = False

    for row in range(n):
        for col in range(n):

            if matrix[row][col] == 2:

                bfs(row, col, dist)

                breaker = True
                break

        if breaker:
            break

    if answer == INF:
        answer = 0

    print(f'#{tc} {answer}')
