import sys
sys.stdin = open('input.txt', encoding='utf-8')
from functools import reduce
from itertools import combinations


for tc in range(1, int(input()) + 1):
    n, m, c = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    dp = [[0] * (n - m + 1) for _ in range(n)]
    answer = 0

    for row in range(n):
        for col in range(n - m + 1):
            m_arr = []

            for i in range(m):
                m_arr.append(matrix[row][col + i])

            if sum(m_arr) <= c:
                dp[row][col] = reduce(lambda x, y: x ** 2 + y ** 2, m_arr)
            else:
                for j in range(1, m):
                    for arr in combinations(m_arr, j):
                        if sum(arr) <= c:
                            value = reduce(lambda x: x ** 2, m_arr)
                            if value > dp[row][col]:
                                dp[row][col] = value

    print(dp)

    print(f'#{tc} {answer}')
