import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = [(r, c)]
    visited[r][c] = True
    while queue:
        r, c = queue.pop(0)

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and matrix[nr][nc] != 1:

                if matrix[nr][nc] == 3:
                    global answer
                    answer = 1
                    return

                visited[nr][nc] = True

                queue.append((nr, nc))


for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    answer = 0
    breaker = False

    for row in range(16):
        for col in range(16):

            if matrix[row][col] == 2:

                bfs(row, col)

                breaker = True
                break

        if breaker:
            break

    print(f'#{tc} {answer}')
