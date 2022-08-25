# BOJ 2606. 바이러스
# https://www.acmicpc.net/problem/2606

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = [start]
    total = 0  # 결과 값 (감염된 컴퓨터의 개수)

    # 큐가 빌 때까지 탐색
    while queue:
        node = queue.pop(0)  # 현재 정점
        for next_node in graph[node]:  # 인접한 모든 정점에 대해
            if not visited[next_node]:  # 아직 방문하지 않았다면
                visited[next_node] = True  # 방문처리
                queue.append(next_node)  # 인접 정점을 큐에 넣음
                total += 1  # 감염 + 1

    return total


n = int(input())  # 정점(컴퓨터) 개수
m = int(input())  # 간선(네트워크 연결) 개수
graph = [[] for _ in range(n + 1)]

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))  # 1번 컴퓨터에서 시작