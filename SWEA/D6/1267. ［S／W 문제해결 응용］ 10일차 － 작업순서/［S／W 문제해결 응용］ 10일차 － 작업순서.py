for tc in range(1, 11):
    answer = []
    # 정점의 개수 / 간선의 개수
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    arr = list(map(int, input().split()))

    # 인접 리스트
    for i in range(e):
        graph[arr[(i * 2) + 1] - 1].append(arr[i * 2])

    for _ in range(v + 1):
        for idx, value in enumerate(graph):
            if not value:
                answer.append(idx + 1)
                graph[idx] = [v + 1]
            else:
                for i in value:
                    if i in answer:
                        value.remove(i)

    print(f'#{tc}', *answer)
