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


def find_target(arr, left, right, side):
    global target

    if not arr:
        return

    mid = (left + right) // 2

    target.add(numbers[mid])

    if len(arr) == 1:
        return

    left_arr = numbers[left:mid]
    right_arr = numbers[mid + 1:right + 1]

    if side != 1 and left_arr:
        find_target(left_arr, left, mid - 1, 1)

    if side != 2 and right_arr:
        find_target(right_arr, mid + 1, right, 2)


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    targets = set(map(int, input().split()))
    target = set()

    quick_sort(numbers, 0, n - 1)

    find_target(numbers, 0, n - 1, 0)

    answer = targets & target

    print(f'#{tc} {len(answer)}')
