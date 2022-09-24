for tc in range(1, int(input()) + 1):
    words = input()
    answer = 0
    for index, word in enumerate(words):
        alpha = chr(97 + index)
        if alpha == word:
            answer += 1
        else:
            break

    print(f'#{tc} {answer}')