def solution(a, b):
    # a, b 값들 중 무엇이 더 큰지 알지 모르기에 abs()를 사용
    # 가우스의 덧셈정리를 사용
    answer = ((a + b) / 2) * (abs(a - b) + 1)
    
    # a, b가 같은 경우 아무거나 출력
    if a == b:
        answer = a
        
    return answer