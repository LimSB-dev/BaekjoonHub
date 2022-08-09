import sys
sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    arr = list(map(int, input()))
    answer = 0
    # 0 ~ 9 까지의 숫자 범위이고 out of range ERROR를 피하기 위해 범위보다 많은 저장 공간을 만든다.
    count_arr = [0] * 12
    run = triple = 0

    # count_arr의 값을 채워준다.
    for i in range(6):
        count_arr[arr[i]] += 1

    # count_arr의 요소를 탐색한다.
    for i in range(12):

        # 만약 index의 값이 3이상으로 triple일 경우
        if count_arr[i] >= 3:
            triple += count_arr[i] // 3
            count_arr[i] %= 3

        # 만약 연속된 3개의 index의 값이 모두 0보다 클 경우
        if count_arr[i] > 0 and count_arr[i+1] > 0 and count_arr[i+2] > 0:
            run += 1
            count_arr[i] -= 1
            count_arr[i+1] -= 1
            count_arr[i+2] -= 1
            # 같은 연속된 수의 run일 경우 한 번 더 조건을 만족할 수 있다.
            if count_arr[i] > 0 and count_arr[i+1] > 0 and count_arr[i+2] > 0:
                run += 1
                count_arr[i] -= 1
                count_arr[i+1] -= 1
                count_arr[i+2] -= 1

    if triple + run == 2:
        answer = 1

    print(f'#{tc} {answer}')