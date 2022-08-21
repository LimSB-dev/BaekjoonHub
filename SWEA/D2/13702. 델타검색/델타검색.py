for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    for y in range(n):
        for x in range(n):
            # 가로 덧셈
            # list out of range
            if x != n - 1:
                y_value = matrix[y][x] - matrix[y][x + 1]
                # 절대값 혹은 abs() 사용
                if y_value < 0:
                    y_value *= -1
                answer += y_value

            # 세로 덧셈
            # list out of range
            if y != n - 1:
                x_value = matrix[y][x] - matrix[y + 1][x]
                # 절대값 혹은 abs() 사용
                if x_value < 0:
                    x_value *= -1
                answer += x_value

    answer *= 2

    print(f'#{tc} {answer}')