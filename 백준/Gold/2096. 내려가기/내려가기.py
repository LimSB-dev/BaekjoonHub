import sys
input = sys.stdin.readline

n = int(input())

dp_max = dp_min = list(map(int, input().split()))

for _ in range(1, n):
    a, b, c = map(int, input().split())

    # 현재 위치에서의 최대값 구하기
    dp_max = [
        max(dp_max[0], dp_max[1]) + a,
        max(dp_max[0], dp_max[1], dp_max[2]) + b,
        max(dp_max[1], dp_max[2]) + c
    ]

    # 현재 위치에서의 최소값 구하기
    dp_min = [
        min(dp_min[0], dp_min[1]) + a,
        min(dp_min[0], dp_min[1], dp_min[2]) + b,
        min(dp_min[1], dp_min[2]) + c
    ]

max_value = max(dp_max)
min_value = min(dp_min)

print(max_value, min_value)
