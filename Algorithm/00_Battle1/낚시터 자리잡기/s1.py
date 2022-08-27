import sys
sys.stdin = open('input.txt')

dg = [-1, 1]


# 게이트 index, 사람의 수, fishing, 이동거리 합
def bfs(gate, visited, sum_length):
    global answer

    visited[gate[0][0]] = True

    while gate:

        g, p, visited, sum_length = gate.pop(0)

        for direction in range(2):
            ng = g + dg[direction]
            np = p - 1

            # 이동 거리 증가
            move = 0

            if 0 <= ng < n and 0 <= np and not visited[ng]:

                # 방문 처리
                visited[ng] = True

                move += 1

                gate.append(ng, np, visited, sum_length + move)


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())

    # 최소 이동 거리
    answer = INF

    # 낚시터
    fishing = [False] * n

    entrance = []
    for i in range(3):
        gate, people = map(int, input().split())
        entrance.append([gate - 1, people])

    # 게이트 순서
    bfs(entrance, fishing, 0)

    print(f'#{tc} {answer}')
