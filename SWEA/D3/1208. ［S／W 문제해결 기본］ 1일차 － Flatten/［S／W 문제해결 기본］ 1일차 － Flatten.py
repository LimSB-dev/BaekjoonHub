for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    
    # 상자의 높이별 개수를 담을 리스트
    count_arr = [0] * 100

    # 가로 길이는 항상 100
    for i in range(100):
        count_arr[arr[i] - 1] += 1

    # 주어진 덤프 횟수만큼 평탄화 작업
    for i in range(n):
        for j in range(100):
            
            # count_arr의 index가 j 일 때 0이 아니라면
            if count_arr[j]:
                count_arr[j] -= 1
                count_arr[j + 1] += 1
                break

    # 주어진 덤프 횟수만큼 평탄화 작업
    for i in range(n):
        for j in range(100):
            
            # count_arr의 index가 99 - j 일 때 0이 아니라면
            if count_arr[99 - j]:
                count_arr[99 - j] -= 1
                count_arr[98 - j] += 1
                break

    for i in range(100):
        if count_arr[i]:
            min_value = i
            break

    for i in range(100):
        if count_arr[99 - i]:
            max_value = 99 - i
            break

    answer = max_value - min_value

    print(f'#{tc + 1} {answer}')
