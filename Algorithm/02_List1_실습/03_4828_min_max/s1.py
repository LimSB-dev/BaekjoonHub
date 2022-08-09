t = int(input())

for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[0]
    min_value = arr[0]

    for i in range(1, n):

        if arr[i] > max_value:
            max_value = arr[i]

        elif arr[i] < min_value:
            min_value = arr[i]

    answer = max_value - min_value

    print(f'#{tc} {answer}')
