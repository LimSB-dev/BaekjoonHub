import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = float('inf')
lp = 0
rp = 0
sum_value = 0

while lp != n:
    if rp == n:
        if sum_value >= s:
            answer = min(answer, rp-lp)
            if answer == 1:
                break
            sum_value -= arr[lp]
            lp += 1
        else:
            break
    else:
        if sum_value >= s:
            answer = min(answer, rp-lp)
            if answer == 1:
                break
            sum_value -= arr[lp]
            lp += 1
        else:
            sum_value += arr[rp]
            rp += 1

print(answer if answer != float('inf') else 0)