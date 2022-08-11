import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    answer = 0
    # 첫 페이지
    l_a = l_b = 1
    # p: 전체 쪽 수
    # a: a가 찾을 페이지
    # b: b가 찾을 페이지
    p, a, b = map(int, input().split())
    p_a = p_b = p
    
    # 승리시 반복문을 탈출하기 위한 변수
    a_win = 0
    b_win = 0
    
    while True:
        # 중간값
        c_a = int((l_a + p_a) / 2)
        c_b = int((l_b + p_b) / 2)

        # a, b가 이길 경우
        if c_a == a:
            a_win += 1
        if c_b == b:
            b_win += 1

        # 반복문 탈출
        if a_win != b_win or a_win + b_win == 2:
            if not a_win - b_win:
                break
            elif a_win > b_win:
                answer = "A"
            else:
                answer = "B"
        
            break
        
        # 이진 탐색
        if c_a < a:
            l_a = c_a
        else:
            p_a = c_a

        if c_b < b:
            l_b = c_b
        else:
            p_b = c_b

    print(f'#{tc} {answer}')
