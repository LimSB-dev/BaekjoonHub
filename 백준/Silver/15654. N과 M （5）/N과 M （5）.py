import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

selected = [0] * m

def dfs(depth):
    if depth == m:
        print(*selected)
        return

    for i in range(n):
        num = nums[i]
        if num not in selected:
            selected[depth] = nums[i]
            dfs(depth + 1)
            selected[depth] = 0

dfs(0)