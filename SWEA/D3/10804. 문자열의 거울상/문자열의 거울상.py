t = int(input())

for tc in range(1, t + 1):
    n = input()

    answer = ''
    for i in n:
        if i == 'b':
            answer += 'd'
        elif i == 'd':
            answer += 'b'
        elif i == 'p':
            answer += 'q'
        elif i == 'q':
            answer += 'p'

    print(f'#{tc} {answer[::-1]}')
