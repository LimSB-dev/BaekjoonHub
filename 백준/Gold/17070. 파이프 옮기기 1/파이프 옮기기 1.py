house_size = int(input())
house = [list(map(int, input().split())) for _ in range(house_size)]

dp = [[[0]*3 for _ in range(house_size+1)] for _ in range(house_size+1)]

dp[0][1][0] = 1

for r in range(house_size):
    for c in range(house_size):
        # 벽일경우
        if house[r][c] == 1:
            dp[r+1][c+1][2] = 0
            dp[r+1][c][1] = 0
            dp[r+1][c][2] = 0
            dp[r][c+1][0] = 0
            dp[r][c+1][2] = 0
            continue
        # 가로방향 = 가로방향, 대각선방향으로 왔을때
        dp[r][c+1][0] += dp[r][c][0] + dp[r][c][2]

        # 세로방향 = 세로방향, 대각선방향으로 왔을때
        dp[r+1][c][1] += dp[r][c][1] + dp[r][c][2]

        # 대각선방향 = 가로, 세로, 대각선 전부
        dp[r+1][c+1][2] += sum(dp[r][c])

print(sum(dp[house_size][house_size]))