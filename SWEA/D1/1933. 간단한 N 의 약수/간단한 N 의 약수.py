n = int(input())
answer = []

for i in range(1, n + 1):
    if n % i == 0:
        answer.append(i)

print(*answer)