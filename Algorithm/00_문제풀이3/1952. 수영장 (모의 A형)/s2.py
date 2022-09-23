import sys
sys.stdin = open('input.txt')


def bit(num):
    words = ''
    for j in range(3, -1, -1):
        words += '1' if num & (1 << j) else '0'
    return words


T = int(input())

for tc in range(1, T + 1):
    result = ''
    answer = []

    for n in input():
        result += bit(int(n, 16))

    while result:
        answer.append(int(result[:7], 2))
        result = result[7:]

    print(*answer)