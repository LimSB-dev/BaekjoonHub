t = int(input())

for tc in range(1, t + 1):
    n = input()
    dict_n = {}
    for i in n:
        if i in dict_n:
            dict_n[i] += 1
        else:
            dict_n.setdefault(i, 1)

    lonely = []
    for key, value in dict_n.items():
        if value % 2 != 0:
            lonely.append(key)

    if len(lonely) == 0:
        print(f'#{tc} Good')
    else:
        lonely.sort()
        print(f'#{tc}', end=' ')
        print(*lonely, sep='')
