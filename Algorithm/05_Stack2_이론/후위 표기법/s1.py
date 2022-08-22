import sys
sys.stdin = open('input.txt')

operator = ['(', ')', '+', '-', '*', '/']

for tc in range(1, int(input()) + 1):
    # 중위표기법 입력
    arr = list(input())

    # 후위표기법 출력
    answer = ''

    # 연산자 스택
    stack = []

    for i in arr:
        # 연산자 및 괄호
        if i in operator:

            # stack이 비어있거나 여는 괄호
            if not stack or i == '(':
                stack.append(i)

            # * 혹은 /
            elif i in '*/':

                # stack이 비거나 stack의 top 우선순위가 낮을 때까지 반복
                while stack and stack[-1] in '*/':
                    # 스택에서 pop
                    answer += stack.pop()

                stack.append(i)

            # + 혹은 -
            elif i in '+-':

                # stack이 비거나 stack의 top이 여는 괄호일 때까지 반복
                while stack and stack[-1] != '(':
                    # 스택에서 pop
                    answer += stack.pop()

                stack.append(i)

            # 닫는 괄호
            elif i == ')':
                # 여는 괄호일 때까지 반복
                while stack[-1] != '(':
                    answer += stack.pop()

                stack.pop()

        # 피연산자
        else:
            answer += i

    # stack에 남은 연산자를 후위표기법에 저장
    while stack:
        answer += stack.pop()

    print(f'#{tc} {answer}')
