import sys
sys.stdin = open('input.txt')


def dfs(node):
    answer.append(node)
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(i)


numbers = list(map(int, input().split()))
M = max(numbers)
answer = []
graph = [[] for _ in range(M + 1)]
visited = [False] * (M + 1)

for i in range(0, len(numbers), 2):
    v1, v2 = numbers[i], numbers[i + 1]

    # 양 방향 인접 그래프
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)

print(*answer)
