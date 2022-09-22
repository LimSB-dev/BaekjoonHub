import sys
sys.stdin = open('input.txt', encoding='utf-8')


def find_max(containers, trucks, weight):
    global answer

    containers_copy = list(containers)
    trucks_copy = list(trucks)

    # 가지치기
    if sum(containers_copy) + weight <= answer:
        return

    # 저장
    if answer < weight:
        answer = weight

    if containers and trucks:
        container = containers_copy.pop()
        truck = trucks_copy[-1]

        if truck >= container:
            trucks_copy.pop()
            weight += container
            find_max(containers_copy, trucks_copy, weight)
        else:
            find_max(containers_copy, trucks_copy, weight)


INF = 999999999
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    answer = -INF

    arr_1.sort()
    arr_2.sort()

    find_max(arr_1, arr_2, 0)

    print(f'#{tc} {answer}')
