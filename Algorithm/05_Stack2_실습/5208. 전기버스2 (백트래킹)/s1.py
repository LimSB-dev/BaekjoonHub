import sys
sys.stdin = open('input.txt')


def find_min(now, charge):
    global answer, cnt

    # 가지치기
    if cnt >= answer:
        return

    # 현재 위치에서 충전량 만큼 이동했을때 종점 index에 도달하면 종료 조건
    if now + charge >= station - 1:
        # 최솟값 비교
        if cnt < answer:
            answer = cnt
        return

    # 현재 index + 1부터 현재 index + 1 + 충전량만큼 탐색
    for col in range(now + 1, now + charge + 1):

        # 아직 방문하지 않은 col일 경우
        if not visited[col]:

            # 방문 갱신
            visited[col] = True

            charge = arr[col]   # 충전량 변경
            now = col          # 현재 위치
            cnt += 1            # 횟수 증가

            find_min(now, charge)

            # 재귀 함수가 바닥까지 가거나 가지치기 당한 후
            # 다시 now 위치로 돌아와야한다.
            visited[col] = False
            now = col
            cnt -= 1


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    station = arr[0]
    arr = arr[1:]
    visited = [False] * station     # 방문 리스트
    answer = 100                    # 최솟값
    cnt = 0                         # 횟수

    find_min(0, arr[0])             # 시작 index / 처음 충전량

    print(f'#{tc} {answer}')

