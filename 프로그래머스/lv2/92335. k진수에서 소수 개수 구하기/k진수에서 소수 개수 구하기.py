# n을 k진법으로 변환
def trans(N, K):
    if N >= K:
        trans_N = N % K
        N //= K
        return f'{trans(N, K)}' + f'{trans_N}'
    else:
        return N

# 소수 판별
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0 
    arr = list(trans(n, k).split('0'))
    for i in arr:
        if i and i != '1':
            if is_prime(int(i)):
                answer += 1
            
    return answer