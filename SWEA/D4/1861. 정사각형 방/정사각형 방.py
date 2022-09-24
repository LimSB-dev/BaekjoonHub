# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# BFS 탐색
def bfs(r, c):
    global answer, cnt

    # 방문 처리
    visited[r][c] = True

    # 방 리스트 추가
    rooms.append(matrix[r][c])

    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 범위 내부 / 방문 FALSE / 현재 방 번호 차이의 절대값이 1
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and abs(matrix[r][c] - matrix[nr][nc]) == 1:

            # 방 개수 증가
            cnt += 1
            bfs(nr, nc)


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    answer = 0

    for row in range(n):
        for col in range(n):
            cnt = 1
            rooms = []
            if not visited[row][col]:
                bfs(row, col)

                # 최대값 및 방 리스트 저장
                if answer <= cnt:

                    if answer == cnt:
                        room = min(room, min(rooms))
                    else:
                        answer = cnt
                        room = min(rooms)

    print(f'#{tc} {room} {answer}')