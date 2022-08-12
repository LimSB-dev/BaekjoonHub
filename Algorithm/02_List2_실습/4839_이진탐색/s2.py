import sys

sys.stdin = open('input.txt')


def number_of_attempts(first_page, last_page, target_page, cnt):
    cnt += 1
    center_page = (first_page + last_page) // 2
    target = target_page
    
    if target_page < center_page:
        last_page = center_page
        return number_of_attempts(first_page, last_page, target, cnt)
    elif target_page > center_page:
        first_page = center_page
        return number_of_attempts(first_page, last_page, target, cnt)
    else:
        return cnt


t = int(input())

for tc in range(1, t + 1):
    answer = 0
    # p: 전체 쪽 수
    # a: a가 찾을 페이지
    # b: b가 찾을 페이지
    pages, target_a, target_b = map(int, input().split())
    
    a_cnt = number_of_attempts(1, pages, target_a, answer)
    b_cnt = number_of_attempts(1, pages, target_b, answer)
    
    if a_cnt > b_cnt:
        answer = 'A'
    elif a_cnt < b_cnt:
        answer = 'B'
    
    print(f'#{tc} {answer}')
