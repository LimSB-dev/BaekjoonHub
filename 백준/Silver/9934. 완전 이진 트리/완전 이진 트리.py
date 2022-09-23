from collections import deque


def bfs(tree, depth):
    global answer

    queue = deque([[tree, depth]])

    while queue:

        # dequeue
        sub_tree, depth = queue.popleft()

        # 중앙값
        m = len(sub_tree) // 2

        # 노드 입력
        answer[depth].append(sub_tree[m])

        ch1 = sub_tree[:m]
        ch2 = sub_tree[-m:]

        if len(sub_tree) > 1:
            queue.append([ch1, depth + 1])
            queue.append([ch2, depth + 1])


k = int(input())
array = list(map(int, input().split()))
answer = [[] for _ in range(k)]

bfs(array, 0)

for i in range(k):
    print(*answer[i])
