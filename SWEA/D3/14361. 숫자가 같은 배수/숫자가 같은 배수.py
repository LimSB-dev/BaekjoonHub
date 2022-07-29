for tc in range(1, int(input()) + 1):
    n = input()
    answer = 'impossible'
    list_n = list(map(int, n.strip()))
    for i in range(2, 10):
        now_value = i * int(n)
        now_value_list = list(map(int, str(now_value).strip()))
        for j in list_n:
            if j in now_value_list:
                now_value_list.remove(j)
        if len(now_value_list) == 0:
            answer = 'possible'

    print(f'#{tc}', end=' ')
    print(answer)
