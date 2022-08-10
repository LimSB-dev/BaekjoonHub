def solution(seoul):
    # enumerate를 사용해 index값과 value값을 가져온다.
    for index, value in enumerate(seoul):
        
        # value값이 문제의 조건인 'Kim'이라면
        if value == 'Kim':
            
            # 변수에 대입할 필요 없이 바로 반환
            return f'김서방은 {index}에 있다'
