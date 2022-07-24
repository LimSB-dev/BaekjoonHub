def solution(n):
    answer = 0
    sqrt_n = n**0.5
    
    if sqrt_n == int(sqrt_n): 
        answer = (sqrt_n + 1)**2
    else:
        answer = -1
        
    return answer