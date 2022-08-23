import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    postfix = input().split()
    stack = []

    # 후위표기법 계산기
    for i in postfix:
        # 피연산자
        if i not in '+-*/.':
            stack.append(int(i))
        # 연산자
        else:
            if i == '.':
                break

            elif len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()

                if i == '+':
                    result = y + x
                if i == '-':
                    result = y - x
                if i == '*':
                    result = y * x
                if i == '/':
                    result = y // x

                stack.append(result)

            else:
                stack.append('error')
                break

    if len(stack) != 1:
        stack.append('error')

    print(f'#{tc} {stack.pop()}')
