import math
answers = []
for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = 0
    for _ in range(n):
        x, y = map(int, input().split())
        r = math.ceil(math.sqrt(x*x + y*y) / 20)
        if r <= 0:
            answer += 10
        elif r <= 11:
            answer += 11 - r
    answers.append(f'#{tc} {answer}')

for answer in answers:
    print(answer)
