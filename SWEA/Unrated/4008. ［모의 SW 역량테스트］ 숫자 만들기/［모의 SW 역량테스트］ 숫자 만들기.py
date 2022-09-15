from collections import deque
from copy import deepcopy

operator = ['+', '-', '*', '/']


def cal_result(numbers, operators, stack):

    # queue가 비어있을 경우 DFS 종료
    if not numbers:
        global min_value, max_value
        value = stack.pop()
        if min_value > value:
            min_value = value
        if max_value < value:
            max_value = value
        return

    numbers_copy = deepcopy(numbers)
    stack_num = stack.pop()
    deque_num = numbers_copy.popleft()

    for i in range(4):
        if operators[i] != 0:
            operators[i] -= 1
            if i == 0:
                result = stack_num + deque_num
            elif i == 1:
                result = stack_num - deque_num
            elif i == 2:
                result = stack_num * deque_num
            elif i == 3:
                result = stack_num / deque_num

            stack.append(int(result))

            cal_result(numbers_copy, operators, stack)

            # 재귀의 끝까지 도달한 경우
            operators[i] += 1


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    operators = list(map(int, input().split()))
    numbers = deque(map(int, input().split()))
    stack = []

    min_value = INF
    max_value = INF * -1

    number = numbers.popleft()
    stack.append(number)

    cal_result(numbers, operators, stack)

    answer = max_value - min_value

    print(f'#{tc} {answer}')
