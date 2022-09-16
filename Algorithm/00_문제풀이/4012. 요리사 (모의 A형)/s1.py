# 루트 노드 찾기
def find_root(n):
    for node in range(1, n + 1):
        if tree[node][2] == 0:  # 부모 노드가 없으면 루트 노드
            return node


# 전위 순회 (V -> L -> R)
def pre_order(node):
    if node != 0:
        print(node, end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


# 중위 순회 (L -> V -> R)
def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(node, end=' ')
        in_order(tree[node][1])


# 후위 순회 (L -> R -> V)
def post_order(node):
    if node != 0:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(node, end=' ')


v = int(input())  # 정점 개수
tree = [[0] * 3 for _ in range(v + 1)]  # [왼쪽자식, 오른쪽자식, 부모]
edges = list(map(int, input().split()))

# 이진 트리 구현
for i in range(0, len(edges), 2):
    parent, child = edges[i], edges[i + 1]

    if tree[parent][0] == 0:
        tree[parent][0] = child  # 왼쪽 자식 노드 삽입
    else:
        tree[parent][1] = child  # 오른쪽 자식 노드 삽입

    tree[child][2] = parent  # 부모 노드 삽입

root = find_root(v)  # 루트 노드 찾기

print(tree)
print('-------------')

print('전위 순회 : ', end='')
pre_order(root)
print()

print('중위 순회 : ', end='')
in_order(root)
print()

print('후위 순회 : ', end='')
post_order(root)
print()


"""
이진 트리 구현 방법은 아래와 같습니다.

                1          2          3      ...
[[0, 0, 0], [2, 3, 0], [4, 0, 1], [5, 6, 1], ...]

1번 노드
- 왼쪽: 2번
- 오른쪽: 3번
- 부모: 없음

2번 노드
- 왼쪽: 4번
- 오른쪽: 없음
- 부모: 1번

3번 노드
- 왼쪽: 5번
- 오른쪽: 6번
- 부모: 1번
"""