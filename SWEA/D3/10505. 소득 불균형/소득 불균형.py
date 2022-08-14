for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    average = sum(arr) / n
    answer = 0
    for i in arr:
        if average >= i:
            answer += 1
    print(f'#{tc} {answer}')
