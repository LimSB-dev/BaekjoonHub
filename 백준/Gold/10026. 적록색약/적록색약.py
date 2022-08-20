import sys
sys.setrecursionlimit(100000)

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(x, y, color):
    visited[x][y] = True
    for direction in range(4):
        nx = x + dr[direction]
        ny = y + dc[direction]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] == color:
            dfs(nx, ny, color)


n = int(input())
matrix = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
total1 = 0
total2 = 0

# 일반인
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            total1 += 1
            dfs(row, col, matrix[row][col])

# 방문 초기화
visited = [[False] * n for _ in range(n)]

# 2차원 배열 R -> G 변경
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'R':
            matrix[row][col] = 'G'

# 적록색약
for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            total2 += 1
            dfs(row, col, matrix[row][col])

print(total1, total2)
