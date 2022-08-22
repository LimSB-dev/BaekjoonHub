import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    answer = 0
    # 후위표기법 계산기
    string = input()
    stack = []
    for i in string:
        # 연산자
        if i in '+-*/':
            a = stack.pop()
            b = stack.pop()

            if i == '+':
                c = b + a

            elif i == '-':
                c = b - a

            elif i == '*':
                c = b * a

            elif i == '/':
                c = b / a

            stack.append(c)

        # 피연산자
        else:
            stack.append(int(i))

    answer = stack[-1]

    print(f'#{tc} {answer}')
