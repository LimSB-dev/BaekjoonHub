from itertools import combinations

# 소수 판정
def is_prime(num):
    answer = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            answer = False
            break
    return answer

def solution(nums):
    answer = 0
    
    # nums 요소 중 3개 조합
    for three in combinations(nums, 3):
        value = sum(three)
        
        # 조건문에 들어가면 소수
        if is_prime(value): 
            answer += 1
    
    return answer