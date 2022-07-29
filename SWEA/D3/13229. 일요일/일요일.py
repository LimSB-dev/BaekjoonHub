t = int(input())

day = ['SAT', 'FRI', 'THU', 'WED', 'TUE', 'MON', 'SUN']

for tc in range(1, t + 1):
    n = input()
    last_day = day.index(n) + 1

    print(f'#{tc} {last_day}')
