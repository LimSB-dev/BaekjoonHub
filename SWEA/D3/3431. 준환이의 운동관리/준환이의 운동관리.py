t = int(input())

for tc in range(1, t + 1):
    answer = 0
    L, U, X = map(int, input().split())
    if L > X:
        answer = L - X
    elif U < X:
        answer = -1
    print(f'#{tc} {answer}')
