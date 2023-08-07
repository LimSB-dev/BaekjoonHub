import sys

input = sys.stdin.readline

def dfs(node, distance):
    global max_distance, farthest_node
    visited[node] = True

    if distance > max_distance:
        max_distance = distance
        farthest_node = node

    for v, w in graph[node]:
        if not visited[v]:
            dfs(v, distance + w)

# 입력값 받기
n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n):
    info = list(map(int, input().split()))
    node = info[0]
    for i in range(1, len(info) - 1, 2):
        v, w = info[i], info[i + 1]
        graph[node].append((v, w))

# 첫 번째 DFS를 통해 아무 노드에서 시작해 가장 먼 노드를 찾음
max_distance = 0
farthest_node = 0
dfs(1, 0)

# 두 번째 DFS를 통해 가장 먼 노드로부터 다시 가장 먼 노드를 찾음
# 이것이 트리의 지름이 됨
max_distance = 0
visited = [False] * (n + 1)
dfs(farthest_node, 0)

print(max_distance)
