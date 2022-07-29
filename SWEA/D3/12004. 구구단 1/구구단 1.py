t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    answer = 'No'
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                answer = 'Yes'

    print(f'#{tc} {answer}')
