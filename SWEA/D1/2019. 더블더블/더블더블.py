n = int(input())
answer = []

for i in range(n + 1):
    answer.append(2**i)

print(*answer)