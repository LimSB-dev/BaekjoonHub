'''
소수 판정
에라토스테네스의 체 (알고리즘 개선)
범위를 2에서 n까지 모든 정수를 다 탐색하지 않고
2에서 n의 제곱근까지 탐색해서 소수 판정

================================================
모든 정수를 탐색하지 않고 n의 제곱근까지만 탐색하는 이유

n이 소수가 아니라면 n = a * b 로 표현이 가능하다.
이때 a, b는 1과 n이 아닌 자연수이다.

m = sqrt(n) 이라하면 n = m * m 이라 할 수 있다.

즉, a * b = m * m이다.
이 상태에라면 아래 3가지 조건 중 1개를 반드시 만족한다.
1) a == m and b == m
2) a < m and b > m
3) a > m and b < a

n이 소수가 아니라면 n의 약수들의 쌍 중 반드시 하나는
n의 제곱근 m과 같거나 작다는 것을 알 수 있다.

때문에 2에서 sqrt(n)까지 탐색하면 된다.
단, sqrt(n)도 범위에 포함 시켜주어야하기 때문에 1을 더한다.
'''

def is_Prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    
    for i in range(2,n + 1):
        if is_Prime(i):
            answer +=1
    return answer