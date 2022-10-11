def init(node, start, end):
    if start == end:
        tree[node] = 1
        return

    middle = (start + end) // 2

    init(2 * node, start, middle)
    init(2 * node + 1, middle + 1, end)

    tree[node] = tree[2 * node] + tree[2 * node + 1]


def query(node, start, end, order):
    tree[node] -= 1

    if start == end:
        return start

    middle = (start + end) // 2

    if tree[2 * node] >= order:
        return query(2 * node, start, middle, order)
    else:
        return query(2 * node + 1, middle + 1, end, order - tree[2 * node])


n, k = map(int, input().split())
tree = [0] * 4 * n
order = k
init(1, 1, n)

print('<', end='')

for _ in range(1, n):
    print(query(1, 1, n, order), end=', ')
    order += k - 1
    order = (order - 1) % tree[1] + 1

print(query(1, 1, n, order), end='>')
