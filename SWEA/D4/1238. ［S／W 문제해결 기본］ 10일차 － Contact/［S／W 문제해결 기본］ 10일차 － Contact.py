from collections import deque


def bfs(v, cnt):
    global calls, last_call
    # 큐 생성
    queue = deque([[graphs[v], cnt]])

    # 방문처리
    visited[v] = True

    # 큐가 빌 때까지
    while queue:

        # dequeue
        graph, cnt = queue.popleft()

        for next_v in graph:

            # 방문 기록 없을 경우
            if not visited[next_v] and next_v:


                # 종료조건
                if last_call <= cnt:
                    if last_call == cnt:
                        calls.append(next_v)
                    else:
                        last_call = cnt
                        calls = [next_v]

                visited[next_v] = True

                # enqueue
                queue.append([graphs[next_v], cnt + 1])


for tc in range(1, 11):
    n, start = map(int, input().split())
    arr = list(map(int, input().split()))
    graphs = [[] for _ in range(101)]
    visited = [False] * 101
    calls = []
    last_call = 0

    # 인접그래프 생성
    for i in range(n // 2):
        i *= 2
        v1, v2 = arr[i], arr[i + 1]

        # 단방향 그래프
        graphs[v1].append(v2)

    bfs(start, 1)

    answer = max(calls)

    print(f'#{tc} {answer}')
