import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        init(node * 2, start, mid)
        init(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)


n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - nums[b - 1]
        nums[b - 1] = c
        update(1, 0, n - 1, b - 1, diff)
    else:
        print(query(1, 0, n - 1, b - 1, c - 1))
