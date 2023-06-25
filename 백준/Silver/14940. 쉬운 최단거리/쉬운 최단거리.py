import sys
from collections import deque
input = sys.stdin.readline

def bfs(row, col):
    visited[row][col] = True
    queue = deque([[row, col]])
    
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + delta[i][0], c + delta[i][1]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append([nr, nc])
                board[nr][nc] = board[r][c] + 1


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]

start = [0, 0]
for row in range(n):
    for col in range(m):
        if matrix[row][col] == 2:
            start = [row, col]
        elif matrix[row][col] == 0:
            visited[row][col] = True

bfs(start[0], start[1])

for row in range(n):
    for col in range(m):
        if not visited[row][col]:
            board[row][col] = -1

print('\n'.join(' '.join(map(str, row)) for row in board))