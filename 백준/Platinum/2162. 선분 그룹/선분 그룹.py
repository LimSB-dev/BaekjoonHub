import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def is_intersected(a, b):
    x1, y1, x2, y2 = a
    x3, y3, x4, y4 = b

    if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
        if ccw(x1, y1, x2, y2, x3, y3) == 0 and ccw(x1, y1, x2, y2, x4, y4) == 0:
            return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)
        return True
    return False


def find(u):
    if union[u] != u:
        union[u] = find(union[u])
    return union[u]


def merge(u, v):
    u, v = find(u), find(v)
    if u == v:
        return False
    if u < v:
        union[v] = u
    else:
        union[u] = v
    return True


n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
union = list(range(n))

for i in range(n):
    for j in range(i+1, n):
        if is_intersected(lines[i], lines[j]):
            merge(i, j)

union = [find(u) for u in union]
union_cnt = len(set(union))
print(union_cnt)
print(max(union.count(u) for u in set(union)))
