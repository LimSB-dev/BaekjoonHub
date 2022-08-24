import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt):
    global answer

    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 2차원 배열 범위 내부 / 방문 전적 False / 빈 영역
        if 0 <= nr < n and 0 <= nr < n and not visited[nr][nc] and field[nr][nc] == 0:
            visited[nr][nc] = True    # 방문 처리



for tc in range(1, int(input()) + 1):
    n = int(input())    # 맵의 크기
    field = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    monster = []
    client = []
    for row in range(n):
        for col in range(n):

            value = field[row][col]    # 종류

            # 몬스터
            if value < 0:
                monster.append([row, col, value])

            # 고객
            elif value > 0:
                client.append([row, col, value])

    answer = 0  # 최단 거리

    # 사냥꾼의 시작 위치: 1, 1
    # 현재 거리: 0
    dfs(1, 1, 0)

    print(f'#{tc} {answer}')
