import sys
sys.setrecursionlimit(100000)

# 상 하 좌 우 대각선 4개
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]


def dfs(p, q):
    visited[p][q] = True
    for direction in range(8):
        np = p + dx[direction]
        nq = q + dy[direction]
        if 0 <= np <= h - 1 and 0 <= nq <= w - 1 and not visited[np][nq] and graph[np][nq] == 1:
            dfs(np, nq)


while True:
    answer = 0
    w, h = map(int, input().split())
    if w + h == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    # 탐색
    for row in range(h):
        for col in range(w):
            if not visited[row][col] and graph[row][col] == 1:
                answer += 1
                dfs(row, col)

    print(answer)