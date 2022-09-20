import sys
sys.stdin = open('input.txt')

table = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    code = ''
    answer = 0
    cnt = 0
    check = 0

    for row in range(n):
        num = matrix[row].strip('0')
        if num:
            num = '0' * (56 - len(num)) + num
            code = num
            break

    for i in range(0, 56, 7):
        cnt += 1
        num = table[code[i:i + 7]]
        if cnt % 2 == 0:
            check += num
        else:
            check += num * 3
        answer += num

    if check % 10 != 0:
        answer = 0

    print(f'#{tc} {answer}')
