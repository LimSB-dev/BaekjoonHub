from itertools import combinations


def find_min(array):
    global answer
    taste_one = 0
    taste_two = 0

    # A 음식
    for two_arr in combinations(array, 2):
        row, col = two_arr[0], two_arr[1]
        taste_one += matrix[row][col] + matrix[col][row]

    difference = set(range(n)) - set(array)

    # B 음식
    for two_arr in combinations(difference, 2):
        row, col = two_arr[0], two_arr[1]
        taste_two += matrix[row][col] + matrix[col][row]

    result = abs(taste_one - taste_two)

    if answer > result:
        answer = result


INF = 999999999

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    answer = INF

    for arr in combinations(range(n), n//2):
        find_min(arr)

    print(f'#{tc} {answer}')
