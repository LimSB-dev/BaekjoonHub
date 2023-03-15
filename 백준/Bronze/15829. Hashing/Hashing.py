L = int(input())
alpha_list = list(map(str, input().strip()))
r = 31
M = 1234567891
answer = 0

for idx, alpha in enumerate(alpha_list):
    hash_value = ord(alpha) - 96
    answer += hash_value * r**idx

print(answer % M)