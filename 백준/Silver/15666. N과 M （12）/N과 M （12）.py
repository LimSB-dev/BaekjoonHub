import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(map(int, input().split())))
answer = [0]


def dfs(depth):
    if depth == m:
        print(*answer[1:])
        return
    for i in arr:
        if i < answer[-1]:
            continue
        answer.append(i)
        dfs(depth+1)
        answer.pop()


dfs(0)
