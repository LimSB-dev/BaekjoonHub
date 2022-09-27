import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dfs(row, col, value):
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
        col_copy = col.copy()

        if i not in col_copy:
            col_copy.append(i)
            dfs(row + 1, col_copy, value * (matrix[row][i] / 100))


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    dfs(0, [], 1)

    print(f'#{tc} {format(round(answer * 100, 6),".6f")}')
