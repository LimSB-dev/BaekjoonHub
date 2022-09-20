import sys
sys.stdin = open('input.txt', encoding='utf-8')


def dfs(value, result, depth):
    global answer

    for i in range(2):
        # 종료조건
        if answer:
            return

        if value == n:
            answer = result
            return

        # 가지치기
        if value > n:
            return

        if i == 0:
            value += 2 ** (-depth)
            result += '1'
        else:
            result += '0'

        depth += 1

        if depth == 14:
            answer = 'overflow'
            return

        dfs(value, result, depth)

        # 가지치기 혹은 종료조건 이후
        depth -= 1
        result = result[:-1]
        value -= 2 ** (-depth)


for tc in range(1, int(input()) + 1):
    n = float(input())
    answer = ''

    dfs(0, '', 1)

    print(f'#{tc} {answer}')
