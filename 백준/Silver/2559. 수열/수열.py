n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 온도의 합
sum_value = 0

# 시작 온도 설정
for i in range(k):
    sum_value += arr[i]

# 온도의 합: 최대값
answer = sum_value

# Slicing Window
for i in range(n - k):
    sum_value -= arr[i]
    sum_value += arr[i + k]

    if answer < sum_value:
        answer = sum_value

print(answer)