import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

# 분할 정복
def divide(matrix: list, n: int):
    new_matrix_list = [
        [row[:n//2] for row in matrix[:n//2]],
        [row[n//2:] for row in matrix[:n//2]],
        [row[:n//2] for row in matrix[n//2:]],
        [row[n//2:] for row in matrix[n//2:]]
    ]
    return new_matrix_list

# 하나의 색인지 확인
def check(matrix: list):
    global white, blue
    n = len(matrix)
    color = matrix[0][0]
    
    for r in range(n):
        for c in range(n):
            if color != matrix[r][c]:
                new_matrix_list = divide(matrix, n)
                for new_matrix in new_matrix_list:
                    check(new_matrix)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

check(matrix)

print(white)
print(blue)