for tc in range(1, int(input()) + 1):
    matrix = [list(map(str, input().strip())) for _ in range(8)]
    answer = 'yes'

    rook = 0
    col_check = [0] * 8
    for row in range(8):
        row_check = 0
        for col in range(8):

            if matrix[row][col] == 'O':
                rook += 1
                row_check += 1

                if row_check > 1:
                    answer = 'no'

                col_check[col] += 1

                if col_check[col] > 1:
                    answer = 'no'

    if rook != 8:
        answer = 'no'

    print(f'#{tc} {answer}')
