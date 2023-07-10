import sys
input = sys.stdin.readline


def dfs(row, post):
    global answer

    # 종료 조건
    if row == n:
        answer += 1
        return

    # 열 탐색
    for col in range(n):

        # 행, 열 확인
        if not d1[row + col] and not d2[row + n - 1 - col] and not visited[col]:

            visited[col] = True
            d1[row + col] = True
            d2[row + n - 1 - col] = True

            dfs(row + 1, col)

            # 가지치기 / 종료조건 이후
            visited[col] = False
            d1[row + col] = False
            d2[row + n - 1 - col] = False


n = int(input())
visited = [False] * n
d1 = [False] * (n + n + 1)
d2 = [False] * (n + n + 1)
answer = 0

dfs(0, 999999999)

print(answer)
