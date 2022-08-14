n = int(input())
arr = list(map(int, input().split()))

# 최대 오름차순, 내림차순
max_ascending = 0
max_descending = 0

# 오름차순, 내림차순
ascending = 1
descending = 1
if n == 1:
    answer = 1
else:
    for i in range(n - 1):

        # 오름차순 개수 카운트
        if arr[i] <= arr[i + 1]:
            ascending += 1
        else:
            ascending = 1

        # 내림차순 개수 카운트
        if arr[i] >= arr[i + 1]:
            descending += 1
        else:
            descending = 1

        # 오름차순, 내림차순 최대 연속 횟수 최대값 비교
        if max_ascending < ascending:
            max_ascending = ascending

        if max_descending < descending:
            max_descending = descending

    answer = max(max_ascending, max_descending)

print(answer)
