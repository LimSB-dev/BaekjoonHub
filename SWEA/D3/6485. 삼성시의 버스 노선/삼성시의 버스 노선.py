t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    station = [0] * 5000
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a-1 , b):
            station[i] += 1

    p = int(input())

    answer_arr = [0] * p
    for i in range(p):
        answer_arr[i] += station[int(input()) - 1]

    print(f'#{tc}', end=' ')
    print(*answer_arr)