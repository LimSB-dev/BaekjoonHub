t = int(input())

for tc in range(1, t+1):
    words = input()
    word = ''

    for i in words:
        word += i
        answer = len(word)
        if word == words[answer:(answer * 2)]:
            break

    print(f'#{tc} {answer}')