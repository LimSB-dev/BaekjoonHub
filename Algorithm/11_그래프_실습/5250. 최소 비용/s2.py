import sys
sys.stdin = open('input.txt', encoding='utf-8')
from heapq import heappush, heappop

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(row, col):

    distance[row][col] = 0
    heap = [(distance[row][col], row, col)]

    while heap:
        dist, row, col = heappop(heap)

        if distance[row][col] >= dist:

            for direction in range(4):
                nr = row + dr[direction]
                nc = col + dc[direction]

                next_dist = dist
                next_dist += 1

                if 0 <= nr < n and 0 <= nc < n:
                    height = matrix[nr][nc] - matrix[row][col]
                    next_dist += height if height > 0 else 0

                    if next_dist < distance[nr][nc]:
                        distance[nr][nc] = next_dist
                        heappush(heap, (next_dist, nr, nc))


INF = 999999999
for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    distance = [[INF] * n for _ in range(n)]
    dijkstra(0, 0)

    print(f'#{tc} {distance[n - 1][n - 1]}')
