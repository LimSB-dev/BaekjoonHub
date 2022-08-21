dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

w, h = map(int, input().split())
k = int(input())
answer = 0
matrix = [[0] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]

row = col = 0
direction = 0

if k <= w * h:
    for _ in range(k - 1):
        visited[row][col] = True
        row += dr[direction]
        col += dc[direction]
        if 0 <= row < h and 0 <= col < w and not visited[row][col]:
            pass
        else:
            row -= dr[direction]
            col -= dc[direction]

            direction = (direction + 1) % 4

            row += dr[direction]
            col += dc[direction]

    print(col + 1, row + 1)
else:
    print(answer)