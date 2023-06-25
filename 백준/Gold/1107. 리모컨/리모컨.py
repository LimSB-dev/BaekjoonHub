import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))

# 1. 100번에서 +, -로만 이동하는 경우
ans = abs(N - 100)

# 2. 0 ~ 1000000까지 모든 채널을 돌면서
for i in range(1000001):
    # 2-1. i를 누를 수 있는지 확인
    for j in str(i):
        if int(j) in broken:
            break
    else:
        # 2-2. i를 누른 후 +, -로만 이동하는 경우
        ans = min(ans, abs(N - i) + len(str(i)))

print(ans)