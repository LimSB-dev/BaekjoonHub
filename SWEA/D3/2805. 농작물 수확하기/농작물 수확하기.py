for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    # 중앙값
    answer = matrix[mid][mid]

    # 대각
    for i in range(1, mid + 1):
        for j in range(1, mid + 1):
            if i + j <= mid:
                answer += matrix[mid + i][mid + j]
                answer += matrix[mid - i][mid - j]
                answer += matrix[mid + i][mid - j]
                answer += matrix[mid - i][mid + j]

    # 가로 세로
    for i in range(1, mid + 1):
        answer += matrix[mid + i][mid]
        answer += matrix[mid - i][mid]
        answer += matrix[mid][mid + i]
        answer += matrix[mid][mid - i]

    print(f'#{tc} {answer}')
