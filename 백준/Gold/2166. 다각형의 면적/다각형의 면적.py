import sys
input = sys.stdin.readline

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

total_x, total_y = 0, 0
for i in range(n):
    total_x += points[i][0] * points[i-1][1]
    total_y += points[i][1] * points[i-1][0]

print(round(abs(total_x - total_y) / 2, 1))