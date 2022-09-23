n, m = map(int, input().split())
arr = list(range(n))
leaf = []
for _ in range(m - 1):
    leaf.append(arr.pop())

answers = []
for i in range(n - m):
    answers.append([arr[i], arr[i + 1]])

for i in range(m - 1):
    answers.append([arr[-1], leaf[i]])

for answer in answers:
    print(*answer)
