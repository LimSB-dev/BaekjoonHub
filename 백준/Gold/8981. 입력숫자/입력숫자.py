n = int(input())
x = [0] * 31
y = list(map(int, input().split()))

start = 0
for i in y:
    while x[start] != 0:
        start = (start + 1) % n
    x[start] = i
    start = (start + i) % n

print(n)
print(*x[:n])
