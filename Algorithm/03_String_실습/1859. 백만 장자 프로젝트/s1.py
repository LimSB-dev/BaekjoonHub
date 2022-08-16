import sys
sys.stdin = open('input.txt')

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = 0
    sum_value = 0
    for j in range(n - 1, -1, -1):
        if arr[j] > max_value:
            max_value = arr[j]
        else:
            sum_value += max_value - arr[j]

    print(f'#{i} {sum_value}')
