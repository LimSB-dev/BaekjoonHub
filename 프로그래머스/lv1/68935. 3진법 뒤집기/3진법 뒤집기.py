# 3진법 상에서 앞뒤를 바꾼후 str형태로 내보냄
def reversed_ternary(num):
    if num >= 3:
        return f'{num % 3}' + reversed_ternary(num // 3)
    else:
        return f'{num}'

def solution(n):
    reversed_ternary_n = reversed_ternary(n)
    answer = int(reversed_ternary_n, 3)
    return answer