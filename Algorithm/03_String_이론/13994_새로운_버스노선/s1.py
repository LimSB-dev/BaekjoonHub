import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    n = int(input())
    bus = [list(map(int, input().split())) for _ in range(n)]

    # 일반
    normal = bus[0]
    # 급행
    express = []
    # 광역 급행
    wide_area_express = []

    # 급행
    # 짝수
    if bus[1][0] % 2 == 0:
        for i in bus[1]:
            # 마지막 정거장은 필수
            if i == n - 1:
                express.append(i)
            elif i % 2 == 0:
                express.append(i)
    # 홀수
    else:
        for i in bus[1]:
            # 마지막 정거장은 필수
            if i == n - 1:
                express.append(i)
            elif i % 2 == 1:
                express.append(i)

    # 광역 급행
    # 짝수
    if bus[1][0] % 2 == 0:
        for i in bus[2]:
            # 마지막 정거장은 필수
            if i == n - 1:
                wide_area_express.append(i)
            elif i % 4 == 0:
                wide_area_express.append(i)
    # 홀수
    else:
        for i in bus[2]:
            # 마지막 정거장은 필수
            if i == n - 1:
                wide_area_express.append(i)
            elif i % 3 == 0 and i % 10 != 0:
                wide_area_express.append(i)

    

    print(f'#{tc} {len(answer)}')
