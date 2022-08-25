import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c, depth):
    global answer

    queue = [(r, c, depth)]


INF = 999999999

w, h = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

# 최소 날짜
answer = INF

apple = []

for row in range(h):
    for col in range(w):

        if box[row][col] == 1:
            apple.append([row, col])

        if box[row][col] == -1:
            visited[row][col] = True

bfs(r, c, 0)


print(answer)