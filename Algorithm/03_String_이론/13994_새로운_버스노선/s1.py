import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    counter = [0] * 1001

    for _ in range(n):
        bus = list(map(int, input().split()))

        # 일반
        if bus[0] == 1:
            for i in range(bus[1], bus[2] + 1):
                counter[i - 1] += 1

        # 급행
        elif bus[0] == 2:
            for i in range(bus[1], bus[2] + 1):
                # 짝수
                if bus[1] % 2 == 0:
                    # 첫 정거장은 필수
                    if i == bus[1]:
                        counter[i - 1] += 1
                    # 마지막 정거장은 필수
                    elif i == bus[2]:
                        counter[i - 1] += 1
                    elif i % 2 == 0:
                        counter[i - 1] += 1
                # 홀수
                else:
                    # 첫 정거장은 필수
                    if i == bus[1]:
                        counter[i - 1] += 1
                    # 마지막 정거장은 필수
                    elif i == bus[2]:
                        counter[i - 1] += 1
                    elif i % 2 == 1:
                        counter[i - 1] += 1

        # 광역 급행
        else:
            for i in range(bus[1], bus[2] + 1):
                # 짝수
                if bus[1] % 2 == 0:
                    # 첫 정거장은 필수
                    if i == bus[1]:
                        counter[i - 1] += 1
                    # 마지막 정거장은 필수
                    elif i == bus[2]:
                        counter[i - 1] += 1
                    elif i % 4 == 0:
                        counter[i - 1] += 1
                # 홀수
                else:
                    # 첫 정거장은 필수
                    if i == bus[1]:
                        counter[i - 1] += 1
                    # 마지막 정거장은 필수
                    elif i == bus[2]:
                        counter[i - 1] += 1
                    elif i % 3 == 0 and i % 10 != 0:
                        counter[i - 1] += 1

    print(f'#{tc} {max(counter)}')
