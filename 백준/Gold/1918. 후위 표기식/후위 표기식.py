import sys
input = sys.stdin.readline

# 중위 표기식 -> 후위 표기식


def infix_to_postfix(infix):
    stack = []
    postfix = []
    for i in infix:
        if i.isalpha():  # 피연산자
            postfix.append(i)
        else:  # 연산자
            if i == '(':
                stack.append(i)
            elif i == '*' or i == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    postfix.append(stack.pop())
                stack.append(i)
            elif i == '+' or i == '-':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
    while stack:
        postfix.append(stack.pop())
    return postfix


infix = input().rstrip()

print(''.join(infix_to_postfix(infix)))
