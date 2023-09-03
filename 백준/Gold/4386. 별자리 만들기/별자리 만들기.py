import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(float, input().split())) for _ in range(n)]
answer = 0

# 최소 스패닝 트리
# 크루스칼 알고리즘


def get_distance(x1, y1, x2, y2):
    """_summary_

    두 점 사이의 거리를 구하는 함수로 소수점 두자리까지 구한다.
    """
    return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)


def find_parent(parent, x):
    """_summary_

    부모 노드를 찾는 함수
    """
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    """_summary_

    두 노드를 합치는 함수
    """
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


# 간선 정보를 담을 리스트
edges = []
# 부모 노드를 담을 리스트
parent = [0] * n

# 부모 노드 초기화
for i in range(n):
    parent[i] = i

# 간선 정보 초기화
for i in range(n):
    for j in range(i + 1, n):
        distance = get_distance(graph[i][0], graph[i][1],
                                graph[j][0], graph[j][1])
        edges.append((distance, i, j))

# 간선을 거리를 기준으로 오름차순 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    distance, x, y = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        answer += distance

print(answer)
