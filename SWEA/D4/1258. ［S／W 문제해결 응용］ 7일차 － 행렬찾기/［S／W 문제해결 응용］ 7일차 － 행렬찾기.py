# 하 우
dx = [0, 1]
dy = [1, 0]


def dfs(x, y):
    visited[x][y] = True
    
    # 상하좌우 델타 검색
    for direction in range(2):
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 이동 후 범위 내부이고 방문한 적이 없고 값이 0이 아닌 경우
        if 0 <= nx <= (n - 1) and 0 <= ny <= (n - 1) and (not visited[nx][ny]) and graph[nx][ny] != 0:
            
            # 오른쪽 이동 시
            if direction == 1:
                global sub_x
                sub_x += 1
                
            # 아래 이동 시
            elif direction == 0:
                global sub_y
                sub_y += 1

            dfs(nx, ny)


for tc in range(1, int(input()) + 1):
    total = 0
    matrix = []
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            sub_x = 1
            sub_y = 1
            # 방문한 적이 없고 그래프의 값이 0이 아닌 경우
            if not visited[row][col] and graph[row][col] != 0:
                dfs(row, col)

                # 중복 계산 제거
                if sub_y > 1:
                    sub_x //= sub_y
                    sub_x += 1

                # 방문 배열 조정
                for p in range(sub_x):
                    for q in range(sub_y):
                        visited[row + p][col + q] = True
                total += 1
                matrix.append([sub_x, sub_y])

    # matrix를 크기 순으로 정렬
    matrix = sorted(matrix, key=lambda x: x[0] * x[1])

    # 만약 크기가 같을 경우 sub_x의 값을 기준으로 오름차순
    for i in range(total - 1, 0, -1):
        for j in range(i):
            
            # 두 행렬의 곱이 같고 행이 내림차순일 경우
            if matrix[j][0] * matrix[j][1] == matrix[j + 1][0] * matrix[j + 1][1] and matrix[j][0] > matrix[j + 1][0]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

    answer = []
    for i in matrix:
        answer.extend(i)

    print(f'#{tc} {total}', *answer)
