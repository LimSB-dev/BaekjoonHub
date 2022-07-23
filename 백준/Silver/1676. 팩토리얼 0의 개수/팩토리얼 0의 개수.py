import math
import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
N = math.factorial(n)
cnt = 0
while True:
  if N < 10 or N % 10 != 0:
    break
  else:
    N //= 10
    cnt += 1
print(f'{cnt}')