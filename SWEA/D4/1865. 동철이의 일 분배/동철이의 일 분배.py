def dfs(row, value):
    global answer

    # 가지치기
    if value <= answer:
        return

    # 종료 조건
    if row == n:
        answer = value
        return

    # 열 탐색
    for i in range(n):

        if not visited[i]:
            visited[i] = True
            dfs(row + 1, value * (matrix[row][i] / 100))
            visited[i] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    answer = 0

    dfs(0, 1)

    print(f'#{tc} {format(round(answer * 100, 6),".6f")}')