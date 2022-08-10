t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 2차원 배열 생성
    matrix = [list(map(str, input().split())) for _ in range(n)]

    # 90도 회전한 숫자열을 담을 배열 answer 생성
    answer = [[''] * 3 for _ in range(n)]

    # 2 중 for 문을 통한 matrix 탐색
    for row in range(n):
        for col in range(n):

            # 아래는 직접 손으로 적어가면서 찾은 규칙을 기반으로 구현했다.
            answer[row][0] += matrix[n - 1 - col][row]
            answer[row][1] += matrix[n - 1 - row][n - 1 - col]
            answer[row][2] += matrix[col][n - 1 - row]

    print(f'#{tc}')
    for i in range(n):
        print(*answer[i])
