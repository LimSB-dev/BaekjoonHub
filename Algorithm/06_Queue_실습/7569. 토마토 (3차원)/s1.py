import sys
sys.stdin = open('input.txt')

from collections import deque

# 상 하 좌 우 위 아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dd = [0, 0, 0, 0, -1, 1]


def bfs(box, tomato):

    # 현재 일
    day = 0

    # 모든 박스 익히기
    while tomato:
        d, r, c = tomato.popleft()

        # 현재 토마토 날짜
        day = box[d][r][c]

        # 네 방향으로 토마토 익히기
        for direction in range(6):
            nd = d + dd[direction]
            nr = r + dr[direction]
            nc = c + dc[direction]

            # box 범위 내부 / 안 익은 토마토
            if 0 <= nd < z and 0 <= nr < h and 0 <= nc < w and box[nd][nr][nc] == 0:

                # 토마토 익힌 날짜 적기
                box[nd][nr][nc] = day + 1

                tomato.append([nd, nr, nc])
    return day - 1


w, h, z = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(h)] for _ in range(z)]

# 익은 토마토 좌표
tomato = deque()

for dep in range(z):
    for row in range(h):
        for col in range(w):

            # enqueue
            if box[dep][row][col] == 1:
                tomato.append([dep, row, col])

# 모든 익은 토마토 좌표에서 동시에 bfs 진행
answer = bfs(box, tomato)

for dep in range(z):
    for row in range(h):
        for col in range(w):

            # 안 익은 토마토가 있다면
            if box[dep][row][col] == 0:
                answer = -1

            if answer == -1:
                break
        if answer == -1:
            break
    if answer == -1:
        break

print(answer)