import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    # 보라색 영역을 담을 변수
    answer = 0
    n = int(input())
    # 10 x 10 배열 생성
    matrix = [[0] * 10 for _ in range(10)]

    # 빨강, 파랑의 영역을 반복문으로 입력 받는다.
    for i in range(n):
        x1, y1, x2, y2, color = map(int, input().split())    
        # 배열에 색칠하기
        for row in range(10):
            for col in range(10):
                if x1 <= row <= x2 and y1 <= col <= y2:
                    matrix[row][col] += color

    # 보라색 영역 개수 세기
    for row in range(10):
        for col in range(10):
            if matrix[row][col] == 3:
                answer += 1

    print(f'#{tc} {answer}')
