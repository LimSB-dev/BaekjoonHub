import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
answer = set()

for comb in permutations(arr, m):
    answer.add(comb)

answer = sorted(list(answer))

print('\n'.join(' '.join(map(str, row)) for row in answer))
