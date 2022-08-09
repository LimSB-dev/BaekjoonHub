t = int(input())

for tc in range(1, t + 1):
    answer = 0
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    # 구간합을 담을 최대값, 최소값 변수 생성
    max_value = 0
    min_value = 0

    # 범위가 m인 구간의 합의 첫번째 구간을 최대값, 최소값에 대입
    for j in range(m):
        max_value += arr[j]
        min_value += arr[j]

    for i in range(n - m + 1):
        sum_value = 0
        for j in range(m):
            sum_value += arr[i + j]

        if sum_value > max_value:
            max_value = sum_value
        elif sum_value < min_value:
            min_value = sum_value

    answer = max_value - min_value

    print(f'#{tc} {answer}')
