import sys
sys.stdin = open('input.txt', encoding='utf-8')


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    merged_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    mid = len(arr) // 2

    if mid == 0:
        return arr

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


for tc in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0

    numbers = merge_sort(numbers)

    print(f'#{tc} {numbers[n // 2]} {cnt}')
