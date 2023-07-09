import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]  # DP 테이블

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(row, col):

    if dp[row][col] != -1:  # 이미 계산한 값이 있는 경우
        return dp[row][col]

    if row == n - 1 and col == m - 1:
        dp[row][col] = 1  # 목적지에 도달한 경우 경로 개수 1로 설정
        return dp[row][col]

    count = 0
    for dr, dc in dir:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] < matrix[row][col]:
            count += dfs(nr, nc)  # 재귀적으로 다음 위치로 이동하여 경로 개수 누적

    dp[row][col] = count  # 계산한 경로 개수 저장
    return dp[row][col]

result = dfs(0, 0)
print(result)
