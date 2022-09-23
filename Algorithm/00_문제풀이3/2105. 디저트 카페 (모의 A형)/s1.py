import sys
sys.stdin = open('input.txt', encoding='utf-8')

# ↘ ↙ ↖ ↗
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dfs(desserts, r, c):
    global answer

    desserts.add(matrix[r][c])                                          # 새로운 디저트 추가

    for direction in range(4):                                          # 4방향 탐색

        desserts_copy = desserts.copy()

        while True:


        nr = r + dr[direction]
        nc = c + dc[direction]

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:         # 배열 내부 / 방문 False

            if matrix[nr][nc] not in desserts_copy:                     # 먹은적 없는 dessert
                visited[nr][nc] = True                                  # 방문 처리
                dfs(desserts_copy, nr, nc)                   # 재귀

            elif nr == row and nc == col and len(desserts_copy) >= 4:   # 처음 위치 복귀
                if answer < len(desserts_copy):
                    print(row, col, desserts_copy)
                    answer = len(desserts_copy)
                    return


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = -1

    for row in range(n):
        for col in range(n):
            visited = [[False] * n for _ in range(n)]
            desserts_set = set()
            dfs(desserts_set, row, col)

    print(f'#{tc} {answer}')
