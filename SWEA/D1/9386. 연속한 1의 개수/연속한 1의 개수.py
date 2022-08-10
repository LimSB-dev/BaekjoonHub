t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(input())
    max_value = 0
    cnt = 0
    for i in range(n):
        if int(arr[i])==1:
            cnt += 1
            if max_value < cnt:
                max_value = cnt
        else:
            cnt = 0
    print(f'#{tc} {max_value}')