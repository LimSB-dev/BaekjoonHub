from collections import deque


def check_shape(num, d):
    check = False
    if num == 0:
        pass
    elif d == 0:
        if num in [1, 2, 5, 6]:
            check = True
    elif d == 1:
        if num in [1, 2, 4, 7]:
            check = True
    elif d == 2:
        if num in [1, 3, 4, 5]:
            check = True
    elif d == 3:
        if num in [1, 3, 6, 7]:
            check = True
    return check


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 터널 구조물 타입 별 탐색 범위
def find_range(num):
    ranges = 0
    if num == 1:
        ranges = range(4)
    elif num == 2:
        ranges = [0, 1]
    elif num == 3:
        ranges = [2, 3]
    elif num == 4:
        ranges = [0, 3]
    elif num == 5:
        ranges = [1, 3]
    elif num == 6:
        ranges = [1, 2]
    elif num == 7:
        ranges = [0, 2]
    return ranges


def bfs(row, col, cnt):
    global answer

    answer += 1

    cnt += 1

    # queue 생성
    queue = deque([[row, col, cnt]])

    # 방문 처리
    visited[row][col] = True

    # queue 빌 때까지 반복
    while queue:

        # dequeue
        row, col, cnt = queue.popleft()

        # 터널 구조물 타입
        shape = matrix[row][col]

        # 터널 구조물 타입 별 탐색 범위
        ranges = find_range(shape)

        # 탐색
        for direction in ranges:
            nr = row + dr[direction]
            nc = col + dc[direction]

            # 범위 내부 / 방문 FALSE
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:

                # 다음 터널의 모양
                next_shape = matrix[nr][nc]

                # 방향에 따라 다음 터널로 진입 가능한지
                if check_shape(next_shape, direction):

                    # 종료 조건
                    if L < cnt:
                        return

                    # 방문처리
                    visited[nr][nc] = True

                    # 장소의 수 증가
                    answer += 1

                    # enqueue
                    queue.append([nr, nc, cnt + 1])


for tc in range(1, int(input()) + 1):
    n, m, r, c, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    answer = 0

    bfs(r, c, 1)

    print(f'#{tc} {answer}')
