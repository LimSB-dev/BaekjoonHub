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


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())

INF = 999999999
for i in range(3):
    distance = [INF] * (v + 1)
    if i == 0:
        dijkstra(1)
        one_v1 = distance[v1]
        one_v2 = distance[v2]
    elif i == 1:
        dijkstra(v1)
        v1_v2 = distance[v2]
        v1_n = distance[v]
    else:
        dijkstra(v2)
        v2_v1 = distance[v1]
        v2_n = distance[v]

answer = min((one_v1 + v1_v2 + v2_n), (one_v2 + v2_v1 + v1_n))

if answer >= INF:
    answer = -1

print(answer)
