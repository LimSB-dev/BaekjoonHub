# 1시 , 2시, 4시, 5시, 7시, 8시, 10시, 11시
dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(r, c, depth):
    global answer

    # 큐 생성
    queue = [(r, c, depth)]

    # 방문처리
    visited[r][c] = True

    while queue:

        r, c, depth = queue.pop(0)

        for direction in range(8):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:

                # 방문 처리
                visited[nr][nc] = True

                # 가지치기
                if answer <= depth:
                    return

                # 종료조건
                if nr == er and nc == ec:
                    if answer > depth:
                        answer = depth
                    return

                queue.append((nr, nc, depth + 1))


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    visited = [[False] * n for _ in range(n)]

    # 최소 이동
    answer = INF

    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    bfs(sr, sc, 1)

    if answer == INF:
        answer = 0

    print(answer)
