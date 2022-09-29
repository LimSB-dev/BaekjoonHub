import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    if node != parents[node]:
        parents[node] = find_set(parents[node])
    return parents[node]


n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
answer = 0

# 비용을 기준으로 오름차순
edges.sort(key=lambda x: x[2])

parents = list(range(n + 1))
cnt = 0
cost = 0

for v1, v2, fee in edges:
    v1_root, v2_root = find_set(v1), find_set(v2)

    if v1_root != v2_root:
        parents[v2_root] = v1_root
        cost += fee
        cnt += 1

        if cnt >= n - 1:
            break

print(cost)
