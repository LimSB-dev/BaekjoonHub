t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    print(f'#{tc}')
    li = []

    for row in range(n):
        li.append([0] * (row + 1))
        for col in range(row + 1):
            if col == 0:
                li[row][col] = 1
            elif col == row:
                li[row][col] = 1
            else:
                li[row][col] = li[row - 1][col-1] + li[row - 1][col]

    for i in range(n):
        print(*li[i])