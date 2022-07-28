for tc in range(1, int(input()) + 1):
    result_list = list(map(str, input().strip()))
    win = 0
    win = 15 - len(result_list)
    win += result_list.count('o')
    if win >= 8:
        answer = 'YES'
    else:
        answer = 'NO'
    print(f'#{tc} {answer}')