import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    answer = 'ON'
    bit = format(m, 'b')

    if len(bit) >= n:
        for i in range(n):
            if bit[-i] == '0':
                answer = 'OFF'
                break
    else:
        answer = 'OFF'

    print(f'#{tc} {answer}')
