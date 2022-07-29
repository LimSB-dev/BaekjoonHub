t = int(input())

for tc in range(1, t + 1):
    n = input()
    a, b = 1, 1
    for i in n:
        if i == 'L':
            a, b = a, a + b
        elif i == 'R':
            a, b = a + b, b

    print(f'#{tc} {a} {b}')
