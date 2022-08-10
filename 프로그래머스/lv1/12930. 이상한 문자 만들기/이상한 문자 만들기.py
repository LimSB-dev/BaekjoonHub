def solution(s):
    # 정답을 입력 받을 문자열 answer
    answer = ''
    
    # 글자의 index값을 홀수와 짝수 구분하여 소문자 및 대문자로 변환시키기 위한 변수
    cnt = 0
    for i in s:

        # 공백이라면 cnt를 0으로 초기화 후 반복문을 처음부터 다시
        if i == ' ':
            answer += i
            cnt = 0
            continue
            
        # 홀수라면 소문자 추가
        if cnt % 2:
            answer += i.lower()
        # 짝수라면 대문자 추가
        else:
            answer += i.upper()
            
        # 글자의 index값 1씩 증가
        cnt += 1                
    
    return answer