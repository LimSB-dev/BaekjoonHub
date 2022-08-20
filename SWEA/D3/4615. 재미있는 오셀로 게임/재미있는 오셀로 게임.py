# 상하좌우 대각선
dr = [-1, 1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]


def check(p, q, color):
    # 가로 세로
    for direction in range(8):
        be_change = []
        # 한 방향으로 반복
        nx = p
        ny = q
        while True:
            nx += dr[direction]
            ny += dc[direction]
            # 2차원 배열 내부일 경우
            if 0 <= nx < n and 0 <= ny < n:    
                # 다른 색의 돌인 경우
                if matrix[nx][ny] + color == 3:
                    be_change.append([nx, ny])
                # 범위 내부이고 돌이 없다면
                if matrix[nx][ny] == 0:
                    break
                # 범위 내부이고 같은 색의 돌인 경우
                if matrix[nx][ny] == color:
                    # 저장해둔 바뀔 돌 좌표를 불러와 좌표값 위의 돌을 변경
                    for np, nq in be_change:
                        matrix[np][nq] = color
                    break
            else:
                break


for tc in range(1, int(input()) + 1):
    answer = [0, 0]
    n, m = map(int, input().split())
    matrix = [[0] * n for _ in range(n)]
    mid = n // 2
    # 흑돌
    matrix[mid - 1][mid] = matrix[mid][mid - 1] = 1
    # 백돌
    matrix[mid - 1][mid - 1] = matrix[mid][mid] = 2

    for i in range(m):
        x, y, stone = map(int, input().split())
        x -= 1
        y -= 1
        matrix[x][y] = stone
        check(x, y, stone)

    # 게임이 끝난 후 돌의 개수
    for row in range(n):
        answer[0] += matrix[row].count(1)
        answer[1] += matrix[row].count(2)

    # for i in matrix:
    #     print(i)
    print(f'#{tc}', *answer)
