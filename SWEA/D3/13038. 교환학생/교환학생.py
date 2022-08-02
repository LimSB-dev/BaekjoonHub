t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    day_list = list(map(int, input().split()))
    # 일주일 강의수
    weeks = sum(day_list)

    # 마지막 일주일 남는 일 수
    weeks_r = n % weeks

    # 최소 일수를 위한 최소 주 * 7
    answer = (n // weeks) * 7

    # 아래 조건문에서 사용될 변수 생성
    min_day = 7
    # 만약 마지막 일주일 남는 일 수가 0일
    if weeks_r == 0:
        for i in range(7):
            cnt = 0
            days = 0
            # 만약 시작일에 수업이 없다면
            if day_list[i] == 0:
                # 다시 for문
                continue
            for j in range(7):
                days += 1
                if day_list[(i+j) % 7] == 1:
                    cnt += 1
                if cnt == weeks:
                    break

            if min_day > days:
                min_day = days
        # 마지막 일주일의 남은 일 수가 0일이라면 일주일을 추가로 더했기 때문에 7일을 뺀다.
        answer += min_day - 7
    else:
        for i in range(7):
            cnt = 0
            days = 0
            for j in range(7):
                days += 1
                if day_list[(i+j) % 7] == 1:
                    cnt += 1
                if cnt == weeks_r:
                    break

            if min_day > days:
                min_day = days
        answer += min_day

    print(f'#{tc} {answer}')
