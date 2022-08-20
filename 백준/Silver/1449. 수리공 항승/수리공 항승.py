n, L = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

# 카운팅 정렬
counter = [0] * 1001
for i in arr:
    counter[i] += 1

for idx, value in enumerate(counter):
    if value == 1:
        answer += 1
        for i in range(L):
            if idx + i > 1000:
                break
            else:
                counter[idx + i] = 0

print(answer)
