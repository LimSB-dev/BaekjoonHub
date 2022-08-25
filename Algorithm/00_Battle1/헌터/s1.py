import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt, visited):
    global answer


    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:

            # 방문 처리
            visited[nr][nc] = True

            # 모든 몬스터를 잡고 고객을 방문했을 경우
            if visited == [True] * monster_cnt:
                if answer > cnt:
                    answer = cnt
                return





INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())    # 맵의 크기
    field = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    monster = []
    client = []

    # 총 몬스터의 수
    monster_cnt = 0

    for row in range(n):
        for col in range(n):

            value = field[row][col]    # 종류

            # 몬스터
            if value > 0:
                monster.append([row, col, value])
                monster_cnt += 1
            # 고객
            elif value < 0:
                client.append([row, col, value])

            # 최대 몬스터 수
            if monster_cnt == 4:
                break

        if monster_cnt == 4:
            break

    # 몬스터 방문 정보
    visit_client = [False] * monster_cnt

    # 몬스터의 좌표 / 오름차순
    # 고객의 좌표 / 내림차순 정렬
    monster = sorted(monster, key=lambda x: x[2])
    client = sorted(client, key=lambda x: x[2], reverse=True)

    answer = INF  # 최단 거리

    # 사냥꾼의 시작 위치: 1, 1
    # 현재 거리: 0
    # 방문 정보
    dfs(0, 0, 0, visited)

    print(f'#{tc} {answer}')
