import sys
sys.stdin = open('input.txt')


def find_min(row, sum_value):
    global answer

    # 부분집합의 합이 최솟값보다 클 경우 가지치기
    if sum_value > answer:
        return

    # n 행까지 도달 시 최솟값과 대소비교
    if row == n:
        if sum_value < answer:
            answer = sum_value
        return

    for col in range(n):
        if not visited[col]:
            visited[col] = True
            sum_value += matrix[row][col]

            find_min(row + 1, sum_value)

            # 재귀 함수가 바닥까지 가거나 가지치기 당한 후
            # 다시 현재 row로 올라와야한다.
            visited[col] = False
            sum_value -= matrix[row][col]


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    # 최소 생산 비용
    answer = 1500

    find_min(0, 0)

    print(f'#{tc} {answer}')
