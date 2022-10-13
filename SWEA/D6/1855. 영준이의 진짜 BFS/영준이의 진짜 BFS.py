from collections import deque


def lca(v1, v2):
    global answer

    while deep[v1] != deep[v2]:
        answer += 1
        if deep[v1] > deep[v2]:
            v1 = parent[v1]
        else:
            v2 = parent[v2]

    while v1 != v2:
        answer += 2
        v1 = parent[v1]
        v2 = parent[v2]


def bfs(start):
    global answer

    queue = deque([start])
    now = start

    while queue:
        min_node = queue.popleft()

        for next_node in graph[min_node]:

            lca(now, next_node)

            now = next_node

            queue.append(next_node)


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0

    parent = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for i in range(n - 1):

        parent[i + 2] += arr[i]

        graph[arr[i]].append(i + 2)

    deep = [0] * (n + 1)

    # 깊이 구하기
    for i in range(2, n + 1):
        if parent[i] == 1:
            deep[i] = 1
        else:
            deep[i] += deep[parent[i]] + 1

    bfs(1)

    print(f'#{tc} {answer}')
