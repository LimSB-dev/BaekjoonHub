t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 2차원 배열 생성
    matrix = [list(map(str, input().split())) for _ in range(n)]
    answer = [[''] * 3 for _ in range(n)]
    for row in range(n):
        for col in range(n):
            answer[row][0] += matrix[n - 1 - col][row]
            answer[row][1] += matrix[n - 1 - row][n - 1 - col]
            answer[row][2] += matrix[col][n - 1 - row]

    print(f'#{tc}')
    for i in range(n):
        print(*answer[i])