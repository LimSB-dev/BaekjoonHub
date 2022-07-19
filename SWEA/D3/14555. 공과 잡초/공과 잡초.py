t = int(input())

for tc in range(1, t+1):
    field = list(map(str, input().strip()))
    count = 0
    index = 0
    for i in field:
        if i == '(':
            count += 1
        elif i == ')':
            if field[index] == '|':
                count += 1
            else:
                continue
        else:
            continue

        index += 1

    print(f'#{tc} {count}')
