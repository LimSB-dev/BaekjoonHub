import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

arr = []
for i in range(n):
    coin = int(input())
    arr.append(coin)

cnt = 0

for i in range(n):
    if arr[n - 1 - i] <= k:
        cnt += k // arr[n - 1 - i]
        k %= arr[n - 1 - i]

print(cnt)