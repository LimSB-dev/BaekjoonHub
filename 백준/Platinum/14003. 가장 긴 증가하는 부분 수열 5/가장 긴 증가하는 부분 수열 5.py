import sys
import bisect
input = sys.stdin.readline

def find_longest_increasing_subsequence(arr):
    dp = [arr[0]]
    prev_indices = [0]
    
    for i in range(1, len(arr)):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
            prev_indices.append(len(dp) - 1)
        else:
            index = bisect.bisect_left(dp, arr[i])
            dp[index] = arr[i]
            prev_indices.append(index)
    
    lis_length = len(dp)
    lis_indices = []
    current_index = len(arr) - 1
    
    while lis_length > 0:
        if prev_indices[current_index] == lis_length - 1:
            lis_indices.append(arr[current_index])
            lis_length -= 1
        current_index -= 1
    
    lis_indices.reverse()
    return len(dp), lis_indices

n = int(input())
arr = list(map(int, input().split()))

lis_length, lis_indices = find_longest_increasing_subsequence(arr)

print(lis_length)
print(*lis_indices)
