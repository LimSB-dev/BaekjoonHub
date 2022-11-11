for tc in range(1, int(input()) + 1):
    answer = 'no'
    a, b = map(str, input().split())

    a_length = len(a)
    b_length = len(b)

    for i in range(max(a_length, b_length), (a_length * b_length) + 1):
        if i % a_length == 0 and i % b_length:
            lcm = i

    a = a * (i // a_length)
    b = b * (i // b_length)

    if a == b:
        answer = 'yes'

    print(f'#{tc} {answer}')
