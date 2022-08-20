answer = 0
n, m = map(int, input().split())
matrix1 = [list(map(int, input())) for _ in range(n)]
matrix2 = [list(map(int, input())) for _ in range(n)]

# 완전 탐색
for row in range(n - 2):
    for col in range(m - 2):
        if matrix1[row][col] != matrix2[row][col]:
            answer += 1
            for i in range(3):
                for j in range(3):
                    matrix1[row + i][col + j] = (matrix1[row + i][col + j] + 1) % 2
if matrix1 != matrix2:
    answer = -1

print(answer)
