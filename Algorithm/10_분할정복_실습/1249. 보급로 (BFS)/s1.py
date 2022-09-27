import sys
sys.stdin = open('input.txt', encoding='utf-8')

from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col, visited, dp):

    # 방문 처리
    visited[row][col] = True

    # queue 생성
    queue = deque([[row, col]])

    while queue:

        # dequeue
        row, col = queue.popleft()

        for direction in range(4):
            nr = row + dr[direction]
            nc = col + dc[direction]

            if 0 <= nr < n and 0 <= nc < n:
                time = dp[row][col] + matrix[nr][nc]

                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    dp[nr][nc] = time
                    queue.append([nr, nc])
                elif dp[nr][nc] > time:
                    dp[nr][nc] = time
                    queue.append([nr, nc])


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    bfs(0, 0, visited, dp)

    print(f'#{tc} {dp[n - 1][n - 1]}')
