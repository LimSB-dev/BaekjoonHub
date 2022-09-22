import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_max(times, start, end, value):
    global answer

    times_copy = times.copy()

    # 가지치기
    if len(times_copy) + value <= answer:
        return

    # 종료조건
    if answer < value:
        answer = value

    if times_copy:
        time = times_copy.pop()

        ns, ne = time

        if end <= ns:
            # 화물이 들어올 수 있지만 안 받기
            find_max(times_copy, start, end, value)
            # 화물 받기
            find_max(times_copy, ns, ne, value + 1)
        else:
            find_max(times_copy, start, end, value)


for tc in range(1, int(input()) + 1):
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    # 작업 시작 시간 기준 내림차순
    times.sort(key=lambda x: x[0], reverse=True)

    find_max(times, 0, 0, 0)

    print(f'#{tc} {answer}')
