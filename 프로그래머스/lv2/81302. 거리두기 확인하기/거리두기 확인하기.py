# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(place):
    answer = 1
    for row in range(5):
        for col in range(5):
            visited = [[False] * 5 for _ in range(5)]
            visited[row][col] = True
            if place[row][col] == 'P':
                for direction1 in range(4):
                    nx1 = row + dx[direction1]
                    ny1 = col + dy[direction1]
                    if 0 <= nx1 < 5 and 0 <= ny1 < 5 and not visited[nx1][ny1] and place[nx1][ny1] != 'X':
                        visited[nx1][ny1] = True
                        if place[nx1][ny1] == 'P':
                            answer = 0
                            break
                        for direction2 in range(4):
                            nx2 = nx1 + dx[direction2]
                            ny2 = ny1 + dy[direction2]
                            if 0 <= nx2 < 5 and 0 <= ny2 < 5 and not visited[nx2][ny2] and place[nx2][ny2] != 'X':
                                visited[nx2][ny2] = True
                                if place[nx2][ny2] == 'P':
                                    answer = 0
    return answer

def solution(places):
    arr = []
    for place in places:
        arr.append(dfs(place))
    return arr