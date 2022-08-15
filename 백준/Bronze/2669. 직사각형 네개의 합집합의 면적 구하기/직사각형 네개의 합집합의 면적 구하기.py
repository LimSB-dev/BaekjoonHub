matrix = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for row in range(x1, x2):
        for col in range(y1, y2):
            if matrix[row][col] == 0:
                matrix[row][col] = 1
                answer += 1

print(answer)