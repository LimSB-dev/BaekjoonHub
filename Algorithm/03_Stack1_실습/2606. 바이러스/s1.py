import sys
sys.stdin = open('input.txt')


def dfs(v):
    visited[v] = True  # 현재 정점 방문처리

    for next_v in graph[v]:
        if not visited[next_v]:  # 방문하지 않았다면
            global total
            total += 1  # 감염 컴퓨터 1개 증가
            dfs(next_v)  # 인접 정점으로 이동


n = int(input())  # 정점 개수
m = int(input())  # 간선 개수
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
total = 0  # 결과 값 (감염된 컴퓨터의 개수)

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)  # 1번 정점에서 시작
print(total)
