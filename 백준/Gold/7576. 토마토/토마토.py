from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(box, tomato):

    # 현재 일
    day = 0

    # 모든 박스 익히기
    while tomato:
        r, c = tomato.popleft()

        # 현재 토마토 날짜
        day = box[r][c]

        # 네 방향으로 토마토 익히기
        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            # box 범위 내부 / 안 익은 토마토
            if 0 <= nr < h and 0 <= nc < w and box[nr][nc] == 0:

                # 토마토 익힌 날짜 적기
                box[nr][nc] = day + 1

                tomato.append([nr, nc])
    return day - 1


INF = 999999999

w, h = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

# 익은 토마토 좌표
tomato = deque()

for row in range(h):
    for col in range(w):

        # 방문 처리 및 enqueue
        if box[row][col] == 1:
            visited[row][col] = True
            tomato.append([row, col])

        # 토마토가 없는 칸은 방문 처리
        if box[row][col] == -1:
            visited[row][col] = True

# 모든 익은 토마토 좌표에서 동시에 bfs 진행
answer = bfs(box, tomato)

for row in range(h):
    for col in range(w):

        # 안 익은 토마토가 있다면
        if box[row][col] == 0:
            answer = -1

        if answer == -1:
            break
    if answer == -1:
        break

print(answer)
