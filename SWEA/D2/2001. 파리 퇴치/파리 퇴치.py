t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = 0

    # 배열의 길이에서 파리채의 길이만큼 뺀 범위 탐색 m은 n의 0,0 배열에서 시작함으로 +1
    for row in range(n-m+1):
        for col in range(n-m+1):

            # 파리채 밤위 안에서 잡은 파리의 합
            sum_value = 0

            # 파리채의 배열 탐색
            for i in range(m):
                for j in range(m):
                    sum_value += matrix[col+i][row+j]

                    # 최대값과 대소 비교
                    if sum_value > answer:
                        answer = sum_value

    print(f"#{tc} {answer}")
