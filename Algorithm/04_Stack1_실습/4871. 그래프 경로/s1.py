import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


for tc in range(1, int(input()) + 1):
    # 노드의 수 / 간선의 수
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    answer = 0
    for i in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    start, end = map(int, input().split())

    dfs(start)

    if visited[end]:
        answer = 1

    print(f'#{tc} {answer}')
