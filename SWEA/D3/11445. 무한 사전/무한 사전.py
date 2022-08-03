t = int(input())

for tc in range(1, t + 1):
    answer = 'Y'
    p = list(map(str, input().strip()))
    q = list(map(str, input().strip()))

    # 만약 p의 길이가 10일 때
    if len(p) == 10:
        # p와 q가 같다면
        if p == q:
            # 답은 Y
            answer = 'N'
    # 만약 p의 길이가 10이 아니라면
    else:
        # 만약 q의 마지막이 'a'이고 p와 마지막을 뺀 q가 같다면
        a = q.pop()
        if a == 'a' and p == q:
            answer = 'N'

    print(f'#{tc} {answer}')
