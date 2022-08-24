n = int(input())
q = list(range(1, n + 1))
answer = []

while q:
    answer.append(q.pop(0))
    if q:
        q.append(q.pop(0))

print(*answer)
