import sys
input = sys.stdin.readline

N, M = map(int, input().split())
section = list(map(int, input().split()))
section_sum = [0] * (N + 1)

for i in range(1, N + 1):
    section_sum[i] = section_sum[i - 1] + section[i - 1]


for _ in range(M):
    i, j = map(int, input().split())
    print(section_sum[j] - section_sum[i - 1])
