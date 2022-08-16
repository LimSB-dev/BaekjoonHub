import sys
sys.stdin = open('input.txt')


def even_odd(num):
    if num % 2 == 0:
        num //= 2
        return num
    else:
        num //= 2
        num += 1
        return num


for tc in range(1, int(input()) + 1):
    answer = 0
    n = int(input())

    counter = [0] * 201

    for i in range(n):
        room1, room2 = map(int, input().split())

        room1 = even_odd(room1)
        room2 = even_odd(room2)

        if room1 > room2:
            room1, room2 = room2, room1

        for corridor in range(room1, room2 + 1):
            counter[corridor] += 1

    answer = max(counter)

    print(f'#{tc} {answer}')
