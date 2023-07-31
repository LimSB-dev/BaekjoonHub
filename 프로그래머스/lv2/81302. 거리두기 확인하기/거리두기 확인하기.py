def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def check_surrounding(place, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    queue = [(x, y, 0)]

    while queue:
        x, y, dist = queue.pop(0)

        if dist == 2:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_valid(nx, ny) and not visited[nx][ny] and place[nx][ny] != 'X':
                visited[nx][ny] = True
                if place[nx][ny] == 'P':
                    return False
                queue.append((nx, ny, dist + 1))

    return True

def sol(place):
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                if not check_surrounding(place, row, col):
                    return 0
    return 1

def solution(places):
    return [sol(place) for place in places]
