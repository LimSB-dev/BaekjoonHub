def solution(s1, s2):
    answer = 0
    
    for num1 in s1:
        for num2 in s2:
            if num1 == num2 :
                answer += 1
    
    return answer