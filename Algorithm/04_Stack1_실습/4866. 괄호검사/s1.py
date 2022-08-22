import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    mid = 0
    small = 0
    answer = 1
    stack = []
    arr = list(input())
    for i in arr:
        if i == '(':
            stack.append(i)
        elif i == '{':
            stack.append(i)
        elif i == ')':
            if not stack:
                answer = 0
                break
            elif stack[-1] == '(':
                stack.pop(-1)
            else:
                answer = 0
                break
        elif i == '}':
            if not stack:
                answer = 0
                break
            elif stack[-1] == '{':
                stack.pop(-1)
            else:
                answer = 0
                break

    if stack:
        answer = 0

    print(f'#{tc} {answer}')

