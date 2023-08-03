import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def solution():
    def find_set(node):
        if parents[node] != node:
            parents[node] = find_set(parents[node])
        return parents[node]

    def union(x, y):
        x, y = find_set(x), find_set(y)
        parents[x] = y

    n, m = map(int, input().split())
    parents = list(range(n + 1))

    for i in range(m):
        v1, v2 = map(int, input().split())

        if find_set(v1) == find_set(v2):
            print(i + 1)
            return
        else:
            union(v1, v2)

    print(0)
    return


solution()
