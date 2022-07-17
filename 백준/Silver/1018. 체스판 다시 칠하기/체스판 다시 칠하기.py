n, m = map(int, input().split())

li = []
mini = []

for _ in range(n):
    li.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        a = 0
        b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if li[k][l] != 'W':
                        a += 1
                    if li[k][l] != 'B':
                        b += 1
                else:
                    if li[k][l] != 'B':
                        a += 1
                    if li[k][l] != 'W':
                        b += 1
        mini.append(a)
        mini.append(b)
print(min(mini))
