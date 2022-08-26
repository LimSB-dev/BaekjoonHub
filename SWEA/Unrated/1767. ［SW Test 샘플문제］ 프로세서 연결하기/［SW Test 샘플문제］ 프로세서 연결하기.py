import copy

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# cnt: 현재까지 탐색한 core
# connect: 전류가 통하는 core
# sum_line: 전선의 길이 합
def dfs(cnt, connect, sum_line, visited):
    global answer, max_core

    # 가지치기
    # 총 코어 수 - 현재 core 수 + 전류가 통하는 core
    # 앞으로 탐색 가능한 core 수 + 현재 전류가 통하는 core가 최대 core 수 미만이면 가지치기
    if len(core) - cnt + connect < max_core:
        return

    # 종료 조건
    # 모든 core를 탐색
    if cnt == len(core):
        # 전류가 연결된 core의 수가 max_core일 경우
        if connect == max_core:
            # 최소 전선의 길이와 현재 전선의 길이 합 대소 비교
            answer = min(answer, sum_line)
        # 현재 연결 core의 수가 최대 연결 core 수 초과
        elif connect > max_core:
            # 최소 전선의 길이는 현재 전선의 길이
            answer = sum_line
            max_core = connect
        return

    r, c = core[cnt]

    for direction in range(4):
        # 깊은 복사
        visited_copy = copy.deepcopy(visited)
        line = 0
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 2차원 배열 범위
        while 0 <= nr < n and 0 <= nc < n:

            # 방문 기록 False / core가 아닐 경우
            if not visited_copy[nr][nc] and matrix[nr][nc] != 1:
                line += 1
                visited_copy[nr][nc] = True
                nr += dr[direction]
                nc += dc[direction]
            else:
                line = 0
                break

        if line != 0:
            dfs(cnt + 1, connect + 1, sum_line + line, visited_copy)

    # 4 방향 모두 연결이 안 된 경우 다음 core 탐색
    dfs(cnt + 1, connect, sum_line, visited)


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    # 최단 길이
    answer = INF

    # 최고로 많이 연결된 core 수
    max_core = 0

    # 가장 자리를 제외한 코어의 위치
    core = []

    # 가장 자리 제외한 코어 탐색
    for row in range(1, n - 1):
        for col in range(1, n - 1):
            if matrix[row][col] == 1:
                core.append((row, col))

    dfs(0, 0, 0, visited)

    print(f'#{tc} {answer}')
