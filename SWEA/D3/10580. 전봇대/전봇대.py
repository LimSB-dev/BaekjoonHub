for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = []
    answer = 0

    for i in range(n):
        a, b = map(int, input().split())
        arr.append([a, b])

    for i in range(n - 1):
        
        for j in range(i + 1, n):
            
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                answer += 1
                
            elif arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                answer += 1
                
    print(f'#{tc} {answer}')
