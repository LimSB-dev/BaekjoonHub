import sys
input = sys.stdin.readline

def dfs(delete_node):
    tree[delete_node] = -2
    for node in range(n):
        if delete_node == tree[node]:
            dfs(node)

n = int(input())
tree = list(map(int, input().split()))
delete_node = int(input())
leaf = 0

dfs(delete_node)

for node in range(n):
    if tree[node] != -2 and node not in tree:
        leaf += 1

print(leaf)