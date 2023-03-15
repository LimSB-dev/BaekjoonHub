N, M, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
INF = 10e9

min_time, max_height = INF, 0
for height in range(257):
    block, time = 0, 0

    for i in range(N):
        for j in range(M):
            cur_height = matrix[i][j]

            if cur_height > height:
                block += cur_height - height
                time += (cur_height - height) * 2
            elif cur_height < height:
                block -= height - cur_height
                time += (height - cur_height)

    if block + B >= 0:
        if time <= min_time:
            min_time = time
            max_height = height

print(min_time, max_height)
