# 시작 노드 / 깊이
def bfs(sv, depth):
    global total
    queue = [(sv, depth)]

    visited[sv] = True

    while queue:
        nr, depth = queue.pop(0)

        for next_v in graph[nr]:

            if not visited[next_v]:

                visited[next_v] = True

                queue.append([next_v, depth + 1])

            total += depth


INF = 999999999

# 노드의 수 / 간선의 수
v, e = map(int, input().split())
graph = [[] for _ in range(v)]

# 케빈 베이컨의 수 리스트
answer = []

# 인접 그래프
for _ in range(e):
    v1, v2 = map(int, input().split())

    v1 -= 1
    v2 -= 1

    # 친구 관계는 양방향
    graph[v1].append(v2)
    graph[v2].append(v1)


for i in range(v):
    visited = [False] * v
    total = 0

    bfs(i, 0)

    answer.append(total)

print(answer.index(min(answer)) + 1)
