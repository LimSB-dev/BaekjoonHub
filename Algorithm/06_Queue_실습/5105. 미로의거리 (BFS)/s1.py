import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, dist, visited):
    global answer

    # 방문 처리
    visited[r][c] = True

    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] != 1:

            # 거리 증가
            dist += 1

            # 가지치기
            if answer <= dist:
                return

            # 종료 조건
            if matrix[nr][nc] == 3:
                if answer > dist:
                    answer = dist
                return

            bfs(nr, nc, dist, visited)

            # 가지치기 당하거나 끝까지 간 경우
            visited[nr][nc] = False
            dist -= 1


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    breaker = False

    # 최소 이동 수
    answer = INF

    # 이동 거리
    dist = -1

    for row in range(n):
        for col in range(n):

            if matrix[row][col] == 2:

                bfs(row, col, dist, visited)

                breaker = True
                break

        if breaker:
            break

    # 탈출 불가
    if answer == INF:
        answer = 0

    print(f'#{tc} {answer}')
