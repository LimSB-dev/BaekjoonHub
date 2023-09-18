import sys
input = sys.stdin.readline

a, b = map(int, input().split())

print((a > b) * (b * 2 + 1) + (a <= b) * (a * 2 - 1))
