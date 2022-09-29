import sys
sys.stdin = open('input.txt', encoding='utf-8')


def partition(arr, left, right):
    pivot = arr[right]
    i, j = left - 1, left

    while j < right:

        if pivot > arr[j]:
            i += 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quick_sort(arr, left, right):

    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


for tc in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    quick_sort(numbers, 0, len(numbers) - 1)

    print(f'#{tc} {numbers}')
