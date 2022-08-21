# 좌 우 하
dr = [0, 0, 1]
dc = [-1, 1, 0]


def down(x):
    cnt = 0
    y = 0
    visited = [[False] * 100 for _ in range(100)]
    while y < 99:
        for direction in range(3):
            visited[y][x] = True
            y = y + dr[direction]
            x = x + dc[direction]

            if 0 <= x < 100 and 0 <= y < 100 and matrix[y][x] == 1 and not visited[y][x]:
                cnt += 1
                break

            y -= dr[direction]
            x -= dc[direction]

    return cnt


for _ in range(10):
    answer = 0
    min_value = 10000
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    for col in range(100):
        if matrix[0][col] == 1:
            value = down(col)
            if min_value > value:
                min_value = value
                answer = col

    print(f'#{tc} {answer}')
