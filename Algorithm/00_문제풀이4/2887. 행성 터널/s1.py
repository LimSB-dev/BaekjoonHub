import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])  # 경로 압축(Path compression)
    return parent[node]


def union(a, b):
    a_root, b_root = find_set(a), find_set(b)
    if a_root < b_root:
        parent[b_root] = a_root
    else:
        parent[a_root] = b_root


v = int(input())

x_arr = []
y_arr = []
z_arr = []

for i in range(v):
    x, y, z = map(int, input().split())
    x_arr.append([x, i])
    y_arr.append([y, i])
    z_arr.append([z, i])

x_arr.sort()
y_arr.sort()
z_arr.sort()

# 인접 행성들 사이의 간선
edges = []
for edge in x_arr, y_arr, z_arr:
    for i in range(1, v):
        w1, a = edge[i - 1]
        w2, b = edge[i]
        edges.append((abs(w1 - w2), a, b))

edges.sort()

parent = list(range(v + 1))
counts = 0
cost = 0

for dist, x, y in edges:
    x_root, y_root = find_set(x), find_set(y)
    if x_root != y_root:
        parent[y_root] = x_root
        counts += 1
        cost += dist

        if counts >= v - 1:
            break

print(cost)
