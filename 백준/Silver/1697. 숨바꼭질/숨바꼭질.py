import sys
from collections import deque
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def operate(i, n):
    if i == 0:
        return n * 2
    if i == 1:
        return n + 1
    if i == 2:
        return n - 1


def bfs(n):
    global m
    queue = deque([[n, 0]])

    while queue:

        n, time = queue.popleft()

        if n == m:
            return time

        for i in range(3):
            next_n = operate(i, n)

            if not (0 <= next_n < 200001):
                continue

            if not arr[next_n]:
                arr[next_n] = time

                queue.append([next_n, time + 1])


n, m = map(int, input().split())
arr = [False] * 200001

print(bfs(n))
