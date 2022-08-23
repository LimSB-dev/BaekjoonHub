import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    station = arr[0]    # 정류장
    arr = arr[1:]       # 충전지
    charge = arr[0]     # 충전량
    now = 0             # 현재 위치 index값
    cnt = 0           # 최소 교환 횟수는 무료

    # 현재 위치 index가 정류장 index이상이면 종료
    while now < station - 1:

        # 다음 정류장까지 갈 때 최대 위치 정류장
        max_distance = 0

        # 충전 횟수 증가
        cnt += 1

        # 충전량만큼 이동 가능
        for j in range(1, charge + 1):

            # 현재 위치에서 충전량 만큼 이동했을 때 충전소 이상일 경우
            if now + j >= station - 1:
                # 충전량 만큼 반복하는 for문 탈출
                break

            # 최대로 갈 수 있는 다음 정류장 비교
            if max_distance < j + arr[now + j]:
                max_distance = j + arr[now + j]

        now += max_distance
    print(f'#{tc} {cnt}')
