import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, hexs = input().split()
    answer = ''

    for num in hexs:
        num = int(num, 16)
        num = format(num, 'b')
        num = '0' * (4 - len(num)) + num
        answer += num
    print(f'#{tc}', answer)