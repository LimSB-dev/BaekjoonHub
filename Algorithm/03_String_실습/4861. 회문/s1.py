import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    n, m = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(n)]

    for row in range(n):
        row_check = ''
        col_check = ''
        for col in range(n):
            row_check += matrix[row][col]
            col_check += matrix[col][row]

            if len(row_check) == m:
                if row_check == row_check[::-1]:
                    answer = row_check
                    break
                else:
                    row_check = row_check[1:]

            if len(col_check) == m:
                if col_check == col_check[::-1]:
                    answer = col_check
                    break
                else:
                    col_check = col_check[1:]

        if answer != 0:
            break

    print(f'#{tc} {answer}')
