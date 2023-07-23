import sys
from collections import deque


def bfs(matrix, n, m):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # visited 배열: visited[x][y][z]
    # x, y는 좌표를 의미하고, z는 벽을 부순 상태를 나타냄 (0: 벽을 부수지 않은 상태, 1: 벽을 부순 상태)
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, 1, 0)])  # 시작점 (0, 0)에서 시작하므로 (0, 0, 1, 0)을 큐에 추가
    visited[0][0][0] = True

    while queue:
        x, y, dist, wall_broken = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽을 부수지 않은 상태에서 이동
                if matrix[nx][ny] == 0 and not visited[nx][ny][wall_broken]:
                    visited[nx][ny][wall_broken] = True
                    queue.append((nx, ny, dist + 1, wall_broken))
                # 벽을 부수지 않은 상태에서 벽을 만났을 때, 벽을 부수고 이동
                elif matrix[nx][ny] == 1 and wall_broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, 1))

    return -1  # 도착점에 도달할 수 없는 경우


n, m = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(n)]

result = bfs(matrix, n, m)
print(result)
