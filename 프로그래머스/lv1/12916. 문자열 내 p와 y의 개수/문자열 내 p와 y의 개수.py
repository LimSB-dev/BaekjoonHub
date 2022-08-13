def solution(s):
    answer = False
    p_cnt = s.lower().count('p')
    y_cnt = s.lower().count('y')

    if p_cnt - y_cnt == 0:
        answer = True
    return answer
