t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    # 버블 탐색
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'#{tc}', end=' ')
    print(*arr)