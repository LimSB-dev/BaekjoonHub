result = []
for tc in range(1, int(input()) + 1):
    n, v = map(int, input().split())
    answer = 0
    path = 0
    cnt = 1

    if n == 1:
        answer = 0
    elif n == 2:
        answer = 1
    else:
        if v != 1:
            while v != 1:
                if v == 2:
                    path = 3
                elif v == 3:
                    path = 2
                answer += 1
                v //= 2

            while v <= n:
                if cnt == 1:
                    cnt += 1
                    if path == 2:
                        v = v * 2
                        continue
                    else:
                        v = (v * 2) + 1
                        continue
                answer += 1
                v *= 2
        else:
            while v <= n:
                answer += 1
                v *= 2
            answer -= 1

    result.append(f'#{tc} {answer}')

print('\n'.join(result))
