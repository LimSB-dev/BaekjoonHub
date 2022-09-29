import sys
sys.stdin = open('input.txt')
from collections import deque

operators = {
    '0': lambda x: x + 1,
    '1': lambda x: x - 1,
    '2': lambda x: x * 2,
    '3': lambda x: x - 10,
}


def bfs(num, depth):

    # queue 생성
    queue = deque([[num, depth]])

    while queue:

        # dequeue
        num, depth = queue.popleft()

        # 가지치기
        if num not in visited and 0 < num < 1111111:

            # 방문 처리
            visited.add(num)

            for i in range(4):

                # 연산
                next_num = operators[f'{i}'](num)

                # 종료 조건
                if next_num == m:
                    return depth

                queue.append([next_num, depth + 1])


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = set()

    answer = bfs(n, 1)

    print(f'#{tc} {answer}')
