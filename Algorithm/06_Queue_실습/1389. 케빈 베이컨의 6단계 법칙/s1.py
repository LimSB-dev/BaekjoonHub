import sys
sys.stdin = open('input.txt')


# 시작 노드 / 깊이
def bfs(sv):
    global length , length

    queue = [sv]

    visited[sv] = True

    while queue:
        nr = queue.pop(0)

        for next_v in graph[nr]:

            next_v -= 1

            length += 1

            visited[next_v] = True

            queue.append(next_v)
    return


INF = 999999999

# 노드의 수 / 간선의 수
v, e = map(int, input().split())
graph = [[] for _ in range(v)]
visited = [False] * (v)

# 케빈 베이컨의 수 최댓값
answer = 0

# 인접 그래프
for _ in range(e):
    v1, v2 = map(int, input().split())

    v1 -= 1
    v2 -= 1

    # 친구 관계는 양방향
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(v):
    length = 0

    bfs(i)

    answer.append(length)

print(answer.index(max(answer)) + 1)
