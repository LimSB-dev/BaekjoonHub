import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(x, y):
    x_root, y_root = find_set(x), find_set(y)
    if x_root < y_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    parent = list(range(n + 1))

    for i in range(0, m * 2, 2):
        v1, v2 = numbers[i], numbers[i + 1]
        union(v1, v2)

    answer = set()

    for i in range(1, n + 1):
        answer.add(find_set(i))

    print(f'#{tc} {len(answer)}')