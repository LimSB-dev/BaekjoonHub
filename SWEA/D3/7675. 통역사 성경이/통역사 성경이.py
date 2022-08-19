def is_name(word):
    tmp = word
    # 첫 글자가 대문자
    if tmp[0].isupper():
        tmp = tmp[1:]
    else:
        return False

    # 남은 글자가 없을 경우
    if not tmp:
        return True

    # 모두 영어 소문자일 경우
    for alpha in tmp:
        # 소문자
        if not 97 <= ord(alpha) <= 122:
            return False
    return True


end = ['!', '?', '.']

for tc in range(1, int(input()) + 1):
    answer = []
    n = int(input())
    arr = list(input().split())
    name = 0
    for i in arr:
        if i[-1] in end:
            if is_name(i[:-1]):
                name += 1
            answer.append(name)
            name = 0
            continue

        if is_name(i):
            name += 1

    print(f'#{tc}', *answer)
