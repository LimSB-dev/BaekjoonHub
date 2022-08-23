import sys
sys.stdin = open('input.txt')


def find_min(row):
    global answer, subset

    # 가지치기 pruning
    if answer < subset:
        return

    # n 행에 도달 시 종료조건
    if row == n:
        if answer > subset:
            answer = subset

    for col in range(n):

        # 아직 방문하지 않은 col일 경우
        if not visited[col]:

            # 방문 갱신
            visited[col] = True

            # 부분집합의 합
            subset += matrix[row][col]

            # 더 깊이 재귀
            find_min(row + 1)

            # 재귀 함수가 바닥까지 가거나 가지치기 당한 후
            # 다시 현재 row로 올라와야한다.
            visited[col] = False
            subset -= matrix[row][col]


for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    # 최소값
    answer = 100

    # 부분합
    subset = 0

    find_min(0)

    print(f'#{tc} {answer}')
