import sys
from itertools import combinations
input = sys.stdin.readline

def get_sum(comb):
    sum = 0
    for i, j in comb:
        sum += matrix[i - 1][j - 1] + matrix[j - 1][i - 1]
    return sum

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
min_value = 10e9

for i in range(2, N//2 + 1):
    for start_team in combinations(range(N), i):
        link_team = list(set(range(N)) - set(start_team))
        
        start_comb = list(combinations(start_team, 2))
        link_comb = list(combinations(link_team, 2))

        start_sum = get_sum(start_comb)
        link_sum = get_sum(link_comb)

        min_value = min(abs(start_sum - link_sum), min_value)

        if min_value == 0:
            break
    if min_value == 0:
        break

print(min_value)
