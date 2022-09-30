import sys
sys.stdin = open('input.txt', encoding='utf-8')
from collections import deque


def bfs(start, end):
    global answer

    queue = deque([[0, start]])

    while queue and len(answer) <= k:

        min_dist, min_node = queue.popleft()

        if min_node == end:
            answer.add(min_dist)

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            queue.append([new_dist, next_node])


v, e, k = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[b].append([a, c])

for i in range(1, v + 1):
    answer = set()
    bfs(i, 1)

    if len(answer) <= k:
        answer = -1
    else:
        answer = list(answer)
        answer.sort()
        answer = answer[k - 1]

    print(answer)
