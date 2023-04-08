def check(bingoO, bingoX, cntO, cntX):
    # 선공이 후공보다 적거나 후공보다 2개 이상 앞설 경우
    if cntO < cntX or cntO >= cntX + 2:
        return 0

    # O, X 둘 다 빙고에 성공한 경우
    if bingoO != 0 and bingoX != 0:
        return 0

    # 빙고에 성공한 줄이 2개보다 많은 경우
    if bingoO + bingoX > 2:
        return 0

    # O의 승리 상황에서 O의 개수와 X의 개수가 같은 경우
    if bingoO != 0 and cntO == cntX:
        return 0

    # X의 승리 상황에서 O의 개수가 X의 개수보다 많은 경우
    if bingoX != 0 and cntO > cntX:
        return 0

    # 그 외의 모든 경우
    return 1


def solution(board):
    bingoO = 0
    bingoX = 0
    cntO = 0
    cntX = 0

    for row in range(3):

        # 가로 빙고
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '.':
            if board[row][0] == 'O':
                bingoO += 1
            else:
                bingoX += 1

        # 세로 빙고
        if board[0][row] == board[1][row] == board[2][row] and board[0][row] != '.':
            if board[0][row] == 'O':
                bingoO += 1
            else:
                bingoX += 1

        # O, X 개수
        for col in range(3):
            value = board[row][col]

            if value == 'O':
                cntO += 1
            if value == 'X':
                cntX += 1

    # 대각 빙고
    if board[1][1] == 'O':
        if board[0][0] == board[1][1] == board[2][2]:
            bingoO += 1
        if board[0][2] == board[1][1] == board[2][0]:
            bingoO += 1
    elif board[1][1] == 'X':
        if board[0][0] == board[1][1] == board[2][2]:
            bingoX += 1
        if board[0][2] == board[1][1] == board[2][0]:
            bingoX += 1

    return check(bingoO, bingoX, cntO, cntX)
