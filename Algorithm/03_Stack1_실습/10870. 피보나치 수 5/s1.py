import sys
sys.stdin = open('input.txt')

n = int(input())
a = 0
b = 1

if n > 0:
    for _ in range(n):
        a, b = b, a + b

print(a)
