bracket_dict = {
    '(': 0,
    '[': 1,
    '{': 2,
    '<': 3,
    '>': 4,
    '}': 5,
    ']': 6,
    ')': 7,
}

for tc in range(1, 11):
    n = int(input())
    brackets = list(input().strip())
    answer = 1

    stack = []

    for bracket in brackets:
        # open bracket
        bracket_num = bracket_dict[bracket]
        if bracket_num < 4:
            stack.append(bracket_num)
        else:
            if bracket_num + stack.pop() != 7:
                answer = 0
                break

    print(f'#{tc} {answer}')
