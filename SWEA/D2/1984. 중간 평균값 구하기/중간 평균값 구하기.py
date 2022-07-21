t = int(input())

for tc in range(1, t + 1):
    answer = 0
    li = list(map(int, input().split()))
    answer = (sum(li) - min(li) - max(li)) / (len(li) - 2)
    print(f'#{tc} {round(answer)}')