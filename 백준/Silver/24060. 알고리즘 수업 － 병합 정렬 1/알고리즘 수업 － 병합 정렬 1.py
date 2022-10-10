def merge(left, right):
    merged_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            answer.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            answer.append(right[j])
            j += 1

    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    answer.extend(left[i:])
    answer.extend(right[j:])

    return merged_arr


def merge_sort(arr):

    length = len(arr)

    if length <= 1:
        return arr

    middle = (length + 1) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = []

merge_sort(numbers)

if k > len(answer):
    print(-1)
else:
    print(answer[k - 1])
