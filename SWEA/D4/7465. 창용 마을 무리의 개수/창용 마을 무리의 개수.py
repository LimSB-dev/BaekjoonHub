def dfs(num):
    visited[num] = True
    for next_v in graph[num]:
        # 방문한 적이 없는 경우
        if not visited[next_v]:
            dfs(next_v)


for tc in range(1, int(input()) + 1):
    # 정접의 개수, 간선의 개수
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    # 무리 수
    total = 0

    # 인접 리스트
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, n + 1):
        if not visited[i]:
            total += 1
            dfs(i)

    print(f'#{tc} {total}')