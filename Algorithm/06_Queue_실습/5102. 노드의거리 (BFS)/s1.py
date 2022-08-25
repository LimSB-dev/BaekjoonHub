import sys
sys.stdin = open('input.txt')


# now node / end node
def dfs(nv, ev, edge):
    global answer

    for next_v in graph[nv]:

        # 도착 노드와 연결 시
        # 대소 비교 후 종료
        if next_v == ev:
            edge += 1
            if answer > edge:
                answer = edge
            return

        # 방문 기록이 없다면 탐색
        if not visited[next_v]:

            edge += 1

            # 가지치기
            if answer <= edge:
                return

            # 방문 처리
            visited[next_v] = True

            dfs(next_v, ev, edge)

            # 가지치기 혹은 노드의 끝까지 가고 돌아오는 경우
            edge -= 1
            visited[next_v] = False


INF = 999999999

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    queue = []

    # 최소 간선의 수
    answer = INF

    # 간선의 수
    edge = 0

    # 인접 그래프
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    start, end = map(int, input().split())

    # 출발 노드, 도착 노드
    dfs(start, end, edge)

    if answer == INF:
        answer = 0

    print(f'#{tc} {answer}')
