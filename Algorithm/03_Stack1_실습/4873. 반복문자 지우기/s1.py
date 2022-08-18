import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = []
    words = input()
    for word in words:
        if answer:
            if answer[-1] != word:
                answer.append(word)
            else:
                answer.pop()
        else:
            answer.append(word)

    print(f'#{tc} {len(answer)}')
