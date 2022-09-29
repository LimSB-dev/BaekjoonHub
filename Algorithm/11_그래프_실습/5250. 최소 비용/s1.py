import sys
sys.stdin = open('input.txt', encoding='utf-8')
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col, value):

    queue = deque([[row, col, value]])

    while queue:

        row, col, value = queue.popleft()

        dp[row][col] = value

        for direction in range(4):
            nr = row + dr[direction]
            nc = col + dc[direction]

            next_value = value
            next_value += 1

            if 0 <= nr < n and 0 <= nc < n:

                next_value += abs(matrix[nr][nc] - matrix[row][col])

                if next_value < dp[nr][nc]:

                    dp[nr][nc] = next_value

                    queue.append([nr, nc, next_value])


INF = 999999999
for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * n for _ in range(n)]

    bfs(0, 0, matrix[0][0])

    print(f'#{tc} {dp[n - 1][n - 1]}')
