import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(v):
    if not visited[v]:
        visited[v] = True
        dfs_list.append(v)

        for next_v in graph[v]:
            dfs(next_v)


def bfs(v):
    queue = deque([v])

    while len(queue) != 0:

        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            bfs_list.append(v)

            for next_v in graph[v]:
                queue.append(next_v)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_list = []
bfs_list = []


for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(n+1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(v)
visited = [False] * (n + 1)
bfs(v)


print(*dfs_list)
print(*bfs_list)
