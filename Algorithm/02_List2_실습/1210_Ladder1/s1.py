import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    answer = 0
    # 사다리 배열 생성
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    # 결과값의 위치가 주어졌을 때 출발지를 찾는 가장 쉬운 방법은
    # 도착지에서 출발지로 선을 그어보면 되는 것이다.
    for row in range(100):
        for col in range(100):
            # 끝~ 출발지가 2인 col값 찾기
            if row == 99:
                if matrix[0][col] == 2:
                    answer = col
            
            # 만약 도착지에서부터 연결된 선이면
            if matrix[99 - row][col] == 2:
                
                # 좌우 먼저 살펴보기
                # 왼쪽으로 갈 수 있을 때
                if col != 0:
                    # 왼쪽 선이 존재한다면
                    if matrix[99 - row][col - 1] == 1:
                        cnt = 1
                        # 반복문은 오른쪽으로 탐색하기에 while문으로 왼쪽을 계속 탐색
                        while True:
                            matrix[99 - row][col - cnt] = 2
                            
                            # 위로 다시 갈 수 있으면 위로가고 반복문 탈출
                            if matrix[98 - row][col - cnt] == 1:
                                matrix[98 - row][col - cnt] = 2
                                break
                            cnt += 1
                        continue
                    
                # 오른쪽으로 갈 수 있을 때
                if col != 99:
                    # 오른쪽 선이 존재한다면
                    if matrix[99 - row][col + 1] == 1:
                        # 반복문 덕분에 col은 1씩 상승하면서 다음에 또 탐색할 것이 때문에 while문 생략
                        matrix[99 - row][col + 1] = 2
                    else:
                        matrix[98 - row][col] = 2
                # 좌우 연결 선이 없다면 위로 올리기
                else:
                    matrix[98 - row][col] = 2

    for i in matrix:
        print(*i)
    # print(f'#{tc} {answer}')
    
