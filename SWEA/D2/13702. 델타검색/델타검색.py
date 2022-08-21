dr = [-1, 1, 0, 0]
dc = dr[::-1]


def make_abs(row, col):
    sum_value = 0
    for direction in range(4):
        nrow = row + dr[direction]
        ncol = col + dc[direction]
        if 0 <= nrow < n and 0 <= ncol < n:
            value = matrix[row][col] - matrix[nrow][ncol]
            if value >= 0:
                sum_value += value
            else:
                sum_value -= value
    return sum_value


for tc in range(1, 11):
    answer = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for row in range(n):
        for col in range(n):
            answer += make_abs(row, col)

    print(f'#{tc} {answer}')
