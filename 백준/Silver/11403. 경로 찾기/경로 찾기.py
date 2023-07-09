import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]

def bfs(row):
    queue = deque([row])
    visited = [False] * n

    while queue:
        r = queue.popleft()
        for c in range(n):
            if graph[r][c] == 1 and not visited[c]:
                    visited[c] = True
                    queue.append(c)
                    answer[row][c] = 1

for row in range(n):
    bfs(row)

print('\n'.join([' '.join(map(str, row)) for row in answer]))