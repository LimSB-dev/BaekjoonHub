t = int(input())
answers = []

for _ in range(1, t + 1):
    x_start, x_end, y_start, y_end = map(int, input().split())
    time = min(x_end, y_end) - max(x_start, y_start)
    if time < 0:
        answers.append(0)
    else:
        answers.append(time)

for tc, answer in enumerate(answers):
    print(f'#{tc + 1} {answer}')