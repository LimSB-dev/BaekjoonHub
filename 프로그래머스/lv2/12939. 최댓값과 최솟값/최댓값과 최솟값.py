def solution(s):
    numbers = list(map(int, s.split()))
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    answer = str(min_value) + ' ' + str(max_value)
    
    
    return answer