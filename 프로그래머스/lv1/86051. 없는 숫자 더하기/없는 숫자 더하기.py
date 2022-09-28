def solution(numbers):
    numbers_set = set(range(1,10))
    
    answer = numbers_set - set(numbers)
    
    return sum(answer)