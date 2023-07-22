import sys
input = sys.stdin.readline

answer = 0
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
direction = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


for row in range(m):
    for col in range(n):
        if matrix[row][col] == 1 and not visited[row][col]:
            answer += 1
            stack = [(row, col)]
            visited[row][col] = True
            while stack:
                r, c = stack.pop()
                for dr, dc in direction:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] == 1:
                        visited[nr][nc] = True
                        stack.append((nr, nc))

print(answer)
