import sys
from collections import deque
sys.stdin = open('input.txt')


# 전위순회
def preorder(node):
    if node:
        print(node, end=' ')
        preorder(ch1[node])
        preorder(ch2[node])


n = int(input())
arr = deque(map(int, input().split()))

# 이진 트리의 저장

# 1. 부모 번호를 인덱스로 자식 번호를 저장
ch1 = [0] * (n + 1)
ch2 = [0] * (n + 1)

while arr:
    v1, v2 = arr.popleft(), arr.popleft()

    if ch1[v1] == 0:
        ch1[v1] = v2
    else:
        ch2[v1] = v2

preorder(1)