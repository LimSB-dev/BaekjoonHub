import sys
sys.stdin = open('input.txt')


def selection_sort(i):

    if i == len(arr) - 1:
        return

    min_index = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    selection_sort(i + 1)


def baby_gin():
    global arr, answer
    if len(arr) >= 3:

        a, b, c = arr[0], arr[1], arr[2]

        if a == b and b == c:
            arr = arr[3:]
            baby_gin()
        elif a + 1 == b and b + 1 == c:
            arr = arr[3:]
            baby_gin()


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().strip()))
    selection_sort(0)
    answer = True
    baby_gin()
    if arr:
        answer = False

    print(answer)
