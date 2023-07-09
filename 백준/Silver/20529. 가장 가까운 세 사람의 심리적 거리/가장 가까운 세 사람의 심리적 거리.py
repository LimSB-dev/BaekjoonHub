import sys
from itertools import combinations
input = sys.stdin.readline

def find_distance(A, B, C):
    tendency = {
        'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0
    }

    for a, b, c in zip(A, B, C):
        tendency[a] += 1
        tendency[b] += 1
        tendency[c] += 1

    result = 0
    for value in tendency.values():
        if value == 2:
            result += 2

    return result


T = int(input())
for _ in range(T):
    N = int(input())
    students = input().split()
    answer = float('inf')

    # 최소 하나의 MBTI 유형이 3명
    if N > 33:
        print(0)
        continue
    # 최소 하나의 MBTI 유형이 2명
    else:
        for random_students in combinations(students, 3):
            (A, B ,C) = random_students
            distance = find_distance(A, B, C)
            answer = min(answer, distance)
            if answer == 1:
                break

        print(answer)