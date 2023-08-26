def solution(m, n, board):
    def check_2x2(board):
        """
        입력 받은 보드의 모든 2x2 블록을 '.'으로 변경한 새로운 보드를 반환
        """
        delta = [(0, 0), (0, 1), (1, 0), (1, 1)]
        new_board = [row[:] for row in board]

        for row in range(m - 1):
            for col in range(n - 1):
                block = board[row][col]

                if block == '.':
                    continue

                breaker = False
                for dr, dc in delta:
                    nr, nc = row + dr, col + dc

                    if block != board[nr][nc]:
                        breaker = True
                        break

                if breaker:
                    continue

                for dr, dc in delta:
                    nr, nc = row + dr, col + dc
                    new_board[nr][nc] = '.'

        return new_board

    def drop_down(board):
        """
        입력 받은 보드의 빈 공간에 위에 있는 블록을 아래로 떨어뜨려 빈 공간을 채운 새로운 보드를 반환
        """
        new_board = [row[:] for row in board]

        for col in range(n):
            stack = []
            for row in range(m):
                if board[row][col] != '.':
                    stack.append(board[row][col])

            for row in range(m - 1, -1, -1):
                if stack:
                    new_board[row][col] = stack.pop()
                else:
                    new_board[row][col] = '.'

        return new_board

    board = [list(row) for row in board]
    answer = 0
    while True:
        cur_answer = 0
        board = drop_down(check_2x2(board))

        for row in range(m):
            for col in range(n):
                if board[row][col] == '.':
                    cur_answer += 1

        if answer == cur_answer:
            break

        answer = cur_answer

    return answer
