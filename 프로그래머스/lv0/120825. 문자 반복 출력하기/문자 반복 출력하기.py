def solution(my_string, n):
    answer = ''
    
    for str in my_string:
        answer += str * n
        
    return answer