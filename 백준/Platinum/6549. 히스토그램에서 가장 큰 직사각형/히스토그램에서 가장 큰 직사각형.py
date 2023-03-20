from sys import stdin

input = stdin.readline

while True:
    n, *numbers = list(map(int, input().split()))

    if n == 0:
        break

    stack = [0]
    max_value = 0

    numbers.insert(0, 0)
    numbers.append(0)

    for i in range(1, n + 2):

        while stack and numbers[stack[-1]] > numbers[i]:
            idx = stack.pop()
            max_value = max(max_value, (i - 1 - stack[-1]) * numbers[idx])

        stack.append(i)

    print(max_value)
