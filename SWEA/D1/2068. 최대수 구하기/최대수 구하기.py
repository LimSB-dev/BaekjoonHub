t = int(input())

for tc in range(1,t+1):
    li = list(map(int, input().split()))
    print(f'#{tc} {max(li)}')