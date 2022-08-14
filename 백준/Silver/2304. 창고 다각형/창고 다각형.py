n = int(input())
pillar = [list(map(int, input().split())) for _ in range(n)]
answer = []

counter = [0] * 1001
for i in pillar:
    counter[i[0]] += i[1]

max_value = max(counter)

two_max = False
if counter.count(max_value) > 1:
    two_max = True

now_height = 0
cnt = 0
for value in counter:
    if value == max_value:
        max_location = cnt
        break
    else:
        if now_height < value:
            now_height = value
        answer.append(now_height)
    cnt += 1

now_height = 0
cnt = 0
for value in counter[::-1]:
    if value == max_value:
        if two_max:
            max_location = (1001 - cnt) - max_location
            break
        else:
            max_location = 1
            break
    else:
        if now_height < value:
            now_height = value
        answer.append(now_height)
    cnt += 1

answer.append(max_value * max_location)

print(sum(answer))
