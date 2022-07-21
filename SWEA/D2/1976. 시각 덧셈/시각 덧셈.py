t = int(input())

for tc in range(1, t + 1):
    answer = 0
    hour_1, min_1, hour_2, min_2 = map(int, input().split())
    sum_hour = hour_1 + hour_2
    sum_min = min_1 + min_2

    if sum_min >= 60:
        sum_min -= 60
        sum_hour += 1

    if sum_hour >= 13:
        sum_hour -= 12

    print(f'#{tc} {sum_hour} {sum_min}')