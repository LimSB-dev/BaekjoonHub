import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

brackets = list(input().strip())
answer = 0
iron = 0

for index, bracket in enumerate(brackets):
    if bracket == '(':
        iron += 1
    else:
        iron -= 1
        if brackets[index-1] == '(':
            answer += iron
        else:
            answer += 1

print(answer)
