import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr = arr[1:]

    avg = sum(arr) / N

    over_avg = 0
    for i in arr:
        if i > avg:
            over_avg += 1

    answer = over_avg / N * 100

    print(f'{answer:.3f}%')