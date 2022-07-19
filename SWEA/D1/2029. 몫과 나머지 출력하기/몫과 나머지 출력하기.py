t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    print(f'#{tc} {a // b} {a % b}')