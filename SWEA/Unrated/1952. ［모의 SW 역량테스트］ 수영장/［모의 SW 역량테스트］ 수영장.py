for tc in range(1, int(input()) + 1):

    # 요금
    fees = list(map(int, input().split()))

    # 월별 횟수
    months = list(map(int, input().split()))

    # 매달 최소 요금 저장 리스트
    dp = [0] * 13

    for i in range(1, 13):

        # 1일 이용 금액과 1달 이용 금액 대소비교
        dp[i] = min(dp[i-1] + months[i-1] * fees[0], dp[i-1] + fees[1])

        if i >= 3:

            # 3달 이용 금액과 지금까지 최소 이용 금액 대소 비교
            dp[i] = min(dp[i-3] + fees[2], dp[i])

    # 1년 이용 금액
    answer = min(dp[12], fees[3])

    print(f'#{tc} {answer}')