import sys
sys.stdin = open('input.txt', encoding='utf-8')
from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:

        min_dist, min_node = heappop(heap)

        if min_dist <= distance[min_node]:

            for next_node, dist in graph[min_node]:
                new_dist = min_dist + dist
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    heappush(heap, (new_dist, next_node))


v, e, k = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

INF = 999999999

distance = [INF] * (v + 1)
dijkstra(1)

for i in range(1, v + 1):
    print(distance[i])