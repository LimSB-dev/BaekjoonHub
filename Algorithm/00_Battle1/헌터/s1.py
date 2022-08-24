import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, cnt, visited):
    global answer

    if visited == [True] * monster_cnt:
        if answer > cnt:
            answer = cnt
        return

    for i in range(monster_cnt):

        # 방문 기록이 없는 경우
        if not visited[i]:
            visited[i] = True
            mr, mc = monster[i][0], monster[i][1]    # 몬스터 좌표
            cr, cc = client[i][0], client[i][1]    # 고객 좌표

            # 사냥꾼 위치에서 몬스터한테 가는 거리
            cnt += abs(r - mr) + abs(c - mc)

            # 몬스터 위치에서 고개한테 가는 거리
            cnt += abs(mr - cr) + abs(mc - cc)

            # 가지치기
            if answer <= cnt:
                return

            # 사냥꾼의 위치 갱신
            dfs(cr, cc, cnt, visited)

            # 가지치기 되거나 재귀함수 끝에서 돌아온 경우
            visited[i] = False
            cnt -= abs(r - mr) + abs(c - mc)
            cnt -= abs(mr - cr) + abs(mc - cc)


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())    # 맵의 크기
    field = [list(map(int, input().split())) for _ in range(n)]

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

            if monster_cnt == 4:
                break

        if monster_cnt == 4:
            break

    visited = [False] * monster_cnt

    # 몬스터의 좌표 / 고객의 좌표, 오름차순 / 내림차순 정렬
    monster = sorted(monster, key=lambda x: x[2])
    client = sorted(client, key=lambda x: x[2], reverse=True)

    answer = INF  # 최단 거리

    # 사냥꾼의 시작 위치: 1, 1
    # 현재 거리: 0
    dfs(0, 0, 0, visited)

    print(f'#{tc} {answer}')
