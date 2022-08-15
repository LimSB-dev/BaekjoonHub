length, height = map(int, input().split())
n = int(input())

height_counter = [0] * (height)
length_counter = [0] * (length)

for _ in range(n):
    direction, location = map(int, input().split())

    # 세로로 잘라 가로길이 만들기
    if direction == 0:
        height_counter[location] += 1

    # 가로로 잘라 세로길이 만들기
    else:
        length_counter[location] += 1

max_height = 0
max_length = 0

cnt = 0
for i in range(length):
    cnt += 1
    if length_counter[i] != 0:
        cnt = 1

    if max_length < cnt:
        max_length = cnt

cnt = 0
for i in range(height):
    cnt += 1
    if height_counter[i] != 0:
        cnt = 1

    if max_height < cnt:
        max_height = cnt

print(max_length * max_height)
