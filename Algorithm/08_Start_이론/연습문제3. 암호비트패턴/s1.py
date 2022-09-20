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
    n = input()                             # 16진수 입력
    words = ''                              # 빈 문자열 생성

    for num in n:                           # 16진수 하나씩 받기
        two = format(int(num, 16), 'b')     # 16진수 -> 2진수 변환
        two = ('0' * (4 - len(two))) + two  # 16진수 하나당 4비트 만들기
        words += two                        # 2진수들 하나의 문자열로 붙이기

    words = words.strip('0')                # 앞뒤에 있는 0들 지우기

    words = ('0' * (6 - (len(words) % 6))) + words

    for i in range(0, len(words), 6):
        print(table[words[i:i + 6]], end=' ')
    print()
