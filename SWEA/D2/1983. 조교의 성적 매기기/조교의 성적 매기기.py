t = int(input())

for tc in range(1, t + 1):
    answer = 0
    students, k = map(int, input().split())
    totals = []

    for index in range(students):
        mid, last, pjt = map(int, input().split())
        total = ((35 / 100) * mid) + ((45 / 100) * last) + ((20 / 100) * pjt)
        totals.append(total)
        if index + 1 == k:
            k_score = total

    totals.sort()
    count = 1

    for score in totals:
        if k_score == score:
            break
        count += 1

    stage = students / 10

    if count > stage * 9:
        grade = 'A+'
    elif count > stage * 8:
        grade = 'A0'
    elif count > stage * 7:
        grade = 'A-'
    elif count > stage * 6:
        grade = 'B+'
    elif count > stage * 5:
        grade = 'B0'
    elif count > stage * 4:
        grade = 'B-'
    elif count > stage * 3:
        grade = 'C+'
    elif count > stage * 2:
        grade = 'C0'
    elif count > stage * 1:
        grade = 'C-'
    elif count > stage * 0:
        grade = 'D0'

    print(f'#{tc} {grade}')
