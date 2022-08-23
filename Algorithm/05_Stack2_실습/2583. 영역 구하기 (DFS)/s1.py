import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = dx[::-1]


def dfs(x, y):
    visited[y][x] = True
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx]:
            global space
            space += 1
            dfs(nx, ny)


w, h, k = map(int, input().split())
visited = [[False] * w for _ in range(h)]
answer = 0
arr = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            visited[row][col] = True

for row in range(h):
    for col in range(w):
        if not visited[row][col]:
            space = 1
            answer += 1
            dfs(col, row)
            arr.append(space)

arr.sort()

print(answer)
print(*arr)
