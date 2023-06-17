delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    row, col, direction, value = 0, 0, 0, 1

    for _ in range(n**2):
        answer[row][col] = value
        next_row, next_col = row + delta[direction][0], col + delta[direction][1]

        if 0 <= next_row < n and 0 <= next_col < n and answer[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4
            row, col = row + delta[direction][0], col + delta[direction][1]

        value += 1

    return answer
