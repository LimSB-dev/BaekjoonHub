import sys

sys.stdin = open("input.txt")

t = int(input())

for tc in range(1, t + 1):
    answer = 0
    # 한번 충전으로 최대 이동할 수 있는 정류장 수 K
    # 0번에서 출발해 종점이 N번인 정류장
    # 충전기가 설치된 M개의 정류장 번호가 주어진다.
    k, n, m = map(int, input().split())
    charging_station = list(map(int, input().split()))
    now_station = 0

    # 현재 정거장이 종점보다 작다면 계속 반복
    while now_station < n:
        for i in range(k):
            # 현재 정거장에 한번 충전으로 이동 가능한 최대 거리를 더한 후 1씩 빼주면서 다음 정류장까지 갈 수 있는지 판단
            if now_station + (k - i) in charging_station:
                now_station += k - i
                answer += 1
                # print(f'now : {now_station}, answer : {answer}')
                break

            # 만약 현재 정거장에서 한번 충전으로 이동 가능 거리가 종점을 벗어난다면 for문 탈출
            if now_station + k >= n:
                now_station += k
                break

            # 만약 i 가 k - 1 이 될 때까지 반복문을 탈출하지 못했다면 answer = 0이 된 상태로 for문 탈출
            if i == k - 1:
                answer = 0
                break

        # 만약 answer = 0 이라면
        if not answer:
            # 현재 정거장을 종점으로 바꿔서 while문 탈출
            now_station = n

    print(f'#{tc} {answer}')
