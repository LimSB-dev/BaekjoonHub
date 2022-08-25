import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(v, edge):
    global answer

    queue = [(v, edge)]
    visited[v] = True

    # queue가 빈 리스트가 될 때까지 반복
    while queue:
        nv, depth = queue.pop(0)

        for next_v in graph[nv]:

            # 가지치기
            if answer <= depth:
                return

            # 종료 조건
            if next_v == end:

                # 대소 비교
                if answer > depth:
                    answer = depth
                return

            if not visited[next_v]:

                # 방문 처리
                visited[next_v] = True

                queue.append((next_v, depth + 1))


INF = 999999999

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    # 최소 간선의 수
    answer = INF

    # 간선의 수
    edge = 1

    # 인접 그래프
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    start, end = map(int, input().split())

    # 출발 노드, 간선의 수
    bfs(start, edge)

    if answer == INF:
        answer = 0

    print(f'#{tc} {answer}')
