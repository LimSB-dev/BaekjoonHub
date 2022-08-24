import sys
sys.stdin = open('input.txt')


def find_min(array, cnt):
    global answer

    # 정렬 되었다면 재귀 종료
    if array == sorted_arr or array == reversed_arr:
        if answer > cnt:
            answer = cnt
        return
    else:
        cnt += 1

        # 가지치기
        if answer <= cnt:
            return

        if cnt > 5:
            return

        # 0 ~ n - 1 셔플
        # 단 0은 똑같아서 무한 루프
        for i in range(1, n):

            stack = []

            # 카드 리스트를 두 개로 나누기
            arr1 = array[:half]
            arr2 = array[half:]

            # arr1 먼저
            if i < half:
                for _ in range(half - i):
                    stack.append(arr1.pop(0))

                for _ in range(i):
                    stack.append(arr2.pop(0))
                    stack.append(arr1.pop(0))

                for _ in range(half - i):
                    stack.append(arr2.pop(0))
            # arr2 먼저
            else:
                for _ in range(i - half + 1):
                    stack.append(arr2.pop(0))

                for _ in range(n - i - 1):
                    stack.append(arr1.pop(0))
                    stack.append(arr2.pop(0))

                for _ in range(i - half + 1):
                    stack.append(arr1.pop(0))

            find_min(stack, cnt)


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())    # 카드의 수
    half = n // 2
    arr = list(map(int, input().split()))   # 카드
    answer = INF  # 최소 횟수
    cnt = 0 # 카운트

    # 오름차순 / 내림차순
    sorted_arr = list(range(1, n + 1))
    reversed_arr = list(range(n, 0, -1))

    find_min(arr, cnt)

    if answer > 5:
        answer = -1

    print(f'#{tc} {answer}')
