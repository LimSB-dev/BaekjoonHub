import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    str1 = input()
    str2 = input()

    if str2.count(str1) != 0:
        answer = 1 

    print(f'#{tc} {answer}')
