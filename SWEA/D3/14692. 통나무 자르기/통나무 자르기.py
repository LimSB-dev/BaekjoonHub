t = int(input())

for tc in range(1, t+1):
    answer = 0
    n = int(input())

    for i in range(9, 0, -1):
        if not n % 2**i:
            if i % 2:
                answer = 1
                break

    # while True:
    #     if not n % 2:
    #         n //= 2
    #         answer += 1
    #         answer %= 2
    #     else:
    #         break

    print(f'#{tc} {"Alice" if answer else "Bob"}')
