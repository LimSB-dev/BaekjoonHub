n = int(input())
arr = list(map(int, input().split()))

answer = []
for index, value in enumerate(arr):
    answer.insert(value, index + 1)

print(*answer[::-1])
