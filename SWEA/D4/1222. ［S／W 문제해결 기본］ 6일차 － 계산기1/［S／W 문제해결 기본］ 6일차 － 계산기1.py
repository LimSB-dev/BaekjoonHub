for tc in range(1, 11):
    n = int(input())

    # 중위표기법
    medium = input()

    # 후위표기법
    postfix = ''

    # stack
    stack = []

    for word in medium:
        # 피연산자
        if word not in '()+-*/':
            postfix += word

        # 연산자
        else:

            # * 혹은 /
            if word in '*/':

                # stack이 비거나 우선순위가 낮은 연산자가 나올 때까지 반복
                while stack and stack[-1] in '*/':

                    # stack의 top에 있는 연산자를 후위표기법에 넣기
                    postfix += stack.pop()

                # stack에 push
                stack.append(word)

            # + 혹은 -
            elif word in '+-':

                # stack이 비거나 여는 괄호가 나올 때까지 반복
                while stack and stack[-1] != '(':
                    postfix += stack.pop()

                # stack에 push
                stack.append(word)

            # 닫는 괄효
            elif word == ')':

                # 여는 괄호가 나올 때까지 반복
                while stack[-1] != '(':
                    postfix += stack.pop()

                # 여는 괄호 pop
                stack.pop()

            # 여는 괄호
            else:
                stack.append(word)
    if stack:
        postfix += stack.pop()
        
    # 후위표기법 계산기
    for i in postfix:
        # 피연산자
        if i not in '+-*/':
            stack.append(int(i))
        # 연산자
        else:
            x = stack.pop()
            y = stack.pop()
            if i == '+':
                result = y + x
            if i == '-':
                result = y - x
            if i == '*':
                result = y * x
            if i == '/':
                result = y / x

            stack.append(result)

    print(f'#{tc} {stack.pop()}')
