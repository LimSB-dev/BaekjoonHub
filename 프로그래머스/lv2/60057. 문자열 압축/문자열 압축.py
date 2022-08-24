def find_min(words, num):
    result = ''
    cnt = 1
    while words:
        target = words[:num]
        words = words[num:]
        if target == words[:num]:
            cnt += 1
        else:
            if cnt <= 1:
                result += target
            else:
                result += str(cnt) + target
            cnt = 1
    return result


def solution(s):
    n = len(s)
    answer = n
    for i in range(1, (n // 2) + 1):
        # 약수일 경우
        # if n % i == 0:
        word = find_min(s, i)

        if answer > len(word):
            answer = len(word)
            print(word)
    return answer