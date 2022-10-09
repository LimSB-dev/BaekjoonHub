from itertools import combinations
from  collections import deque
from copy import deepcopy

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    queue = deque(virous)

    while queue:

        r, c = queue.popleft()

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            if 0 <= nr < n and 0 <= nc < m:
                if lab[nr][nc] == 0:
                    lab[nr][nc] = 2
                    queue.append([nr, nc])


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
virous = []
empty = []

for row in range(n):
    for col in range(m):
        value = matrix[row][col]
        if value == 2:
            virous.append([row, col])
        elif value == 0:
            empty.append([row, col])

for walls in combinations(empty, 3):
    lab = deepcopy(matrix)
    max_value = 0
    for wall in walls:
        row, col = wall
        lab[row][col] = 1

    bfs()

    for row in range(n):
        for col in range(m):
            value = lab[row][col]
            if value == 0:
                max_value += 1

    if max_value > answer:
        answer = max_value

print(answer)
