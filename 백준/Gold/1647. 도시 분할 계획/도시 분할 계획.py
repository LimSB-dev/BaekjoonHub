from heapq import heappush, heappop


def prim(start):
    visited = [False] * (v + 1)
    heap = [(0, start)]
    cost = []


    while heap:

        min_dist, min_node = heappop(heap)

        if not visited[min_node]:
            visited[min_node] = True
            cost.append(min_dist)

            for next_node, dist in graph[min_node]:
                if not visited[next_node]:
                    heappush(heap, (dist, next_node))

    return cost


v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

# 인접 행렬 그래프
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

distance = prim(1)
max_path = max(distance)
answer = sum(distance)
answer -= max_path

print(answer)