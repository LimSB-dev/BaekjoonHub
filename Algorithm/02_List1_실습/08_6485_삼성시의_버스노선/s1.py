import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    stations = [[0, 0] for _ in range(n)]
    for i in range(n):
        a, b = map(int, input().split())
        stations[i] = [a, b]

    p = int(input())

    answer_arr = [0] * p
    for i in range(p):
        station = int(input())
        for j in range(n):
            if stations[j][0] <= station <= stations[j][1]:
                answer_arr[i] += 1

    print(f'#{tc}', end=' ')
    print(*answer_arr)