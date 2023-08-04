import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def find(v):
    if v == root[v]:
        return v
    root[v] = find(root[v])
    return root[v]


def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    root[r1] = r2


def ub(key):
    s, e = 0, m - 1
    while s <= e:
        mid = (s + e) // 2
        if my[mid] <= key:
            s = mid + 1
        else:
            e = mid - 1
    return s


n, m, k = map(int, input().split())

my = list(map(int, input().split()))
root = [i for i in range(m + 1)]
enemy = list(map(int, input().split()))

my.sort()

for num in enemy:
    idx = ub(num)
    choice_idx = find(idx)
    print(my[choice_idx])
    union(choice_idx, choice_idx + 1)
