import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_safe_area = 0

for i in range(100):
    visited = [[0] * n for _ in range(n)]
    safe_area = 0
    for j in range(n):
        for k in range(n):
            if matrix[j][k] <= i:
                visited[j][k] = 1

    for j in range(n):
        for k in range(n):
            if visited[j][k] == 0:
                safe_area += 1
                visited[j][k] = 1
                stack = [(j, k)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            stack.append((nx, ny))

    max_safe_area = max(max_safe_area, safe_area)

print(max_safe_area)
