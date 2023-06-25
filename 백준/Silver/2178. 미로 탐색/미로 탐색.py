import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    while queue:
        row, col, cnt = queue.popleft()
        if row == N - 1 and col == M - 1:
            return cnt
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and matrix[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))


N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

answer = bfs()

print(answer)