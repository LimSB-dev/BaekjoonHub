import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break


def get_post_order(nodes):
    if not nodes:
        return []

    root = nodes[0]
    left = []
    right = []

    for node in nodes[1:]:
        if node < root:
            left.append(node)
        else:
            right.append(node)

    return get_post_order(left) + get_post_order(right) + [root]


for node in get_post_order(nodes):
    print(node)
