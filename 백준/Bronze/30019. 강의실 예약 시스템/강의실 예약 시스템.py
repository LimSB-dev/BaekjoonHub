import sys
input = sys.stdin.readline

n, m = map(int, input().split())
reservations = {i: 0 for i in range(1, n+1)}

for _ in range(m):
    k, s, e = map(int, input().split())

    if reservations[k] <= s:
        reservations[k] = e
        print('YES')
    else:
        print('NO')
