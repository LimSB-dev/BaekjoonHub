import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(p, q):
    visited[p][q] = True
    for direction in range(4):
        np = p + dx[direction]
        nq = q + dy[direction]
        if 0 <= np <= h - 1 and 0 <= nq <= w - 1 and not visited[np][nq] and graph[np][nq] == 1:
            dfs(np, nq)


for tc in range(1, int(input()) + 1):
    answer = 0
    w, h, k = map(int, input().split())
    graph = [[0] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    # 2차원 리스트
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 탐색
    for row in range(h):
        for col in range(w):
            if not visited[row][col] and graph[row][col] == 1:
                answer += 1
                dfs(row, col)

    print(answer)