for tc in range(1, int(input()) + 1):
    answer = []
    n = int(input())
    arr = list(input().split())
    mid = n // 2
    arr1 = arr[:mid]
    arr2 = arr[(-1 * mid):]

    for i in range(mid):
        answer.append(arr1[i])
        answer.append(arr2[i])

    # n이 홀수일 경우
    if n % 2 != 0:
        answer.append(arr[mid])

    print(f'#{tc}', *answer)