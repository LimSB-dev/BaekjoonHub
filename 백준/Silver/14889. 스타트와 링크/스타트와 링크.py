import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(1, N + 1)]
min_value = 10e9

for start_team in combinations(people, N//2):
    link_team = list(set(people) - set(start_team))
    
    start_comb = list(combinations(start_team, 2))
    link_comb = list(combinations(link_team, 2))

    start_sum = 0
    link_sum = 0

    for i, j in start_comb:
        start_sum += matrix[i - 1][j - 1] + matrix[j - 1][i - 1]
    
    for i, j in link_comb:
        link_sum += matrix[i - 1][j - 1] + matrix[j - 1][i - 1]
    
    value = abs(start_sum - link_sum)

    if value == 0:
        min_value = value
        break

    elif value < min_value:
        min_value = abs(start_sum - link_sum)

print(min_value)