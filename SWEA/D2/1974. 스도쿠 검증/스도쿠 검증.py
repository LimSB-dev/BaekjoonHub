t = int(input())

for tc in range(1, t + 1):
    answer = 1
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # check row & column
    for row in range(9):
        count_row = [0] * 10
        count_col = [0] * 10
        for col in range(9):
            count_row[sudoku[row][col]] += 1
            count_col[sudoku[col][row]] += 1

        for i in range(1, 10):
            if count_row[i] == 0 or count_col[i] == 0:
                answer = 0
                break

    # check 3 X 3 box
    for row in range(3):
        for col in range(3):
            count_box = [0] * 10
            for i in range(3):
                for j in range(3):
                    count_box[sudoku[(3 * row) + i][(3 * col) + j]] += 1

            for k in range(1, 10):
                if count_box[k] == 0:
                    answer = 0
                    break

    print(f'#{tc} {answer}')