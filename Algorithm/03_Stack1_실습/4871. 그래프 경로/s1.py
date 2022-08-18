import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    path = [0] * (v + 1)
    matrix = []
    answer = 0
    for i in range(e):
        matrix.append(list(map(int, input().split())))

    for i in matrix:
        i = i.sort()

    start, end = map(int, input().split())

    path[start] = 1



    print(f'#{tc} {answer}')
