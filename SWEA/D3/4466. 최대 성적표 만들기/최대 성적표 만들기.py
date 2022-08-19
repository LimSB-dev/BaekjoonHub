for tc in range(1, int(input()) + 1):
    answer = 0
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(k):
        answer += arr[i]
        
    print(f'#{tc} {answer}')
