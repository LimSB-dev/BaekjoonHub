from collections import deque

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    answer = 0
    visitied = [0] * n
    fees = []

    for _ in range(n):
        fees.append(int(input()))

    weight = []
    for _ in range(m):
        weight.append(int(input()))

    cars = deque([])

    for _ in range(m * 2):
        cars.append(int(input()))

    answer = 0

    waiting = deque([])

    while cars:

        car = cars.popleft()

        # 주차
        if car > 0:
            for i in range(n):
                if not visitied[i]:
                    visitied[i] = car
                    answer += fees[i] * weight[car - 1]
                    break
                if i == n - 1:
                    waiting.append(car)
        # 출차
        else:
            car = -car
            idx = visitied.index(car)
            visitied[idx] = 0
            if waiting:
                car = waiting.popleft()
                visitied[idx] = car
                answer += fees[idx] * weight[car - 1]

    print(f'#{tc} {answer}')
