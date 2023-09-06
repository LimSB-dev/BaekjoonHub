import sys
input = sys.stdin.readline

n = int(input())
num = [0] * 10

point = 1
start = 1


def calc(n):
    while n > 0:
        num[n % 10] += point
        n //= 10


while start <= n:
    while n % 10 != 9 and start <= n:
        calc(n)
        n -= 1
    if n < start:
        break
    while start % 10 != 0 and start <= n:
        calc(start)
        start += 1
    start //= 10
    n //= 10
    for i in range(10):
        num[i] += (n - start + 1) * point
    point *= 10

print(*num)
