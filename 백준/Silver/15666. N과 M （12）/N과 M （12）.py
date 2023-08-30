import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))
permutation = []
answer = []


def dfs(depth):
    if depth == m:
        answer.append(tuple(sorted(permutation)))
        return
    for i in arr:
        permutation.append(i)
        dfs(depth+1)
        permutation.pop()


dfs(0)

print('\n'.join(' '.join(map(str, i)) for i in sorted(set(answer))))
