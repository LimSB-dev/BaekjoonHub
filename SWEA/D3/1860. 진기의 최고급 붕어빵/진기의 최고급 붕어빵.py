for tc in range(1, int(input()) + 1):
    answer = 'Possible'
    fish = 0
    # n: 손님의 수
    # m: 붕어빵을 만드는데 걸리는 시간
    # k: 한 번에 만드는 붕어빵의 개수
    n, m, k = map(int, input().split())

    # 손님이 오는 시간
    arr = list(map(int, input().split()))

    arr.sort()
    if arr[0] == 0:
        answer = 'Impossible'
    else:
        for i in range(1, arr[-1] + 1):
            if i % m == 0:
                fish += k
            # 같은 시간에 여러 손님이 올 경우
            while True:
                if i in arr:
                    fish -= 1
                    arr.pop(0)
                else:
                    break
            if fish < 0:
                answer = 'Impossible'
                break

    print(f'#{tc} {answer}')
