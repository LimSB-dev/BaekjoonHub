# 난쟁이의 수 = 9, 일곱 난쟁이 키의 합 = 100으로 고정이지만 확장성을 위해 변수 t, sum_height 생성
t = 9
sum_height = 100

heights = [0] * t

for i in range(t):
    n = int(input())
    heights[i] += n

for i in range(1 << t):
    seven_height = 0
    answer = []
    for j in range(t):
        if i & (1 << j):
            seven_height += heights[j]
            answer.append(heights[j])

    if seven_height == sum_height and len(answer) == 7:
        answer.sort()
        break

for i in answer:
    print(i)
