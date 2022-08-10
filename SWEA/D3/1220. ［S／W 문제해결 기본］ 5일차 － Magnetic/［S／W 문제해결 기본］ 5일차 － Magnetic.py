for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # 교착 상태의 개수를 담을 리스트 생성
    answer = [0] * n

    # 배열 탐색 교차축을 먼저 탐색
    for col in range(n):
        # 현재 위치의 자성을 담을 변수
        now = ''
        for row in range(n):
            # 교차축을 위에서부터 탐색하며 자석의 유무와 자석의 N극, S극 판단
            # 테이블 북쪽이 N극 남쪽이 S극으로 처음에 N극이 나온다면 테이블 아래로 떨어진다.
            # 때문에 N극인 경우 다음에 S극이 올 때 교착 상태를 1 증가 시킨다.
            # 다만 N극 이후 연속으로 S극이 오더라도 교착 상태는 1개로 본다.
            if matrix[row][col] == 1:
                now = 'n'
            elif matrix[row][col] == 2:
                if now == 'n':
                    answer[col] += 1
                now = 's'

    print(f'#{tc}', end=' ')
    print(sum(answer))
