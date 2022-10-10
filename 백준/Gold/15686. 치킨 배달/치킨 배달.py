from itertools import combinations


def find_min(chicken, houses):
    total = 0

    for house in houses:
        min_dist = INF
        h_row, h_col = house
        for c_row, c_col in chicken:
            dist = abs(h_row - c_row) + abs(h_col - c_col)

            if min_dist > dist:
                min_dist = dist

        total += min_dist

        if total > answer:
            return INF

    return total


INF = 999999999
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = INF
houses = []
chickens = []

for row in range(n):
    for col in range(n):
        value = matrix[row][col]

        if value == 1:
            houses.append([row, col])
        elif value == 2:
            chickens.append([row, col])

for chicken in combinations(chickens, m):
    distance = find_min(chicken, houses)

    if distance < answer:
        answer = distance

print(answer)
