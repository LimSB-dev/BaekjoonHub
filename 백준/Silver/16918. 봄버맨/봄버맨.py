import sys
input = sys.stdin.readline
# 아이디어 1: 폭탄이 아무리 터져도 결국 나올 수 있는 칸의 모양은 3가지이다.
# 1. 일부 칸에 폭탄이 설치된 상태
# 2. 모든 칸에 폭탄이 설치된 상태
# 3. 폭탄이 터진 상태


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bomb(board):
    return_board = [['O'] * C for _ in range(R)]
    bomb_position = []
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                bomb_position.append((i, j))

    for i in range(R):
        for j in range(C):
            if (i, j) in bomb_position:
                return_board[i][j] = '.'
                for direction in range(4):
                    nr = i + dr[direction]
                    nc = j + dc[direction]
                    if 0 <= nr < R and 0 <= nc < C:
                        return_board[nr][nc] = '.'

    return return_board

def print_board(board):
    answer = ""
    for row in board:
        answer += "".join(row)
        answer += '\n'

    print(answer)

R, C, N = map(int, input().split())
first_board = [list(input().strip()) for _ in range(R)]
second_board = [['O'] * C for _ in range(R)]

if N == 1:
    print_board(first_board)
elif N % 2 == 0:
    print_board(second_board)
elif N % 4 == 3:
    print_board(bomb(first_board))
else:
    print_board(bomb(bomb(first_board)))