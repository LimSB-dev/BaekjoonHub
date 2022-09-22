from collections import deque


# bfs
def bfs(node):
    global nodes

    queue = deque([[graph[node], node]])
    visited[node] = True

    while queue:

        next_nodes, node = queue.popleft()

        for next_node in next_nodes:
            if not visited[next_node]:
                visited[next_node] = True
                nodes[next_node] = node

                queue.append([graph[next_node], next_node])


n = int(input())
graph = [[] for _ in range(n + 1)]

# 인접 행렬 그래프
for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

nodes = [0] * (n + 1)
visited = [False] * (n + 1)
bfs(1)

answer = []

for i in range(2, n + 1):
    answer.append(nodes[i])

print(*answer, sep='\n')
