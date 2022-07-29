t = int(input())

for tc in range(1, t + 1):
    n = input()
    answer = 'Yes'
    dict_n = {}
    key = ''
    for i in n:
        if i in dict_n.keys():
            dict_n[i] += 1
        else:
            dict_n.setdefault(i, 1)
            key = i

    if len(dict_n) != 2:
        answer = 'No'
    elif len(dict_n) == 2 and dict_n.get(key) != 2:
        answer = 'No'

    print(f'#{tc} {answer}')
