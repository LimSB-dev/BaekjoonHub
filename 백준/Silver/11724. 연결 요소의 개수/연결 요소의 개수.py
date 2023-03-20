import sys
# sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 해제
input = sys.stdin.readline


def dfs(v):
    visited[v] = True
    for edge in graph[v]:
        if not visited[edge]:
            dfs(edge)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

print(answer)
