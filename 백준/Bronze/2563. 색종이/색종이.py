answer = 0
matrix = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            if matrix[row][col] == 0:
                matrix[row][col] = 1
                answer += 1

print(answer)