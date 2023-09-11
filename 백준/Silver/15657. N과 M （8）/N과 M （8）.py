import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

result = list(combinations_with_replacement(numbers, m))

# 결과 출력
for r in result:
    print(*r)
