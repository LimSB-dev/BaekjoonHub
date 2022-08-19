def danjo(num):
    # 10보다 작다면 종료 조건
    if num < 10:
        return True
    # 1의 자리
    tmp1 = num % 10
    # 10의 자리
    tmp2 = (num % 100) // 10
    # 단도 증가하는 수
    if tmp2 <= tmp1:
        num //= 10
        return danjo(num)
    # 위 조건이 모두 아닐 경우
    else:
        return False


for tc in range(1, int(input()) + 1):
    answer = -1
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n - 1):
        for j in range(i+1, n):
            multi = arr[i] * arr[j]
            tmp = multi
            # 단조 증가하는 수일 경우
            if danjo(multi) and answer < tmp:
                answer = tmp

    print(f'#{tc} {answer}')
