import sys
sys.stdin = open('input.txt')


# 중위 순회
def inorder_traverse(node):
    global answer

    if node:
        inorder_traverse(ch1[node])
        answer += words[node]
        inorder_traverse(ch2[node])


for tc in range(1, 11):
    n = int(input())
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)
    words = [''] * (n + 1)
    answer = ''

    # 트리 생성
    for _ in range(n):
        arr = input().split()
        idx = int(arr[0])
        words[idx] = arr[1]

        # 자식 노드가 2개 있을 경우
        if len(arr) == 4:
            left, right = int(arr[2]), int(arr[3])
            ch1[idx] = left
            ch2[idx] = right

        if len(arr) == 3:
            left = int(arr[2])
            ch1[idx] = left

    # 시작 노드를 1로 중위 순회
    inorder_traverse(1)

    print(f'#{tc} {answer}')
