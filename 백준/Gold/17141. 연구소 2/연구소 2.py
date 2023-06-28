import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
disabled_virus = []
min_time = float('inf')

for row in range(N):
    for col in range(N):
        if matrix[row][col] == 2:
            disabled_virus.append((row, col, 3))

def spread_virus(virus):
    visited = [[0] * N for _ in range(N)]
    queue = deque()

    for row, col, time in virus:
        queue.append((row, col, time))
        visited[row][col] = time

    while queue:
        row, col, time = queue.popleft()

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] != 1 and visited[nr][nc] == 0:
                next_time = time + 1
                visited[nr][nc] = next_time
                queue.append((nr, nc, next_time))

    max_time = 0
    for row in range(N):
        for col in range(N):
            # 벽이 아닌 공간일 경우
            if matrix[row][col] != 1:
                # 바이러스가 퍼지지 않은 공간이 있을 경우
                if visited[row][col] == 0:
                    return -1
                
                max_time = max(max_time, visited[row][col])

    return max_time - 3


for virus in combinations(disabled_virus, M):
    result = spread_virus(virus)
    if result != -1:
        min_time = min(min_time, result)

print(min_time if min_time != float('inf') else -1)