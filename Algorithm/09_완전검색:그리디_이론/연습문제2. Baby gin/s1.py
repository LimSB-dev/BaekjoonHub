from itertools import permutations
import sys
sys.stdin = open('input.txt')


def baby_gin(array):
    array = list(array)
    array.sort()
    A, B, C = array
    if (A == B and B == C) or (A + 1 == B and B + 1 == C):
        return True
    return False


for tc in range(1, int(input()) + 1):
    numbers = list(map(int, input().strip()))
    answer = False
    for arr in permutations(numbers, 3):
        if baby_gin(arr):
            arr = list(arr)
            difference = numbers.copy()

            for i in arr:
                if i in difference:
                    difference.remove(i)

            if baby_gin(difference):
                answer = True
                break

    print(f'#{tc} {answer}')