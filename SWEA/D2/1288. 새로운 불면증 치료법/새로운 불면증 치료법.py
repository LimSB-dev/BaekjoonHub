t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    li = []
    k = 1
    while True:
        k_N = k * n
        li.extend(str(k_N).strip())
        k += 1
        if len(set(li)) == 10:
            break

    print(f'#{tc} {k_N}')