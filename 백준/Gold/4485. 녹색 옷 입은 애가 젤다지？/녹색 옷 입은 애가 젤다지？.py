from heapq import heappush, heappop

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(row, col):
    dp[row][col] = matrix[row][col]
    heap = [(matrix[row][col], row, col)]

    while heap:

        min_value, row, col = heappop(heap)

        if min_value <= dp[row][col]:

            for direction in range(4):
                nr = row + dr[direction]
                nc = col + dc[direction]

                if 0 <= nr < n and 0 <= nc < n:
                    new_value = min_value + matrix[nr][nc]

                    if new_value < dp[nr][nc]:
                        dp[nr][nc] = new_value
                        heappush(heap, (new_value, nr, nc))


INF = 999999999
tc = 0
while True:
    tc += 1
    n = int(input())

    if n == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = [[INF] * n for _ in range(n)]

    dijkstra(0, 0)

    answer = dp[n - 1][n - 1]

    print(f'Problem {tc}: {answer}')
