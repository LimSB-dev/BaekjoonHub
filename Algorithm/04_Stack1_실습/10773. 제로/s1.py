import sys
sys.stdin = open('input.txt')

stack = []

for _ in range(int(input())):
    number = int(input())

    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))