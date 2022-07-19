def solution(arr):
    from math import gcd
    answer = arr[0]
    
    for i in arr:
        answer = answer * i // gcd(answer, i)
    return answer