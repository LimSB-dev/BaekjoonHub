import sys
input = sys.stdin.readline

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
answer = 0

for a, b in zip(a_list, b_list):
    answer += abs(a - b)

print(answer // 2)
