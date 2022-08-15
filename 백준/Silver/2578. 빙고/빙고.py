matrix = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]
answer = 0


def check_row(bing_go):
    answer = 0
    for row in range(5):

        if sum(bing_go[row]) == 0:
            answer += 1

    return answer


def check_col(bing_go):
    answer = 0

    for col in range(5):
        sum_value = 0

        for row in range(5):
            sum_value += bing_go[row][col]

        if sum_value == 0:
            answer += 1

    return answer


def check_x(bing_go):
    answer = 0
    slash = 0
    back_slash = 0

    for i in range(5):
        slash += bing_go[i][i]
        back_slash += bing_go[i][4 - i]

    if slash == 0:
        answer += 1
    if back_slash == 0:
        answer += 1
    return answer


cnt = 0
for row in range(5):
    for col in range(5):
        cnt += 1
        call_num = call[row][col]

        for i in range(5):
            for j in range(5):
                if matrix[i][j] == call_num:
                    matrix[i][j] = 0
                    break

        row_cnt = check_row(matrix)
        col_cnt = check_col(matrix)
        x_cnt = check_x(matrix)

        if row_cnt + col_cnt + x_cnt >= 3:
            answer = cnt
            break

    if answer != 0:
        break

print(answer)
