t = int(input())

day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]
day_28 = [2]

for tc in range(1, t + 1):
    month_1, day_1, month_2, day_2 = map(int, input().split())
    answer = day_2 - day_1 + 1
    while month_1 < month_2:
        if month_1 in day_31:
            answer += 31
        elif month_1 in day_30:
            answer += 30
        elif month_1 in day_28:
            answer += 28

        day_1 = 0
        month_1 += 1

    print(f'#{tc} {answer}')