from collections import deque


def rotation(gear_index, direction):
    global answer

    # 방문 처리
    visited[gear_index] = True

    # 좌우 기어 탐색
    for i in [-1, 1]:
        next_gear = gear_index + i

        # 기어 index 범위 내부 / 방문 전적 False
        if 0 <= next_gear < 4 and not visited[next_gear]:

            # 자석의 극이 다를 경우
            if gears[gear_index][2 * i] != gears[next_gear][-2 * i]:

                # 재귀
                rotation(next_gear, -direction)

    # 회전전 방향
    if direction == 1:
        gears[gear_index].insert(0, gears[gear_index].pop())
    else:
        gears[gear_index].append(gears[gear_index].popleft())


for tc in range(1, int(input()) + 1):
    k = int(input())
    gears = [deque(map(int, input().split())) for _ in range(4)]
    turns = [list(map(int, input().split())) for _ in range(k)]
    answer = 0

    for turn in turns:
        idx, direction = turn

        # 방문 초기화
        visited = [False] * 4

        # 회전
        rotation(idx - 1, direction)

    for i in range(4):
        # 점수 기록
        if gears[i][0] == 1:
            answer += 2 ** i

    print(f'#{tc} {answer}')
