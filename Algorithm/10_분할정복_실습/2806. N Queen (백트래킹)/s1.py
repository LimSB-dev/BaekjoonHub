import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dfs(row, post):
    global answer

    # 종료 조건
    if row == n:
        answer += 1
        return

    # 열 탐색
    for col in range(n):

        # 행, 열 확인
        if abs(post - col) > 1 and not visited[col]:

            visited[col] = True

            dfs(row + 1, col)

            # 가지치기 / 종료조건 이후
            visited[col] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    visited = [False] * n
    answer = 0

    dfs(0, 999999999)

    print(f'#{tc} {answer}')
