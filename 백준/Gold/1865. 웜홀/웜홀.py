import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    def bellman_ford():
        dist = [10001] * (n + 1)
        dist[1] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                for next_node, next_cost in graph[j]:
                    if dist[next_node] > dist[j] + next_cost:
                        dist[next_node] = dist[j] + next_cost
                        if i == n:
                            return True
        return False

    if bellman_ford():
        print('YES')
    else:
        print('NO')
