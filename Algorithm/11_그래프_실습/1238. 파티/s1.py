import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dijkstra(start):
    visited = [False] * (n + 1)
    visited[start] = True
    times[start] = 0

    for end, time in graph[start]:
        times[end] = time

    for _ in range(n - 1):
        min_time = INF

        # 최단 시간이 확정되지 않은 정점들 중 최단 시간이 가장 짧은 정점 선택
        for i in range(1, n + 1):
            if not visited[i] and min_time > times[i]:
                min_node = i
                min_time = times[i]

        visited[min_node] = True

        for next_node, time in graph[min_node]:
            new_time = times[min_node] + time
            if new_time < times[next_node]:
                times[next_node] = new_time


INF = 999999999
n, m, x = map(int, input().split())
times = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

dijkstra(x)
print(times)

print(max(times[1:]))