from collections import deque


def solution(num):
    num = deque(str(num))
    for number in range(len(num) // 2):
        if num.popleft() != num.pop():
            return
    return True


for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    answer = 0

    for i in range(a, b + 1):
        if solution(i):
            if i**0.5 == int(i**0.5) and solution(int(i**0.5)):
                answer += 1

    print(f'#{tc} {answer}')
