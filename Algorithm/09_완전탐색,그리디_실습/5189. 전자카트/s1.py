import sys
sys.stdin = open('input.txt', encoding='utf-8')

from itertools import permutations


def cal(idx, value):
    global answer
    now_idx = arr[idx]
    next_idx = arr[idx + 1]

    value += matrix[now_idx - 1][next_idx - 1]

    # 가지치기
    if answer < value:
        return

    # 종료조건
    if next_idx == 1:
        answer = value
        return

    cal(idx + 1, value)

INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = INF

    for arr in permutations(range(2, n + 1)):
        arr = list(arr)
        arr.insert(0, 1)
        arr.append(1)

        cal(0, 0)

    print(f'#{tc} {answer}')
