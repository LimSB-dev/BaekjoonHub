import sys
sys.stdin = open('input.txt', encoding='utf-8')


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:

        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


for tc in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    quick_sort(numbers, 0, n - 1)

    print(f'#{tc} {numbers[n // 2]}')
