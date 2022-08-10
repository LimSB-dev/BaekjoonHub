t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    # 열 탐색
    for row in range(n):

        # 연속하는 1의 횟수를 담을 변수
        cnt = 0
        for col in range(n):

            # 1이 나올 경우 cnt의 값을 1씩 증가
            if matrix[row][col] == 1:
                cnt += 1

                # 문제의 조건 k와 cnt의 값이 같다면 answer의 값 1 증가
                if cnt == k:
                    answer += 1

                # 만약 cnt가 k보다 커진다면 answer의 값 1 감소
                # 계속해서 answer의 1씩 감소하는 것을 방지하기 위해 cnt을 0으로 초기화
                elif cnt > k:
                    answer -= 1
                    cnt = 0

            # 1이 아닐 경우 cnt를 0으로 초기화
            else:
                cnt = 0

    # 이하 동일
    for col in range(n):
        cnt = 0
        for row in range(n):
            if matrix[row][col] == 1:
                cnt += 1
                if cnt == k:
                    answer += 1
                elif cnt > k:
                    answer -= 1
                    cnt = 0
            else:
                cnt = 0

    print(f"#{tc} {answer}")
