import sys
sys.stdin = open('input.txt', encoding='utf-8')
from heapq import heappush, heappop


def prim(start):
    visited = [False] * (v + 1)
    heap = [(0, start)]
    cost = 0

    while heap:

        # 가장 적은 비용으로 이동 가능한 정점 찾기
        min_dist, min_node = heappop(heap)

        if not visited[min_node]:

            # 방문 처리
            visited[min_node] = True

            cost += min_dist

            # 해당 정점과 인접한 정점에 대해 heappush
            for next_node, dist in graph[min_node]:
                if not visited[next_node]:
                    heappush(heap, (dist, next_node))

    return cost


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]

    for _ in range(e):
        v1, v2, w = map(int, input().split())
        graph[v1].append([v2, w])
        graph[v2].append([v1, w])

    print(f'#{tc} {prim(0)}')
