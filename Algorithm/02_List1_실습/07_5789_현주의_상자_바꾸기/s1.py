import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    station = [0] * 5000
    for i in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            station[i] += 1

    p = int(input())

    answer_arr = [0] * p
    for i in range(p):
        answer_arr[i] += station[int(input())]

    print(f'#{tc}', end=' ')
    print(*answer_arr)
