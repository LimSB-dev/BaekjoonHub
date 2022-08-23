import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, words):
    words += matrix[y][x]

    if len(words) == 6:
        answer.append(words)
        return

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, words)


matrix = [list(input().split()) for _ in range(5)]
answer = []

for row in range(5):
    for col in range(5):
        dfs(col, row, '')

answer = set(answer)

print(len(answer))
