import sys
sys.stdin = open('input.txt')

table = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

for tc in range(1, int(input()) + 1):
    num = input()
    words = ''
    answer = []

    for n in num:
        two = format(int(n, 16), 'b')
        two = ('0' * (4 - len(two))) + two
        words += two

    words = words.strip('0')

    words = ('0' * (6 - (len(words) % 6))) + words

    for i in range(0, len(words), 6):
        answer.append(table[words[i:i + 6]])

    print(*answer)
