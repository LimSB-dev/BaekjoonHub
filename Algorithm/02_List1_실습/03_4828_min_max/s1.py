t = int(input())

for tc in range(1, t + 1):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split()))
    # 최대값, 최소값에 arr의 0번째 index값을 대입
    max_value = arr[0]
    min_value = arr[0]

    # 0번째 index를 제외한 1번부터 n-1번째 index를 탐색
    for i in range(1, n):

        # 최대값 구하기
        if arr[i] > max_value:
            max_value = arr[i]

        # 최소값 구하기
        elif arr[i] < min_value:
            min_value = arr[i]

    # 최대값과 최소값의 차
    answer = max_value - min_value

    print(f'#{tc} {answer}')
