import sys
sys.stdin = open('input.txt', encoding='utf-8')


def baby_gin(array):
    running = 0
    triple = 0

    arr = array.copy()

    for i in range(10):

        if arr[i] >= 3:
            triple += 1
            arr[i] -= 3

        if 0 < arr[i] and 0 < arr[i + 1] and 0 < arr[i + 2]:
            running += 1
            arr[i] -= 1
            arr[i + 1] -= 1
            arr[i + 2] -= 1
            if 0 < arr[i] and 0 < arr[i + 1] and 0 < arr[i + 2]:
                running += 1
                arr[i] -= 1
                arr[i + 1] -= 1
                arr[i + 2] -= 1

        if running + triple >= 1:
            return True


for tc in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    answer = 0

    # BABY GIN 검사를 위해 범위보다 많은 저장 공간을 생성
    player_1 = [0] * 12
    player_2 = [0] * 12

    for idx, value in enumerate(cards):
        if idx % 2 == 0:
            player_1[value] += 1
            if idx >= 4:
                if baby_gin(player_1):
                    answer = 1
                    break
        else:
            player_2[value] += 1
            if idx >= 5:
                if baby_gin(player_2):
                    answer = 2
                    break

    print(f'#{tc} {answer}')
