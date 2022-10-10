n = int(input())
numbers = list(map(int, input().split()))

dp_left = [1] * n
dp_right = [1] * n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:

            if dp_left[j] + 1 > dp_left[i]:
                dp_left[i] = dp_left[j] + 1

        if numbers[n - 1 - i] > numbers[n - 1 - j]:

            if dp_right[n - 1 - j] + 1 > dp_right[n - 1 - i]:
                dp_right[n - 1 - i] = dp_right[n - 1 - j] + 1

answer = [x + y for x, y in zip(dp_left, dp_right)]

print(max(answer) - 1)
