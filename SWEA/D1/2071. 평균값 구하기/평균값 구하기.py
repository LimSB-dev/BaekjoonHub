for tc in range(1, int(input()) + 1):
    li = list(map(int, input().split()))
    print(f'#{tc} {round(sum(li) / len(li))}')