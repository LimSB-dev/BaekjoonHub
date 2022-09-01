for tc in range(1, 11):
    n = int(input())
    answer = 1
    for i in range(n):
        arr = list(input().split())
        if len(arr) == 4:
            if arr[1] not in '+-*/':
                answer = 0
        else:
            if arr[1] in '+-*/':
                answer = 0

    print(f'#{tc} {answer}')
