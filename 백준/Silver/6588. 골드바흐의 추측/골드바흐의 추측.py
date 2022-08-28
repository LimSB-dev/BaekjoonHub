import sys

x = 10**6 + 1
a = [*range(x)]

for i in range(2, 1001):
    if (a[i] == 0): continue
    for j in range(i * 2, x, i):
        if (a[j] != 0): a[j] = 0
a = set(a)
for i in range(3):
    a.remove(i)

b = sorted(list(a))

while True:
    n = int(sys.stdin.readline())
    if (n == 0): break
    for i in b:
        if (n - i in a):
            print('%d = %d + %d' % (n, i, n - i))
            break
