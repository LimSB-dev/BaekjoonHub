for tc in range(1, int(input()) + 1):
    answer = -1
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i + 1, n):
            multi = arr[i] * arr[j]
            tmp = multi
            is_danjo = False
            while True:
                # 10보다 작다면 종료 조건
                if multi < 10:
                    is_danjo = True
                    break
                # 1의 자리
                tmp1 = multi % 10
                # 10의 자리
                tmp2 = (multi % 100) // 10
                # 단도 증가하는 수
                if tmp2 <= tmp1:
                    multi //= 10
                # 위 조건이 모두 아닐 경우
                else:
                    break

            # 단조 증가하는 수일 경우
            if is_danjo and answer < tmp:
                answer = tmp

    print(f'#{tc} {answer}')