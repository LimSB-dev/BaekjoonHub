import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().strip())) for _ in range(9)]


def check(x, y, n):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
        if sudoku[i][y] == n:
            return False
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[x + i][y + j] == n:
                return False
    return True


def dfs(z):
    if z == 81:
        print('\n'.join(''.join(map(str, sudoku[i])) for i in range(9)))
        exit()
    x = z // 9
    y = z % 9
    if sudoku[x][y] == 0:
        for i in range(1, 10):
            if check(x, y, i):
                sudoku[x][y] = i
                dfs(z + 1)
                sudoku[x][y] = 0
    else:
        dfs(z + 1)


dfs(0)
