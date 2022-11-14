for tc in range(1, int(input()) + 1):
    n = int(input())
    L = [list(map(int, input().split())) for _ in range(n)]

    if n < 3:
        print(f'#{tc} TAK')
        continue

    v1 = (L[0][0] - L[1][0], L[0][1] - L[1][1], L[0][2] - L[1][2])

    for i in range(2, n):
        v2 = (L[0][0] - L[i][0], L[0][1] - L[i][1], L[0][2] - L[i][2])
        if v1[0] * v2[1] == v1[1] * v2[0] and v1[0] * v2[2] == v1[2] * v2[0]:
            continue
        break
    else:
        print(f'#{tc} TAK')
        continue
    u = (v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0])
    for A in L:
        if (L[0][0] - A[0]) * u[0] + (L[0][1] - A[1]) * u[1] + (L[0][2] - A[2]) * u[2] != 0:
            print(f'#{tc} NIE')
            break
    else:
        print(f'#{tc} TAK')
