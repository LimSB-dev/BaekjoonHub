def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        # 방문하지 않았을 경우
        if not visited[next_v]:
            dfs(next_v)


for _ in range(10):
    tc, e = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [False] * 100
    answer = 0

    # 인접 리스트 생성
    for i in range(0, e * 2, 2):
        graph[arr[i]].append(arr[i + 1])

    # 출발 지점 0
    dfs(0)

    if visited[99]:
        answer = 1

    print(f'#{tc} {answer}')
