# 색종이의 장수를 나타내는 정수
n = int(input())

# 2차원 배열
matrix = [[0] * 1001 for _ in range(1001)]

# 색종이의 영역 색칠
for i in range(1, n + 1):
    x, y, w, h = map(int, input().split())

    for row in range(w):
        matrix[x + row][y:(y + h)] = [i] * h

answer = ''
for i in range(1, n + 1):
    counter = 0
    for j in range(1001):
        counter += matrix[j].count(i)

    answer += f'{counter}\n'

print(answer)
