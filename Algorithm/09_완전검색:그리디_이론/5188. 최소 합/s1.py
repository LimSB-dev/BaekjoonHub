import sys
sys.stdin = open('input.txt')

# 아래, 오른쪽
dr = [1, 0]
dc = [0, 1]


def dfs(row, col, value):
    global answer
    value += matrix[row][col]

    # 가지치기
    if answer <= value:
        return

    # 종료조건
    if row == n - 1 and col == n - 1:
        if answer > value:
            answer = value

    # 탐색
    for directions in range(2):
        nr = row + dr[directions]
        nc = col + dc[directions]

        # 배열 내부
        if nr < n and nc < n:
            dfs(nr, nc, value)


INF = 999999999
for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = INF

    dfs(0, 0, 0)

    print(f'#{tc} {answer}')