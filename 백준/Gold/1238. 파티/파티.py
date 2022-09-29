from heapq import heappush, heappop


def dijkstra(start):
    times[start] = 0
    heap = [(0, start)]

    while heap:
        # 1. 시간이 최단 시간이 되는 정점 선택
        min_time, min_node = heappop(heap)

        # 2. 이미 최단 시간으로 기록되어 있는 값보다 짧을 경우
        if min_time <= times[min_node]:

            for next_node, time in graph[min_node]:
                new_time = min_time + time
                if new_time < times[next_node]:
                    times[next_node] = new_time
                    heappush(heap, (new_time, next_node))


INF = 999999999
n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

answer = [0] * (n + 1)

for i in range(1, n + 1):
    times = [INF] * (n + 1)
    dijkstra(i)
    if i == x:
        answer = [x + y for x, y in zip(answer, times)]
    else:
        answer[i] += times[x]

print(max(answer[1:]))
