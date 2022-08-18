# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    # 상 하 좌 우
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 2차원 배열 내부에 있고 아직 방문하지 않았으며 집일 경우
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and not visited[nx][ny] and matrix[nx][ny] == 1:
            # 재귀 함쉬 실행
            dfs(nx, ny)


n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = []

for row in range(n):
    for col in range(n):
        # 방문하지 않은 집일 경우
        if not visited[row][col] and matrix[row][col] == 1:
            # 단지 초기화
            total = 0

            # dfs 함수 실행
            dfs(row, col)

            # 정답에 단지 수 추가
            answer.append(total)

print(len(answer))
for i in sorted(answer):
    print(i)
