def solution(a, b):
    answer = ((a + b) / 2) * (abs(a - b) + 1)
    
    if a == b:
        answer = a
        
    return answer