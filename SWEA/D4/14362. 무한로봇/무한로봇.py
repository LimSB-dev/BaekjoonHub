# 상 좌 하 우
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

INF = 999999999

for tc in range(1, int(input()) + 1):
    cmds = list(input())
    direction = 0

    answer = 0

    height = 0
    width = 0

    for _ in range(4):
        for cmd in cmds:

            if cmd == 'S':

                height += dr[direction]
                width += dc[direction]

                length = (height ** 2) + (width ** 2)

                if length > answer:
                    answer = length

            elif cmd == 'L':
                direction += 3
                direction %= 4
            elif cmd == 'R':
                direction += 1
                direction %= 4

    if height != 0 or width != 0:
        answer = 'oo'

    print(f'#{tc} {answer}')