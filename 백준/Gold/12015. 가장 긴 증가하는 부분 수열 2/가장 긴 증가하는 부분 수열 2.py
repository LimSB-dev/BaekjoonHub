import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0]
for i in range(n):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        left, right = 0, len(dp)-1
        while left < right:
            mid = (left+right)//2
            if dp[mid] < arr[i]:
                left = mid+1
            else:
                right = mid
        dp[right] = arr[i]

print(len(dp)-1)
