import sys
sys.stdin = open('input.txt')
from collections import deque



def bfs(node):

    answer.append(node)

    # 방문 처리
    visited[node] = True

    # queue 생성
    queue = deque([graph[node]])

    # bfs 탐색
    while queue:

        # dequeue
        next_nodes = queue.popleft()

        # 탐색
        for next_node in next_nodes:

            # 방문 확인
            if not visited[next_node]:

                # 방문 처리
                visited[next_node] = True

                # 방문 리스트 추가
                answer.append(next_node)

                # enqueue
                queue.append(graph[next_node])


numbers = list(map(int, input().split()))
M = max(numbers)
answer = []
graph = [[] for _ in range(M + 1)]
visited = [False] * (M + 1)

# 인접 그래프 생성
for i in range(0, len(numbers), 2):
    v1, v2 = numbers[i], numbers[i + 1]

    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)

print(*answer)
