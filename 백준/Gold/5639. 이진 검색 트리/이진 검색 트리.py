import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def get_postorder(preorder, start, end):
    if start > end:
        return []

    root = preorder[start]
    idx = start + 1

    while idx <= end and preorder[idx] < root:
        idx += 1

    left_subtree = get_postorder(preorder, start + 1, idx - 1)
    right_subtree = get_postorder(preorder, idx, end)

    return [*left_subtree, *right_subtree, root]


preorder_traversal = []

for line in sys.stdin:
    node_value = int(line)
    preorder_traversal.append(node_value)

postorder_traversal = get_postorder(
    preorder_traversal, 0, len(preorder_traversal) - 1)

for node in postorder_traversal:
    print(node)
