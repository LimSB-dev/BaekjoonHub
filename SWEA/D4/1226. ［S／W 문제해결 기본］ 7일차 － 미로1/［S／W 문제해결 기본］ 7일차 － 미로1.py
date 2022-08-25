# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):

    # 큐 생성
    queue = [(r, c)]

    # 방문 처리
    visited[r][c] = True

    # queue가 빈 리스트가 될 때까지 반복
    while queue:
        r, c = queue.pop(0)

        for direction in range(4):
            nr = r + dr[direction]
            nc = c + dc[direction]

            # 2차원 범위 내부 / 방문 기록 False / 벽이 아닌 경우
            if 0 <= nr < 16 and 0 <= nc < 16 and not visited[nr][nc] and matrix[nr][nc] != 1:

                # 종료 조건
                if matrix[nr][nc] == 3:
                    global answer
                    answer = 1
                    return

                # 방문 처리
                visited[nr][nc] = True

                queue.append((nr, nc))


for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    # 연결 확인
    answer = 0
    breaker = False

    for row in range(16):
        for col in range(16):

            if matrix[row][col] == 2:

                bfs(row, col)

                breaker = True
                break

        if breaker:
            break

    print(f'#{tc} {answer}')
