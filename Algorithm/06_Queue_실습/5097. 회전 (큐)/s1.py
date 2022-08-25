import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    k = m % n
    arr = list(map(int, input().split()))
    answer = arr[k]

    print(f'#{tc} {answer}')
