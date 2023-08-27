import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def in_range(y, x):
    return 0 <= y < 10 and 0 <= x < 10


def press(b, y, x):
    for i in range(5):
        ny, nx = y + dy[i], x + dx[i]
        if in_range(ny, nx):
            b[ny][nx] = (b[ny][nx] + 1) % 2


dy = [0, 0, 1, 0, -1]
dx = [0, 1, 0, -1, 0]


board = [[0] * 10 for _ in range(10)]

for i in range(10):
    line = input()
    for j in range(10):
        if line[j] == "O":
            board[i][j] = 1

first_line_press_case = [101] * (1 << 10)

for case in range(1 << 10):
    tmp_board = [board[i][:] for i in range(10)]
    cnt = 0

    mask = 1
    for j in range(9, -1, -1):
        if case & mask:
            press(tmp_board, 0, j)
            cnt += 1
        mask <<= 1

    for i in range(1, 10):
        for j in range(10):
            if tmp_board[i - 1][j]:
                press(tmp_board, i, j)
                cnt += 1

    if sum(tmp_board[9]) == 0:
        first_line_press_case[case] = cnt

print(min(first_line_press_case))
