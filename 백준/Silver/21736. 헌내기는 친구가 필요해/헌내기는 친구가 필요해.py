import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global answer
    queue = deque([doyeon])

    while queue:
        row, col = queue.popleft()

        for dr, dc in delta:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                
                if matrix[nr][nc] == "P":
                    answer += 1
                
                queue.append((nr, nc))


N, M = map(int, input().split())
matrix = [list(map(str, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
doyeon = ()

for row in range(N):
    for col in range(M):
        if matrix[row][col] == "X":
            visited[row][col] = True
        elif matrix[row][col] == "I":
            doyeon = (row, col)
            visited[row][col] = True

answer = 0

bfs()

print("TT" if answer == 0 else answer)