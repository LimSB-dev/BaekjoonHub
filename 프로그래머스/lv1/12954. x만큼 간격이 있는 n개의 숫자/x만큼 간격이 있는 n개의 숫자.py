def solution(x, n):
    answer = []
    max_n = n
    while n > 0:
        n -= 1
        answer.append(x * (max_n - n))
    return answer