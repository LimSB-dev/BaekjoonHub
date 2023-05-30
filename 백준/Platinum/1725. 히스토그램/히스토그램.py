import sys
input = sys.stdin.readline

N = int(input())
max_area = 0
stack = [0]
numbers = [0] + list(int(input()) for _ in range(N)) + [0]

for i in range(1, N + 2):
    while stack and numbers[stack[-1]] > numbers[i]:
        height = numbers[stack.pop()]
        width = i - stack[-1] - 1
        max_area = max(max_area, height * width)

    stack.append(i)

print(max_area)