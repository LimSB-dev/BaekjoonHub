import sys
sys.stdin = open('input.txt', encoding='utf-8')

# ↘ ↙ ↖ ↗
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]


def dfs(r, c, desserts, visited, directions):
    global answer

    # 4방향 탐색
    for direction in range(4):

        # 디저트 set 깊은 복사
        desserts_copy = desserts.copy()

        # 방문 처리 깊은 복사
        visited_copy = visited.copy()

        # 방향 set 깊은 복사
        directions_copy = directions.copy()

        # 동일한 방향 가지 않기
        if direction not in directions_copy:

            # 현재 탐색 방향 저장
            directions_copy.add(direction)

            # 탐색 방향으로 위치 변경
            nr = r + dr[direction]
            nc = c + dc[direction]

            # 진행 불가능할 때까지 한 방향 반복 탐색
            while 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] not in desserts_copy and (nr, nc) not in visited:

                # 방문 처리
                visited_copy.add((nr, nc))

                # 디저트 종류 추가
                desserts_copy.add(matrix[nr][nc])

                # 재귀
                dfs(nr, nc, desserts_copy, visited_copy, directions_copy)

                # 종료 조건
                if nr == row and nc == col and len(desserts_copy) >= 4:
                    if answer < len(desserts_copy):
                        answer = len(desserts_copy)
                    return

                # 계속 진행 방향 탐색
                nr += dr[direction]
                nc += dc[direction]


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = -1

    for row in range(n):
        for col in range(n):
            desserts_set = set()
            visit = set()
            direction_set = set()
            dfs(row, col, desserts_set, visit, direction_set)

    print(f'#{tc} {answer}')
