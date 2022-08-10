t = int(input())
 
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
 
    for row in range(n):
        cnt = 0
        for col in range(m):
            if arr[row][col]:
                cnt += 1
                if answer < cnt:
                    answer = cnt
            else:
                cnt = 0
    for col in range(m):
        cnt = 0
        for row in range(n):
            if arr[row][col]:
                cnt += 1
                if answer < cnt:
                    answer = cnt
            else:
                cnt = 0
 
    print(f"#{tc} {answer}")