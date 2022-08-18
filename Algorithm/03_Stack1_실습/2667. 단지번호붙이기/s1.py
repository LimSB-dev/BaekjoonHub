import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input()) + 1):
    arr = input()
    answer = 1
    openning = 0
    for i in arr:
        if i == '(':
            openning += 1
        else:
            openning -= 1

        if openning == -1:
            answer = -1
            break

    if openning != 0:
        answer = -1

    print(f'#{tc} {answer}')
