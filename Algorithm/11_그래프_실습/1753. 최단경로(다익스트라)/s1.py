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
k = int(input())

INF = 999999999
distance = [INF] * (v + 1)

# 인접 행렬 그래프
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

dijkstra(k)

answer = []

for idx in range(1, v + 1):
    if distance[idx] == INF:
        answer.append('INF')
    else:
        answer.append(distance[idx])

print(*answer, sep='\n')
