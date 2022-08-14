t = int(input())

for tc in range(1, t + 1):
    # 최대값
    answer = 0
    n, m = map(int, input().split())


    matrix = [list(map(int, input().split())) for _ in range(n)]

    # matrix의 상하좌우를 m만큼 키워 스프레이를 뿌리기 쉽게 만든다.

    # 좌우 m - 1의 빈 영역을 추가
    for i in range(n):
        for _ in range(m-1):
            matrix[i].insert(0, 0)
            matrix[i].append(0)

    # 상 하에 m - 1만큼 빈 영역 추가 
    for _ in range(m-1):
        matrix.insert(0, [0] * (2 * (m - 1) + n))
        matrix.append([0] * (2 * (m - 1) + n))

    # 스프레이의 중심을 기준으로 +, x 방향 더하면서 최대값 구하기
    for row in range(m-1, n + m - 1):
        for col in range(m-1, n + m - 1):

            # 스프레이 중앙
            plus = matrix[row][col]
            x = matrix[row][col]

            # 스프레이 범위
            for i in range(1, m):
                plus += matrix[row - i][col] + matrix[row + i][col] + matrix[row][col - i] + matrix[row][col + i]
                x += matrix[row - i][col - i] + matrix[row + i][col + i] + matrix[row + i][col - i] + matrix[row - i][col + i]

            # print(plus, x)

            # 최대값 대소 비교
            if answer < max(plus, x):
                answer = max(plus, x)

            
    print(f'#{tc} {answer}')
