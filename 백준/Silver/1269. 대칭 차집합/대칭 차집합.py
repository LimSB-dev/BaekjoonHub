answer = 0
a, b = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

only_a = set(arr_a) - set(arr_b)
only_b = set(arr_b) - set(arr_a)

answer = list(only_a) + list(only_b)

print(len(answer))
