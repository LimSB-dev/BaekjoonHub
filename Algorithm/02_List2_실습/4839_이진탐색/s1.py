import sys

sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    answer = 0
    # p: 전체 쪽 수
    # a: a가 찾을 페이지
    # b: b가 찾을 페이지
    p, a, b = map(int, input().split())
    
    # 첫 페이지
    l_a = l_b = 1

    # 마지막 페이지
    p_a = p_b = p
    
    # 승리시 반복문을 탈출하기 위한 변수
    a_win = 0
    b_win = 0

    # 이진 탐색
    while True:
        # 중간값
        # int() 형 변환은 기본적으로 내림
        c_a = int((l_a + p_a) / 2)
        c_b = int((l_b + p_b) / 2)

        # a, b가 이길 경우
        if c_a == a:
            a_win += 1
        if c_b == b:
            b_win += 1

        # 반복문 탈출
        if a_win != b_win or a_win + b_win == 2:
            if a_win > b_win:
                answer = "A"
            elif a_win < b_win:
                answer = "B"
            break

        # 중간값과 a, b가 찾을 페이지 대소 비교
        if c_a < a:
            l_a = c_a
        else:
            p_a = c_a
        if c_b < b:
            l_b = c_b
        else:
            p_b = c_b

    print(f'#{tc} {answer}')
