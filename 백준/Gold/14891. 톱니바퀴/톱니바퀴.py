import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = 0
gears = [list(map(int, input().strip())) for _ in range(4)]


def rotate(index, d):
    if visited[index]:
        return

    left, right = gears[index][-2], gears[index][2]
    visited[index] = True

    if d == 1:
        gears[index] = [gears[index][-1]] + gears[index][:-1]
    else:
        gears[index] = gears[index][1:] + [gears[index][0]]

    if index < 3:
        next_index = index + 1
        next_left = gears[next_index][-2]

        if right != next_left:
            next_d = d * -1
            rotate(next_index, next_d)

    if index > 0:
        next_index = index - 1
        next_right = gears[next_index][2]

        if left != next_right:
            next_d = d * -1
            rotate(next_index, next_d)


for _ in range(int(input())):
    visited = [False] * 4

    index, d = map(int, input().split())
    index -= 1

    # 회전
    rotate(index, d)


for (idx, gear) in enumerate(gears):
    head = 2**idx if gear[0] else 0
    answer += head

print(answer)
