import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
matrix = [list(map(int, input().split())) for _ in range(n)]

s = [[0] * (n + 1) for _ in range(n + 1)]
for x in range(1, n + 1):
    for y in range(1, n + 1):
        s[x][y] = s[x - 1][y] + s[x][y - 1] - \
            s[x - 1][y - 1] + matrix[x - 1][y - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x2][y1 - 1] - s[x1 - 1][y2] + s[x1 - 1][y1 - 1])
