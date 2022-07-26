t = int(input())

li = [2, 3, 5, 7, 11]

for tc in range(1, t + 1):
    n = int(input())
    answer = [0] * 5
    for i in range(5):
        while n % li[i] == 0:
            answer[i] += 1
            n //= li[i]

    print(f'#{tc}', end=' ')
    print(*answer)
