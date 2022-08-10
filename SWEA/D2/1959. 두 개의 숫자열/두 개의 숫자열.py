t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))

    # 최대값을 대입할 변수 answer 생성
    answer = 0

    # n과 m 중 어떤 값이 클지 알 수 없기 때문에 abs()를 사용
    for i in range(abs(n-m)+1):

        # 두 숫자열의 곱의 더할 변수 생성
        sum_value = 0

        # n과 m 중 작은 값만큼 반복
        for j in range(min(n, m)):

            # 배열의 길이에 따른 조건문
            if len(arr_n) > len(arr_m):
                sum_value += arr_n[i+j] * arr_m[j]
            elif len(arr_m) > len(arr_n):
                sum_value += arr_n[j] * arr_m[i+j]
            else:
                sum_value += arr_n[j] * arr_m[j]

        # 최대값과 대소비교
        if sum_value > answer:
            answer = sum_value

    print(f"#{tc} {answer}")
