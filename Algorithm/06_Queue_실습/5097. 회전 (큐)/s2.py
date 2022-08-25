import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))

    while m != 0:
        q.append(q.pop(0))
        m -= 1
    answer = q.pop(0)

    print(f'#{tc} {answer}')
