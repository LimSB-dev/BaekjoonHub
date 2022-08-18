import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    answer = []
    n, words = map(int, input().split())
    words = str(words)
    for word in words:
        if answer:
            if answer[-1] != word:
                answer.append(word)
            else:
                answer.pop()
        else:
            answer.append(word)

    print(f'#{tc}', int(''.join(answer)))
