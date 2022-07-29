t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    li = list(map(int, input().split()))
    answer = 0
    for i in range(1, n-1):
        if li[i - 1] < li[i] < li[i + 1]:
            answer += 1
        elif li[i + 1] < li[i] < li[i - 1]:
            answer += 1

    print(f'#{tc} {answer}')
