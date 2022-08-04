t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    matrix = [input() for _ in range(n)]
    answer = "NO"
    for i in range(n):
        # 가로줄 확인
        if "ooooo" in matrix[i]:
            answer = "YES"
            break
        for j in range(n):
            if matrix[i][j] == 'o':
                # 세로줄 확인
                if i <= n-5 and matrix[i+1][j] == 'o' and matrix[i+2][j] == 'o' and matrix[i+3][j] == 'o' and matrix[i+4][j] == 'o':
                    answer = "YES"
                    break
                # \ 대각선 확인
                elif i <= n-5 and j <= n-5 and matrix[i+1][j+1] == 'o' and matrix[i+2][j+2] == 'o' and matrix[i+3][j+3] == 'o' and matrix[i+4][j+4] == 'o':
                    answer = "YES"
                    break
                # / 대각석 확인
                elif i <= n-5 and j >= 4 and matrix[i+1][j-1] == 'o' and matrix[i+2][j-2] == 'o' and matrix[i+3][j-3] == 'o' and matrix[i+4][j-4] == 'o':
                    answer = "YES"
                    break

        if answer == "YES":
            break
    print(f'#{tc} {answer}')
