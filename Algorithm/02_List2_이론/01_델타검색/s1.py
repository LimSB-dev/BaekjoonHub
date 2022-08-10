import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(5)]

    for row in range(n):
        for col in range(n):
            # 가로 덧셈
            # list out of range
            if col != 4:
                row_value = matrix[row][col] - matrix[row][col+1]
                # 절대값 혹은 abs() 사용
                if row_value < 0:
                    row_value *= -1
                answer += row_value

            # 세로 덧셈
            # list out of range
            if row != 4:
                col_value = matrix[row][col] - matrix[row+1][col]
                # 절대값 혹은 abs() 사용
                if col_value < 0:
                    col_value *= -1
                answer += col_value

    print(f'#{tc} {answer*2}')
