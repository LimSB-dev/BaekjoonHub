t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    li = list(map(int, input().split()))

    print(f'#{tc}', end=' ')
    print(*sorted(li))