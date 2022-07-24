def solution(x):
    answer = True
    tmp = x
    sum = 0
    
    while x > 0:
        sum += x % 10
        x //= 10
    
    if tmp % sum != 0:
        answer = False
    return answer