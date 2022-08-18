for tc in range(1, 11):
    answer = 0
    n = 8
    m = int(input())
    matrix1 = [list(input()) for _ in range(n)]
    matrix2 = [i for i in zip(*matrix1)]

    for row in range(n):
        row_check = ''
        col_check = ''
        for col in range(n):
            row_check += matrix1[row][col]
            col_check += matrix2[row][col]

            if len(row_check) == m:
                if row_check == row_check[::-1]:
                    answer += 1
                    row_check = row_check[1:]
                else:
                    row_check = row_check[1:]

            if len(col_check) == m:
                if col_check == col_check[::-1]:
                    answer += 1
                    col_check = col_check[1:]
                else:
                    col_check = col_check[1:]

    print(f'#{tc} {answer}')
