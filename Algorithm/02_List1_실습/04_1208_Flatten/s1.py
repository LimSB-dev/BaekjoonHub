for tc in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))
    answer = 0
    # 상자의 높이별 개수를 담을 리스트
    box_height = [0] * 100

    # 가로 길이는 항상 100
    for i in range(100):
        box_height[boxes[i] - 1] += 1

    # 주어진 덤프 횟수만큼 평탄화 작업
    for i in range(dump):
        for j in range(100):
            # box_height의 index가 j 일 때 0이 아니라면
            # 즉, 높이가 j인 상자가 존재하면
            if box_height[j]:
                # 높이가 j인 상자의 개수를 하나 줄이고 높이가 j + 1인 상자의 개수를 1개 늘림
                box_height[j] -= 1
                box_height[j + 1] += 1
                break

    # 주어진 덤프 횟수만큼 평탄화 작업
    for i in range(dump):
        for j in range(100):
            # box_height의 index가 99 - j 일 때 0이 아니라면
            # 즉, 높이가 99 - j인 상자가 존재하면
            if box_height[99 - j]:
                # 높이가 99 - j인 상자의 개수를 하나 줄이고 높이가 98 - j 인 상자의 개수를 1개 늘림
                box_height[99 - j] -= 1
                box_height[98 - j] += 1
                break

    # 최대값 찾기
    for i in range(100):
        if box_height[99 - i]:
            max_value = 99 - i
            break

    # 최소값 찾기
    for i in range(100):
        if box_height[i]:
            min_value = i
            break

    answer = max_value - min_value

    print(f'#{tc + 1} {answer}')
