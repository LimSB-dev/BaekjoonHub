import sys
from itertools import combinations
input = sys.stdin.readline

# 거리 계산
def calc_distance(r1: int, c1: int, r2: int, c2: int):
    return abs(r1 - r2) + abs(c1 - c2)

# 궁수 공격
def attack(archers: list, enemies: list, d: int):
    targets = []
    for archer in archers:
        min_distance = float('inf')
        target = None
        for enemy in enemies:
            distance = calc_distance(
                archer[0], archer[1], enemy[0], enemy[1])
            if distance <= d and distance <= min_distance:
                min_distance = distance
                target = enemy
        if target:
            targets.append(target)
    return targets

# 적 이동
def move_enemies(enemies: list, N: int):
    new_enemies = []
    for enemy in enemies:
        if enemy[0] < N - 1:
            new_enemies.append([enemy[0] + 1, enemy[1]])
    return new_enemies


def solution(matrix: list, N: int, M: int, D: int):
    archer_combinations = list(combinations(range(M), 3))
    max_kill = 0

    for archer_combination in archer_combinations:
        enemies = []
        for j in range(M-1, -1, -1):
            for i in range(N):  
                if matrix[i][j] == 1:
                    enemies.append([i, j])

        kill = 0
        archers = [[N, archer_combination[i]] for i in range(3)]
        while enemies:
            targets = attack(archers, enemies, D)
            for target in targets:
                if target in enemies:
                    enemies.remove(target)
                    kill += 1
            enemies = move_enemies(enemies, N)

        max_kill = max(max_kill, kill)

    print(max_kill)

N, M, D = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(N)]

solution(matrix, N, M, D)