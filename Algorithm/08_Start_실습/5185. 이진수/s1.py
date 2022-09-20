import sys
sys.stdin = open('input.txt', encoding='utf-8')

converter = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, int(input()) + 1):
    n, hexs = input().split()
    answer = ''

    for num in hexs:
        if num in converter:
            num = converter[num]
        num = int(num)

        num = format(num, 'b')

        if len(num) != 4:
            num = '0' * (4 - len(num)) + num

        answer += num

    print(f'#{tc} {answer}')
