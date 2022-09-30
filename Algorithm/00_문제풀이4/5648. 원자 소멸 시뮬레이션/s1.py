import sys
sys.stdin = open('input.txt', encoding='utf-8')

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    n = int(input())

    for _ in range(n):
        x, y, direction, energy = map(int, input())

    answer = 0

    print(f'#{tc} {answer}')