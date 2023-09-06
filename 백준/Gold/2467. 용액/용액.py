import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
close_zero = [float('inf'), 0]

for i in range(n):
    left = i + 1
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if abs(liquid[i] + liquid[mid]) < abs(sum(close_zero)):
            close_zero = [liquid[i], liquid[mid]]
            if sum(close_zero) == 0:
                break
        if liquid[i] + liquid[mid] < 0:
            left = mid + 1
        else:
            right = mid - 1

print(*close_zero)
