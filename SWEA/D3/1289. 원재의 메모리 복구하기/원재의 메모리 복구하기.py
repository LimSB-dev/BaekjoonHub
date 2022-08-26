for tc in range(1, int(input()) + 1):
    words = list(input())
    n = len(words)
    answer = 0

    for idx in range(n):

        if words[idx] == '1':
            answer += 1
            for i in range(idx, n):
                if words[i] == '0':
                    words[i] = '1'
                elif words[i] == '1':
                    words[i] = '0'

    print(f'#{tc} {answer}')
