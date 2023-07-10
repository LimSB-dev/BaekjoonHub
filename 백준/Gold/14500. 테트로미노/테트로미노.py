import sys
input = sys.stdin.readline

def dfs(r, c, idx, total):
    global answer
    if answer >= total + max_value * (3 - idx):
        return
    if idx == 3:
        answer = max(answer, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0:
                if idx == 1:
                    visit[nr][nc] = 1
                    dfs(r, c, idx + 1, total + matrix[nr][nc])
                    visit[nr][nc] = 0
                visit[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + matrix[nr][nc])
                visit[nr][nc] = 0


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
max_value = max(map(max, matrix))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, matrix[r][c])
        visit[r][c] = 0

print(answer)