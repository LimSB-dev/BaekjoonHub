t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = [[1] * (i + 1) for i in range(n)]

    for row in range(2, n):
        for col in range(1, row):
            arr[row][col] = arr[row - 1][col - 1] + arr[row - 1][col]

    print(f'#{tc}')
    for i in range(n):
        print(*arr[i])