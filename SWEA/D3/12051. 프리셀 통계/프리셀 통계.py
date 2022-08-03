t = int(input())

for tc in range(1, t + 1):
    answer = 'Possible'
    check = True
    n, p_d, p_g = map(int, input().split())
    if (p_g == 100 and p_d != 100) or (p_g == 0 and p_d != 0):
        answer = 'Broken'
    else:
        for i in range(1, n + 1):
            if (i*p_d) / 100 == (i*p_d) // 100:
                check = False
                break

        if check:
            answer = 'Broken'

    print(f'#{tc} {answer}')
