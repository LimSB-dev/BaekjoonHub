t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    station_arr = [[0, 0] for _ in range(n)]
    for i in range(n):
        a, b = map(int, input().split())
        station_arr[i] = [a, b]

    p = int(input())

    answer_arr = [0] * p
    for i in range(p):
        station = int(input())
        for j in range(n):
            if station_arr[j][0] <= station <= station_arr[j][1]:
                answer_arr[i] += 1

    print(f'#{tc}', *answer_arr)