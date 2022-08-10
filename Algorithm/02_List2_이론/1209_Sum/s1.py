import sys
sys.stdin = open('input.txt')

for _ in range(10):
    answer = 0
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    # 가장 큰 합을 담을 변수
    max_sum_value = 0

    # / 대각선의 합을 담을 변수
    sum_slash = 0
    # \ 대각선의 합을 담을 변수
    sum_back_slash = 0

    # 반복문으로 /,\ 속의 값을 다 덧셈
    for i in range(100):
        sum_slash += matrix[i][i]
        sum_back_slash += matrix[99 - i][99 - i]

    # 최대값과 대소 비교 후 대입
    if max_sum_value < sum_slash:
        max_sum_value = sum_slash
    if max_sum_value < sum_back_slash:
        max_sum_value = sum_back_slash

    # 반복문으로 가로 세로의 값을 다 덧셈
    for row in range(100):
        sum_row = 0
        sum_col = 0
        for col in range(100):
            sum_row += matrix[row][col]
            sum_col += matrix[col][row]

        # 최대값과 대소 비교 후 대입
        if max_sum_value < sum_row:
            max_sum_value = sum_row
        if max_sum_value < sum_col:
            max_sum_value = sum_col

    print(f'#{tc} {max_sum_value}')
