import string

def convert(num, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    return convert(q, base) + number[r] if q else number[r]

def solution(n, t, m, p):
    answer = []
    number = 0
    
    while len(answer) <= t * m:
        nums = convert(number, n)
        for num in nums:
            answer.append(num)
        number += 1
        
    result = []
    for i in range(p - 1, len(answer), m):
        result.append(answer[i])
    
    return ''.join(result[:t])