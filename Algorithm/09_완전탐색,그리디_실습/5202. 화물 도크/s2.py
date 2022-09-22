import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n = int(input())
    time = [list(map(int, input().split())) for _ in range(n)]
    time.sort(key=lambda x: x[1])
    i, j, answer = 0, 1, 1

    while j != n:
        if time[i][1] <= time[j][0]:
            answer += 1
            i, j = j, j + 1
        else:
            j += 1

    print(f'#{tc} {answer}')
