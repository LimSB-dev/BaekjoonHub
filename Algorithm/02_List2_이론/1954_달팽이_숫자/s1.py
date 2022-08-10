import sys
sys.stdin = open('input.txt')

# 방향 전환을 위한 delta row, delta column
# 순서는 우 > 하 > 좌 > 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    # 이차원배열 생성
    answer = [[0]*n for _ in range(n)]
    # 초기 위치 & 회전 방향 설정
    r = c = 0
    # 0: 우, 1: 하, 2: 좌, 3: 상
    direction = 0

    # 이차원배열에 값 넣기
    for i in range(1, n**2 + 1):
        answer[r][c] = i
        r += dr[direction]
        c += dc[direction]

        # 범위를 벗어나거나 0 이 아닌 다른 값이 존재한다면 방향 전환
        if n <= r or r < 0 or n <= c or c < 0 or answer[r][c] != 0:
            # 이미 앞에서 실행해서 다음 반복 때 오류가 생기기 때문에 실행 취소
            r -= dr[direction]
            c -= dc[direction]

            direction = (direction + 1) % 4

            # 다시 실행
            r += dr[direction]
            c += dc[direction]

    print(f'#{tc}')
    for row in answer:
        print(*row)
