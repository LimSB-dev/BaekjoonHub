n = int(input())

for i in range(1, n + 1):
    count = 0
    num = i
    while 0 < i:
        check_i = i % 10
        if check_i in [3, 6, 9]:
            i //= 10
            count += 1
        else:
            i //= 10

    if count == 0:
        print(num, end=' ')
    else:
        print('-' * count, end=' ')