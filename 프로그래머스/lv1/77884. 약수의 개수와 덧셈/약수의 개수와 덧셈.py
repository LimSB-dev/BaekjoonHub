# 제곱근이 있다면 약수의 개수는 홀수 없다면 짝수
def count_divisor(num):
    if num**0.5 == int(num**0.5):
        num *= -1
    return num

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += count_divisor(i)
    return answer
