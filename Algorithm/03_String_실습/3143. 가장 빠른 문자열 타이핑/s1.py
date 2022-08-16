import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    word_1, word_2 = input().split()
    cnt = word_1.count(word_2)
    answer += len(word_1)
    answer -= len(word_2) * cnt
    answer += cnt
    print(f'#{tc} {answer}')