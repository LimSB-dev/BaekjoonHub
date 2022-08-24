for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    answer = []

    # 0 이하의 값이 나올 때까지 반복
    while arr[-1] != 0:

        # 사이클
        for i in range(1, 6):
            num = arr[0]
            arr = arr[1:]
            num -= i
            arr.append(num)

            # 종료 조건
            if num <= 0:
                arr[-1] = 0
                break

    print(f'#{tc}', *arr)
