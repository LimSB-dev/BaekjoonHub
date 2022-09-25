n, k = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr, reverse=True)

target = sorted_arr[k - 1]

print(target)
