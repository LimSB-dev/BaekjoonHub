import sys
sys.stdin = open('input.txt')


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    for row in range(n):
        for col in range(n):
            r_value = 999999999
            c_value = 999999999
            if row != 0:
                r_value = matrix[row - 1][col]
            if col != 0:
                c_value = matrix[row][col - 1]

            value = min(r_value, c_value)

            if value != 999999999:
                matrix[row][col] += value

    answer = matrix[n - 1][n - 1]

    print(f'#{tc} {answer}')