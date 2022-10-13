# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

block = {
    1: [2, 0, 3, 1],
    2: [3, 2, 0, 1],
    3: [1, 3, 0, 2],
    4: [2, 3, 1, 0],
    5: [2, 3, 0, 1],
}

# 깊이 우선 탐색
def dfs(nr, nc, direction, depth):
    global max_value, block

    while True:
        nr += dr[direction]
        nc += dc[direction]

        # 이차원 배열 내부
        if 0 <= nr < n and 0 <= nc < n:

            value = matrix[nr][nc]

            if nr == row and nc == col:
                if depth > max_value:
                    max_value = depth
                return
            if value == -1:
                if depth > max_value:
                    max_value = depth
                return
            elif 1 <= value <= 5:
                # 점수 증가
                depth += 1

                direction = block.get(value)[direction]

            elif 6 <= value <= 10:
                pos_1, pos_2 = hole[value]
                r1, c1 = pos_1
                r2, c2 = pos_2

                if nr == r1 and nc == c1:
                    nr, nc = r2, c2
                else:
                    nr, nc = r1, c1
        # 범위를 벗어날 경우
        else:
            # 점수 증가
            depth += 1

            # 방향 전환
            direction = (direction + 2) % 4


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    hole = [[] for _ in range(11)]

    # 웜홀 좌표 저장
    for row in range(n):
        for col in range(n):
            value = matrix[row][col]

            if value >= 6:
                hole[value].append([row, col])

    # 이차원 배열 탐색
    for row in range(n):
        for col in range(n):

            if matrix[row][col] == 0:
                # 현재 좌표에서 최대값
                max_value = 0

                # 4 방향 탐색
                for i in range(4):
                    dfs(row, col, i, 0)

                # 최대값 대소 비교
                if max_value > answer:
                    answer = max_value

    print(f'#{tc} {answer}')
